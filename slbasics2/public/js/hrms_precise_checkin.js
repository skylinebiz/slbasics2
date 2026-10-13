// Injected into the HRMS PWA (see slbasics2.override.hrms_pwa).
// Check-in / check-out is allowed only after a GPS fix accurate to the HR Settings limit (default 5 m) is fetched.
// Nothing is stored: the fix is only held in memory while the check-in modal is open.
(() => {
	const REQUIRED_ACCURACY_METERS = 20;
	const APPROXIMATE_LOCATION_METERS = 500;
	const WATCH_TIMEOUT_MS = 30000;

	const STALE_AFTER_MS = 20000;
	const MODAL_GRACE_MS = 2500;

	let watchId = null;
	let current = null; // latest reading: { latitude, longitude, accuracy, at }
	let active = false;
	let startedAt = 0;
	let message = "";

	const banner = document.createElement("div");
	banner.setAttribute("role", "alert");
	banner.style.cssText =
		"width:100%;box-sizing:border-box;padding:10px 12px;border-radius:8px;font:500 13px/1.4 system-ui,sans-serif;" +
		"display:none";

	function isValid() {
		return (
			!!current &&
			current.accuracy <= REQUIRED_ACCURACY_METERS &&
			Date.now() - current.at <= STALE_AFTER_MS
		);
	}

	function getModal() {
		return document.querySelector("ion-modal.show-modal");
	}

	// place the banner in the check-in modal: below the latitude/longitude line and above the map
	function placeBanner(modal) {
		const map = modal.querySelector("iframe");
		const anchor =
			(map && map.parentElement) ||
			[...modal.querySelectorAll("button")].find((b) => /^\s*confirm/i.test(b.textContent));
		if (!anchor || !anchor.parentNode) return false;
		if (banner.nextSibling !== anchor || banner.parentNode !== anchor.parentNode) {
			anchor.parentNode.insertBefore(banner, anchor);
		}
		return true;
	}

	function updateBanner() {
		const modal = active && getModal();
		if (!modal || !placeBanner(modal)) {
			banner.style.display = "none";
			return;
		}
		const valid = isValid();
		banner.style.display = "block";
		if (valid) {
			banner.style.background = "#ecfdf5";
			banner.style.color = "#047857";
			banner.style.border = "1px solid #a7f3d0";
			banner.textContent = `Precise location fetched (${current.accuracy.toFixed(
				1
			)} m). You can confirm now.`;
		} else {
			banner.style.background = "#fef2f2";
			banner.style.color = "#dc2626";
			banner.style.border = "1px solid #fecaca";
			banner.textContent = message || "Fetching precise location...";
		}
	}

	function stop() {
		if (watchId !== null) {
			navigator.geolocation.clearWatch(watchId);
			watchId = null;
		}
	}

	function evaluate() {
		if (!current) return;
		if (current.accuracy <= REQUIRED_ACCURACY_METERS) {
			message = "";
		} else if (current.accuracy > APPROXIMATE_LOCATION_METERS) {
			message =
				"Only approximate location is available. Please allow Precise location for this site and move outside.";
		} else {
			message = `Precise location (within ${REQUIRED_ACCURACY_METERS} m) could not be fetched yet (now ${current.accuracy.toFixed(
				1
			)} m). Please move outside to fetch your location.`;
		}
		updateBanner();
	}

	function start() {
		stop();
		current = null;
		active = true;
		startedAt = Date.now();
		message = "Fetching precise location...";

		if (!navigator.geolocation) {
			message = "Geolocation is not supported. Precise location is required to check in.";
			return;
		}

		// keep watching while the modal is open so the check always uses the latest reading
		watchId = navigator.geolocation.watchPosition(
			(position) => {
				const { latitude, longitude, accuracy } = position.coords;
				current = { latitude, longitude, accuracy, at: Date.now() };
				evaluate();
			},
			(error) => {
				current = null;
				message =
					"Precise location could not be fetched. Please move outside and enable location access.";
				if (error && error.code === 1)
					message =
						"Location permission denied. Please allow Precise location for this site.";
				updateBanner();
			},
			{ enableHighAccuracy: true, maximumAge: 0, timeout: WATCH_TIMEOUT_MS }
		);
	}

	function end() {
		stop();
		active = false;
		current = null;
		banner.style.display = "none";
		banner.remove();
	}

	// start when the employee taps Check In / Check Out
	document.addEventListener(
		"click",
		(event) => {
			if (event.target.closest && event.target.closest("#open-checkin-modal")) start();
		},
		true
	);

	setInterval(() => {
		if (!active) return;

		// modal closed (dismissed, swiped away or after a successful check-in)
		if (!getModal() && Date.now() - startedAt > MODAL_GRACE_MS) {
			end();
			return;
		}

		if (!current) message = message || "Fetching precise location...";
		else if (!isValid() && current.accuracy <= REQUIRED_ACCURACY_METERS) {
			message = "Location is not updating. Please move outside to fetch your location.";
		}
		updateBanner();

		// keep the Confirm button disabled until a precise location is available
		const valid = isValid();
		document.querySelectorAll("ion-modal button").forEach((btn) => {
			if (!/^\s*confirm/i.test(btn.textContent)) return;
			if (!valid) {
				btn.disabled = true;
				btn.dataset.preciseLock = "1";
			} else if (btn.dataset.preciseLock) {
				btn.disabled = false;
				delete btn.dataset.preciseLock;
			}
		});
	}, 300);

	function findCheckinDoc(node) {
		if (!node || typeof node !== "object") return null;
		if (node.doctype === "Employee Checkin") return node;
		for (const key of Object.keys(node)) {
			let value = node[key];
			if (typeof value === "string" && value.startsWith("{")) {
				try {
					value = JSON.parse(value);
					node[key] = value; // keep parsed so edits made below are serialised back
				} catch (e) {
					continue;
				}
			}
			const found = findCheckinDoc(value);
			if (found) return found;
		}
		return null;
	}

	// block Employee Checkin inserts without a precise location, and send the precise coordinates
	const originalFetch = window.fetch.bind(window);
	window.fetch = (input, init) => {
		try {
			const method = (
				(init && init.method) ||
				(input && input.method) ||
				"GET"
			).toUpperCase();
			if (
				method === "POST" &&
				init &&
				typeof init.body === "string" &&
				init.body.includes("Employee Checkin")
			) {
				const body = JSON.parse(init.body);
				const doc = findCheckinDoc(body);
				if (doc && doc.log_type) {
					if (!isValid()) {
						const text =
							"Precise location is required. Please move outside to fetch your location before checking in.";
						updateBanner();
						return Promise.resolve(
							new Response(
								JSON.stringify({
									exc_type: "ValidationError",
									_server_messages: JSON.stringify([
										JSON.stringify({ message: text }),
									]),
								}),
								{ status: 417, headers: { "Content-Type": "application/json" } }
							)
						);
					}
					doc.latitude = current.latitude;
					doc.longitude = current.longitude;
					init = { ...init, body: JSON.stringify(body) };
				}
			}
		} catch (e) {
			// never break unrelated requests
		}
		return originalFetch(input, init);
	};
})();
