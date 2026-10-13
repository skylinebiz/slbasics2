# Changelog

All notable changes to SLBasics2 are documented in this file.

Versioning follows [Semantic Versioning](https://semver.org/): MAJOR for breaking changes, MINOR for backward-compatible features, and PATCH for backward-compatible fixes.

## [2.0.0] - 2026-10-13

### Added

- **HRMS mobile app (PWA) precise-location check-in.** When enabled, employees can check in or out only after a GPS fix within the configured accuracy (default 5 m) is fetched. The check-in modal shows the live accuracy and, until the fix is precise enough, an alert asking the employee to move outside. The **Confirm** button stays disabled, and any Employee Checkin created without a precise fix is blocked. The check is re-evaluated on the latest reading, so moving out of range again blocks the check-in, and nothing about the fix is stored.
- New fields on **HR Settings**, next to *Allow Geolocation Tracking*:
  - **Require Precise Location for Mobile Check-in**: turns the rule on or off for all employees.
  - **Required Location Accuracy (meters)**: the accuracy limit, defaults to `5`.
- The behaviour is added from `slbasics2` (an `after_request` hook injects the script into the `/hrms` page); no changes were made to the `hrms` app.

### Changed

- **Behaviour change:** with **Require Precise Location for Mobile Check-in** enabled, mobile check-ins that previously succeeded with a coarse location are now rejected until a precise fix is available. The setting is off by default, so existing behaviour is unchanged until it is enabled.

## [1.4.0] - 2026-10-01

### Added

- **User** records are now restricted to a single simultaneous session: **Simultaneous Sessions** is set to `1` every time a User is created or updated, so logging in on a second device ends the earlier session. Existing users are switched to a single session the next time their record is saved.
- The **Simultaneous Sessions** field on User is now read-only, so it can no longer be edited from the form.

## [1.3.0] - 2026-09-18

### Fixed

- **Employee Checkin Summary** report: sorting by the In Time / Last Punch columns was alphabetical instead of chronological once times were shown as text (e.g. `01:00 PM` sorted before `09:00 AM`).

### Changed

- **Employee Checkin Summary** report: In Time and Last Punch now show 24-hour time (`HH:MM:SS`), keeping them correctly sortable. Punch Records continues to show 12-hour AM/PM, since it's a comma-separated list rather than a single sortable value.

## [1.2.0] - 2026-09-17

### Added

- New **Aadhar Number (UID Number)** field on Employee > Personal Details, with validation on both client and server side: only 12 digits are accepted, and the value is auto-formatted as `1234 5678 9101` after entry.
- New **Category** select field on Employee > Personal Details (SC / ST / OBC / EWS / General).

### Changed

- **Employee Checkin Summary** report now shows punch times in 12-hour format (e.g. `09:15 am`) instead of 24-hour format.

## [1.1.0] - 2026-09-03

### Added

- New **Employee Checkin Summary** report (Report > Employee Checkin Summary). Given a date, it groups all Employee Checkin records by employee for that day and shows Employee (name - attendance device ID), Designation, In Time (first punch), Last Punch (last punch), and Punch Records (all punches, comma-separated).

## [1.0.1] - 2026-08-27

### Fixed

- Fixed barcode scanner override linting issues.
- Fixed `cur_frm` usage issue in global shortcuts.
- Resolved lint formatting and Semgrep errors.

## [1.0.0] - 2026-08-25

### Added

- Initial release: global keyboard shortcuts and barcode scanner override JS.
