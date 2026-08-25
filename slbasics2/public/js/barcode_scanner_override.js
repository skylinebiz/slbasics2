/* global erpnext */

frappe.provide("erpnext.utils");

if (erpnext.utils.BarcodeScanner && !erpnext.utils.BarcodeScanner.__cleanup_override) {
	erpnext.utils.BarcodeScanner.__cleanup_override = true;

	erpnext.utils.BarcodeScanner.prototype.clean_up = function () {
		if (this.frm && this.items_table_name) {
			this.frm.refresh_field(this.items_table_name);
		}
	};
}
