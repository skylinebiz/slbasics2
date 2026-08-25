app_name = "slbasics2"
app_title = "SLBasics2"
app_publisher = "Harshit Jain"
app_description = "Basic Utility Functionalities from SkylineBiz"
app_email = "harshit@skylinebiz.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "slbasics2",
# 		"logo": "/assets/slbasics2/logo.png",
# 		"title": "SLBasics2",
# 		"route": "/slbasics2",
# 		"has_permission": "slbasics2.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/slbasics2/css/slbasics2.css"
# app_include_js = "/assets/slbasics2/js/slbasics2.js"

# include js, css files in header of web template
# web_include_css = "/assets/slbasics2/css/slbasics2.css"
# web_include_js = "/assets/slbasics2/js/slbasics2.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "slbasics2/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "slbasics2/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "slbasics2.utils.jinja_methods",
# 	"filters": "slbasics2.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "slbasics2.install.before_install"
# after_install = "slbasics2.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "slbasics2.uninstall.before_uninstall"
# after_uninstall = "slbasics2.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "slbasics2.utils.before_app_install"
# after_app_install = "slbasics2.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "slbasics2.utils.before_app_uninstall"
# after_app_uninstall = "slbasics2.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "slbasics2.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "slbasics2.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"slbasics2.tasks.all"
# 	],
# 	"daily": [
# 		"slbasics2.tasks.daily"
# 	],
# 	"hourly": [
# 		"slbasics2.tasks.hourly"
# 	],
# 	"weekly": [
# 		"slbasics2.tasks.weekly"
# 	],
# 	"monthly": [
# 		"slbasics2.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "slbasics2.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "slbasics2.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "slbasics2.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "slbasics2.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["slbasics2.utils.before_request"]
# after_request = ["slbasics2.utils.after_request"]

# Job Events
# ----------
# before_job = ["slbasics2.utils.before_job"]
# after_job = ["slbasics2.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"slbasics2.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

