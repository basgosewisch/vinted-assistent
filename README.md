# Vinted-assistent

Een Codex-skill die helpt om kledingfoto’s te verwerken, advertenties te plaatsen, reacties en biedingen af te handelen en verkoop bij te houden.

## Nodig

- Codex desktop met toegang tot lokale skills en browserbediening.
- Een ingelogde Vinted-sessie in de ingebouwde browser (IAB), met ondersteunde foto-uploadtools.
- Leesrechten op Downloads en schrijfrechten op een eigen werkmap.
- Python 3 voor het intakescript; alleen standaardbibliotheek, geen pip-packages nodig.
- Codex-automations voor geplande runs. De skill zelf is geen scheduler of zelfstandige server.
- Optioneel een printer en ondersteunde IAB-printbediening. Zonder die bediening kunnen labels alleen worden klaargezet.

Geen Vinted-API-sleutel of Gmail-connector nodig. Toolbeschikbaarheid moet in de eigen Codex-omgeving worden gecontroleerd.

## Installeren

1. Kopieer deze repository naar `~/.codex/skills/vinted-assistent/`.
2. Maak een afzonderlijke privéwerkmap. Kopieer `config.example.json` daar als `config.local.json` en vul account, paden en voorkeuren in. Geef Codex die werkmap bij de eerste opdracht.
3. Open Vinted in IAB en log zelf in. Laat Codex het account controleren en het mandaat afspreken voor publiceren, prijzen, berichten, tegenbiedingen en printen.
4. Start met: ‘Gebruik $vinted-assistent. Mijn werkmap is [pad]. Er staan nieuwe kledingfoto’s in Downloads.’
5. Laat Codex ontbrekende log- en intakebestanden aanmaken. Bestaande foto’s eerst inventariseren; leg pas na beoordeling een baseline vast. Publiceer niets dubbel.

De configuratie is een leesbaar contract voor de agent. Het intakescript krijgt Downloads en de intakewerkmap expliciet via CLI-argumenten; het leest JSON niet zelfstandig. `<workspace>`, `<downloads>` en `<skill-dir>` in de instructies worden uit de eigen configuratie en installatie ingevuld.

## Werkwijze

Foto’s worden per artikel gegroepeerd. Ontbreekt een prijs, dan vraagt Codex een indicatie of toestemming zelf te bepalen. Een duidelijke menselijke draagfoto gaat vooraan. Merken, maten en conditie worden gebaseerd op foto’s, labels en de eigenaar zijn informatie.

Voor onderhandelingen is de standaard maximaal 15% korting op de actuele vraagprijs, met hogere artikelbodems gerespecteerd. Stel het mandaat en eventuele afwijkingen vooraf vast. Geen automatische acceptatie, prijsverlaging of herhaalde saver-berichten. De precieze uitvoering staat in [SKILL.md](SKILL.md).

## Terugkerende taken instellen

Laat Codex bestaande automations eerst controleren en daarna via de automation-tool instellen, in je eigen tijdzone:

| Moment | Werk |
| --- | --- |
| Elk uur | Nieuwe reacties en biedingen |
| Dagelijks 09:00 | Dashboard en dagupdate |
| Dagelijks 12:00 | Foto-intake, labels en aparte eenmalige favorietenopvolging |
| Zondag 18:30 | Weekoverzicht |

Deze repository maakt geen automations aan. Geplande uitvoering vereist dat de betreffende Codex-omgeving toegang tot bestanden, browser en sessie heeft. Een geplande start bewijst geen geslaagde uitvoering.

## Dashboard en labels

De skill schrijft gedateerde waarnemingen in de privéwerkmap en houdt het dashboard daar bij. Een bestaand persoonlijk dashboard wordt niet meegeleverd. Laat Codex bij eerste gebruik een dashboard maken met omzet, views, saves, sales en alleen vergelijkbare conversieratio’s. Betaalde orders, voltooide verkopen en bankuitbetalingen blijven afzonderlijk. Vraagprijzen tellen niet als omzet.

Label-PDF’s en printstatus horen in de privéwerkmap, nooit in Git. Print alleen voor nog te verzenden orders en maximaal eenmaal per labelversie. Een printopdracht is geen bewijs dat papier uit de printer kwam. Geen blinde herprints bij onzekere status.

## Status

Eerste versie, afgeleid van een persoonlijke werkwijze. Het intakescript is lokaal controleerbaar. Browseracties, onderhandelingen en fysieke printopdrachten vereisen nog een volledige test in iedere nieuwe omgeving. Geen garantie op ononderbroken uitvoering bij een gewijzigde Vinted-interface, sessieverlies of platformlimieten.

Accountgegevens, cookies, foto's, ordergegevens en labels blijven lokaal. De toestemming van de maker geldt niet voor andere gebruikers van deze skill.
