# Reporting and scheduling

The skill defines execution; actual Codex automations provide scheduling. Inspect existing jobs and use automation_update to preserve or change them. Do not write scheduler files directly or create duplicate jobs. Use the configured timezone, default Europe/Amsterdam.

Suggested schedule, only after owner authorization and actual automation setup:
- Hourly: handle new messages/offers under operations.md. Keep routine runs quiet; surface required decisions or meaningful access blockers.
- Daily 09:00: update account/order observations and dashboard; give the requested short daily summary of new sales, confirmed amounts, open offers, blockers, and last observation time.
- Daily 12:00: inspect new Downloads photos, batch questions about missing pricing authority, and process complete authorized items. Check labels and print only unprocessed printable versions. Keep favorites follow-up separate and do not duplicate it.
- Sunday 18:30: weekly performance and revenue summary with a few evidence-backed next steps.

Before each update, read the log and verify the signed-in account. Record title, item ID, asking price, status, views, saves, and timestamp. Keep received/sent/accepted offers distinct from paid purchases. Record each sale once per order, using confirmed item revenue, confirmation date, and any cancellation/refund. Separate paid/pending, completed, and bank-paid-out states. Unknown amounts remain unknown; asking prices are not revenue. New listings and relistings have separate IDs and cohorts.

Show cumulative and period revenue, views, saves, and sales. Per item and week, show saves/views, sales/views, and linked sales/saves where available. Numerators and denominators must cover the same period and listings. Keep sold items in the cohort to avoid survivorship bias. Current favorites counters are stocks and net changes, not unique new saver events. Views are not unique visitors. Label aggregate ratios as signals rather than proven person-level funnels. When comparable weekly observations are missing, leave weekly CVR blank with a reason. Never distribute cumulative views across days arbitrarily.

Offer timing analysis requires linked save events, recipients, offer timestamps/prices, and confirmed purchases. Do not claim causality without comparable groups and sufficient follow-up. Recommend specific tests supported by observations.

Preserve photos and NL/EN controls when updating HTML. English is the default for a new dashboard and reports, unless the user requests another language. Parse large datasets selectively; do not print base64 photos. Check JavaScript syntax and, when permitted, rendered charts and the language switch. Link to the absolute HTML path without a fragment because some file viewers cannot open fragment links. Clearly date stale data when access fails. Reports must specify period, population, and missing observations.
