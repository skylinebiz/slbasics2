(function () {
	const settings = (frappe.listview_settings["Item"] = frappe.listview_settings["Item"] || {});

	// Keep the onload other apps have already set instead of replacing it
	const onload = settings.onload;

	settings.onload = function (listview) {
		if (onload) onload.call(this, listview);

		listview.page.add_inner_button(__("UOM Calculator"), function () {
			frappe.slbasics2.open_uom_calculator();
		});
	};
})();
