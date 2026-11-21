# Vinted Assistant

A Codex skill for turning clothing photos into listings, handling buyer conversations and counteroffers, tracking sales, and preparing shipping labels. English is the default language. Buyer messages follow the buyer’s language when known; listing language is configurable.

## Requirements

- Codex desktop with local skills and browser-control tools.
- A signed-in Vinted session in the built-in browser (IAB), with supported photo uploads.
- Read access to Downloads and write access to a private workspace.
- Python 3 for photo intake. The script uses only the standard library.
- Codex automations for scheduled runs. The skill is not a scheduler or standalone server.
- Optional printer and supported IAB print controls. Without these, labels can only be prepared.

No Vinted API key or Gmail connector is required. Check tool availability in your own Codex environment.

## Setup

1. Copy this repository to `~/.codex/skills/vinted-assistent/`.
2. Create a separate private workspace. Copy `config.example.json` there as `config.local.json`, then fill in your account, paths, language, and preferences. Tell Codex which workspace to use.
3. Open Vinted in IAB and sign in yourself. Have Codex verify the account and establish authorization for publishing, pricing, messaging, counteroffers, and printing.
4. Start with: “Use $vinted-assistent. My workspace is [path]. There are new clothing photos in Downloads.”
5. Let Codex create missing logs and intake state. Inventory existing photos before establishing the baseline to avoid missing files or duplicating listings.

Configuration is a readable contract for the agent. The intake script receives Downloads and state directories through CLI arguments; it does not read JSON itself. Replace `<workspace>`, `<downloads>`, and `<skill-dir>` in instructions using your configuration and installation paths.

## Workflow

Photos are grouped by item. If a price is missing, Codex asks for an indication or permission to choose one. A clear real photo of someone wearing the item becomes the cover when available. Sizes, brands, and condition come from images, labels, and owner information.

Default maximum counteroffer discount is 15% below asking price, respecting higher item floors. Agree on authorization and exceptions first. No automatic offer acceptance, asking-price changes, or repeated saver follow-ups. Detailed instructions are in [SKILL.md](SKILL.md).

## Scheduling

Have Codex inspect existing automations before creating or updating jobs in your timezone:

| When | Work |
| --- | --- |
| Hourly | New messages and offers |
| Daily 09:00 | Dashboard and daily summary |
| Daily 12:00 | Photo intake, labels, and separate one-time favorites follow-up |
| Sunday 18:30 | Weekly report |

This repository does not create automations. Scheduled execution requires access to files, browser tools, and the signed-in session during each run. A scheduled start is not evidence of successful completion.

## Dashboard and labels

The skill records dated observations and maintains a dashboard in your private workspace. No personal dashboard or sales history is bundled. On first use, ask Codex to create a dashboard covering revenue, views, saves, sales, and comparable conversion ratios. Keep paid orders, completed sales, and bank payouts separate. Asking prices are not revenue.

Keep PDFs and print state outside Git. Print only for orders awaiting shipment, at most once per label version. A submitted print job does not prove physical output. Never blindly reprint an uncertain job.

## Status and privacy

Initial version adapted from a personal workflow. Intake scanning, staging, deduplication, and preservation of original files have been tested locally. Browser actions, negotiations, and physical printing still need end-to-end validation in each new environment. Interface changes, expired sessions, and platform limits can interrupt execution.

Account details, cookies, photos, order data, and labels stay local. The creator’s authorization does not transfer to other users of this skill.
