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

	script_path = frappe.get_app_path("slbasics2", "public", "js", "hrms_precise_checkin.js")
	script = PRECISE_CHECKIN_SCRIPT.format(version=int(os.path.getmtime(script_path)))
	response.set_data(html.replace("</body>", f"{script}</body>", 1))
