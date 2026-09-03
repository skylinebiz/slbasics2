// Copyright (c) 2026, SkylineBiz and contributors
// For license information, please see license.txt

frappe.query_reports["Employee Checkin Summary"] = {
	filters: [
		{
			fieldname: "date",
			label: __("Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today(),
			reqd: 1,
		},
		{
			fieldname: "employee",
			label: __("Employee"),
			fieldtype: "Link",
			options: "Employee",
		},
	],
};
