import re

import frappe
from frappe import _

AADHAR_NUMBER_PATTERN = re.compile(r"^\d{12}$")


def validate_aadhar_number(doc, method=None):
	aadhar_number = doc.get("custom_aadhar_number")
	if not aadhar_number:
		return

	digits_only = re.sub(r"\D", "", aadhar_number)

	if not AADHAR_NUMBER_PATTERN.match(digits_only):
		frappe.throw(_("Aadhar Number must be exactly 12 digits"))

	doc.custom_aadhar_number = " ".join(
		digits_only[i : i + 4] for i in range(0, len(digits_only), 4)
	)
