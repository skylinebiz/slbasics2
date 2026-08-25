frappe.provide("erpnext.utils");

if (erpnext.utils.BarcodeScanner && !erpnext.utils.BarcodeScanner.__cleanup_override) {
    
    erpnext.utils.BarcodeScanner.__cleanup_override = true;

    erpnext.utils.BarcodeScanner.prototype.clean_up = function () {
        // Safe access to the active form object
        if (cur_frm && this.items_table_name) {
            cur_frm.refresh_field(this.items_table_name);
        }
    };
}
