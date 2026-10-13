import json
import os

import frappe

PRECISE_CHECKIN_SCRIPT = (
	'<script src="/assets/slbasics2/js/hrms_precise_checkin.js?v={version}" defer></script>'
)


def inject_precise_checkin_script(response, request):
	"""Add the precise-location check-in script to the HRMS PWA page without modifying hrms."""
	if request.path != "/hrms" and not request.path.startswith("/hrms/"):
		return

	if response.status_code != 200 or "text/html" not in (response.content_type or ""):
		return

	html = response.get_data(as_text=True)
	if "hrms_precise_checkin.js" in html or "</body>" not in html:
		return

	settings = frappe.get_cached_doc("HR Settings")
	config = {
		"enabled": bool(settings.get("custom_require_precise_checkin")),
		"accuracy": float(settings.get("custom_checkin_required_accuracy") or 5),
	}
	if not config["enabled"]:
		return

	script_path = frappe.get_app_path("slbasics2", "public", "js", "hrms_precise_checkin.js")
	script = PRECISE_CHECKIN_SCRIPT.format(version=int(os.path.getmtime(script_path)))
	config_tag = f"<script>window.slbasics2_checkin = {json.dumps(config)}</script>"
	response.set_data(html.replace("</body>", f"{config_tag}{script}</body>", 1))
