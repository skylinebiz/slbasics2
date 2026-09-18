# Changelog

All notable changes to SLBasics2 are documented in this file.

Versioning follows [Semantic Versioning](https://semver.org/): MAJOR for breaking changes, MINOR for backward-compatible features, and PATCH for backward-compatible fixes.

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
