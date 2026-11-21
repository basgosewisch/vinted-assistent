# Messages, offers, and shipping labels

## Hourly check

Read new messages/offers and their conversation history. Answer product questions using known information, in the buyer’s language when clear; otherwise English. Batch unknown measurements/details for the owner. Do not promise shipping dates or attributes without evidence.

For asking price P and configured maximum discount d (default 15%), calculate counteroffer C as max((1 − d/100) × P, explicit higher item floor), rounded up to eurocents. Round up to whole euros if required by the interface. An offer below C receives one polite reply and the built-in counteroffer C. For example: “Hi! Thanks for your offer. That is a bit low for this item, but I can offer €[C].” Refer to condition only when known. For an offer between C and P, return that same amount through the offer tool where supported; do not automatically accept. If unsupported, say that amount works and invite the buyer to purchase, without claiming offer acceptance or payment. Never offer less than the buyer already offered. Offers above asking price and unusual bundles need owner review. Do not repeat an unanswered counteroffer or spontaneously discount every saved item.

Follow up only on new reachable favorites once daily at 12:00, asking whether the person has questions or would like to make an offer. Skip existing conversations, negotiations, previously contacted recipients, sold/reserved items. No repeated “still interested?” messages without separate authorization. Log recipient + item ID + timestamp + outcome; check the log and conversation before sending.

## Daily shipping check

Inspect paid orders awaiting shipment and visible deadlines. Distinguish printable PDFs, QR/drop-off codes, and shipping without printing. Do not open or print labels for cancelled, already shipped, or unrelated orders.

Download required official label PDFs through signed-in IAB. Save to `outputs/verzendlabels/` with order ID and item name. Maintain an index of order ID, item ID, deadline, source, local file, download time, opened state, print status, and label version/hash when available. Use the relevant PDF skill for inspection. Verify a readable PDF for the correct order; do not expose addresses in chat or the dashboard.

If printing is enabled and authorized, open printable labels in IAB and use supported print controls. Keep actual-size/100% scaling and suitable existing printer settings. Do not open another app to bypass the IAB restriction. If print controls, printer selection, or access are unavailable, keep the PDF ready and state that physical printing is unconfirmed. A submitted print job does not prove paper was produced.

Print each order/label version at most once. Mark uncertain submissions “unknown” and inspect the queue through permitted controls or ask the owner; never blindly resubmit. Reprint only on explicit instruction or a verified new label version, explaining why. Downloading or printing never marks an order shipped. An offer or negotiation is not a sale.
