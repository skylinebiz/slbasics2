frappe.ui.form.on("Employee", {
	custom_aadhar_number: function (frm) {
		let digits = (frm.doc.custom_aadhar_number || "").replace(/\D/g, "").slice(0, 12);
		let formatted = digits.replace(/(\d{4})(?=\d)/g, "$1 ");

		if (formatted !== frm.doc.custom_aadhar_number) {
			frm.set_value("custom_aadhar_number", formatted);
		}

		if (digits && digits.length !== 12) {
			frappe.show_alert({
				message: __("Aadhar Number must be exactly 12 digits"),
				indicator: "orange",
			});
		}
	},

	validate: function (frm) {
		let digits = (frm.doc.custom_aadhar_number || "").replace(/\D/g, "");

		if (digits && digits.length !== 12) {
			frappe.throw(__("Aadhar Number must be exactly 12 digits"));
		}
	},
});
