# Metingen en planning

De skill beschrijft de uitvoering. Alleen echte Codex-automations verzorgen de planning. Inspecteer bestaande automations en gebruik automation_update om ze te behouden of bij te werken; schrijf geen ruwe schedulerbestanden en maak geen duplicaten. Tijdzone Europe/Amsterdam.

Gewenst ritme:
- Elk uur: nieuwe reacties/biedingen afhandelen volgens operations.md. Routine stil; meld een vereiste beslissing of wezenlijk toegangsprobleem.
- Dagelijks 09:00: account, orders en dashboard bijwerken; geef een korte dagelijkse update met nieuwe verkopen, bevestigde bedragen, open biedingen en concrete blokkades. Vermeld de laatste meettijd.
- Dagelijks 12:00: nieuwe Downloads-foto’s inventariseren en gebundeld prijzen/mandaat vragen wanneer nodig; voer complete geautoriseerde items uit. Controleer daarnaast labels en print alleen nog niet verwerkte printbare exemplaren. De bestaande aparte favorietencheck blijft op 12:00 draaien en wordt niet gedupliceerd.
- Zondag 18:30: weekupdate met prestaties, omzet en één of enkele onderbouwde vervolgacties.

Lees voor iedere update het log en bevestig het account in IAB. Leg per artikel titel, id, vraagprijs, status, views, favorieten en meettijd vast. Log ontvangen/verstuurde/geaccepteerde biedingen apart van betaalde aankopen. Registreer een verkoop één keer per order, werkelijke artikelopbrengst, bevestigingsdatum en eventuele annulering/refund. Onderscheid betaald/in behandeling, voltooid en uitbetaald. Onbekende prijs blijft onbekend; vraagprijs is geen omzet. Nieuwe advertenties en herplaatsingen houden een eigen id en cohort.

Dashboard: cumulatieve en periodieke omzet, views, saves en sales; per artikel en per week de ratio’s saves/views, sales/views en waar gekoppeld sales/saves. Gebruik views- en saveverandering in dezelfde periode en dezelfde artikelen als sales. Behoud verkochte artikelen in de cohort om survivorship bias te vermijden. Actuele favorietentellers zijn standen en netto veranderingen, geen telling van unieke nieuwe savers. Profielviews zijn geen unieke bezoekers. Vermeld wanneer ratio’s slechts geaggregeerde signalen zijn; benoem ze niet als bewezen individuele funnel. Bij geen vergelijkbare weekmetingen laat week-CVR leeg met reden; verdeel geen cumulatieve views willekeurig over dagen.

Voor aanbodtiming is een gekoppeld save-event, ontvanger, aanbodtijd, prijs en bevestigde aankoop nodig. Rapporteer geen causaliteit zonder vergelijkbare groepen en voldoende opvolging. Adviseer alleen concrete tests op basis van waarnemingen.

Behoud NL/EN-switch en bestaande foto's bij HTML-updates. Parse grote datasetblokken gericht; print geen base64-foto’s. Controleer JS-syntax en waar toegestaan de gerenderde pagina en switch. Link in chat naar het absolute HTML-pad zonder fragment, omdat de bestandsviewer links met # eerder niet kon openen. Vermeld bij ontbrekende toegang dat oude data oud is. Geef dagelijkse/wekelijkse updates in de eigenaar zijn directe Nederlandse stijl met periode, populatie en ontbrekende metingen.
