# Release Notes

All notable changes to SLBasics2 are documented in this file.

Versioning follows [Semantic Versioning](https://semver.org/): MAJOR for breaking changes, MINOR for backward-compatible features, and PATCH for backward-compatible fixes.

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
