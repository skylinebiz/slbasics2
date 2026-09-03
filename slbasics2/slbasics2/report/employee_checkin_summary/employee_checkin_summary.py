# Copyright (c) 2026, SkylineBiz and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import format_time, get_datetime

TIME_FORMAT = "hh:mm a"


def execute(filters=None):
	filters = frappe._dict(filters or {})
	validate_filters(filters)

	columns = get_columns()
	data = get_data(filters)
	return columns, data


def validate_filters(filters):
	if not filters.get("date"):
		frappe.throw(_("Please select a Date"))


def get_columns():
	return [
		{
			"label": _("Employee"),
			"fieldname": "employee_detail",
			"fieldtype": "Data",
			"width": 280,
		},
		{
			"label": _("Designation"),
			"fieldname": "designation",
			"fieldtype": "Link",
			"options": "Designation",
			"width": 160,
		},
		{
			"label": _("In Time"),
			"fieldname": "in_time",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": _("Last Punch"),
			"fieldname": "last_punch",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": _("Punch Records"),
			"fieldname": "punch_records",
			"fieldtype": "Data",
			"width": 450,
		},
	]


def get_data(filters):
	checkin_filters = {"time": ["between", [filters.date, filters.date]]}
	if filters.get("employee"):
		checkin_filters["employee"] = filters.employee

	checkins = frappe.get_all(
		"Employee Checkin",
		filters=checkin_filters,
		fields=["employee", "time"],
		order_by="employee asc, time asc",
	)

	if not checkins:
		return []

	employee_ids = list({row.employee for row in checkins})
	employees = frappe.get_all(
		"Employee",
		filters={"name": ["in", employee_ids]},
		fields=["name", "employee_name", "attendance_device_id", "designation"],
	)
	employee_map = {row.name: row for row in employees}

	punches_by_employee = {}
	for row in checkins:
		punches_by_employee.setdefault(row.employee, []).append(get_datetime(row.time))

	data = []
	for employee, punches in punches_by_employee.items():
		emp = employee_map.get(employee) or frappe._dict()

		employee_name = emp.get("employee_name") or employee
		device_id = emp.get("attendance_device_id")
		employee_detail = f"{employee_name} - {device_id}" if device_id else employee_name

		punches = sorted(punches)
		punch_times = [format_time(punch, TIME_FORMAT) for punch in punches]

		data.append(
			{
				"employee_detail": employee_detail,
				"designation": emp.get("designation"),
				"in_time": punch_times[0],
				"last_punch": punch_times[-1],
				"punch_records": ", ".join(punch_times),
			}
		)

	data.sort(key=lambda row: row["employee_detail"])
	return data
