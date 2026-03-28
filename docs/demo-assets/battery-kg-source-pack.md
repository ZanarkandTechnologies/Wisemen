# Battery Knowledge Graph Source Pack

Last updated: March 28, 2026

Purpose: give Miro Supply a fast, good-enough set of real-world anchors for seeding a battery supply-chain knowledge graph. This is intentionally optimized for hackathon speed, not master-data perfection.

## Recommended use

Use these sources in two layers:

1. **Grounding layer** — real firms, products, regions, and supply-chain roles from official company/government sources
2. **Scenario layer** — synthetic entities derived from the real firms so the demo can stay commercially legible without making hard claims about a specific company

## Fast seed set for the current demo

### Lithium / lithium precursor anchors

- **Ganfeng Lithium** — vertically integrated lithium company spanning resource development, refining, battery manufacturing, and recycling
  - Source: https://www.ganfenglithium.com/index_en
  - Source: https://www.ganfenglithium.com/about1_en.html
- **Albemarle** — major lithium and battery-material supplier with battery-products and hydroxide capabilities
  - Source: https://www.albemarle.com/offerings/lithium/products/battery-products
  - Source: https://www.albemarle.com/us/en/who-we-are/global-locations
- **SQM** — large Chilean lithium producer with lithium carbonate and hydroxide production at Salar del Carmen
  - Source: https://sqm.com/en/productos/litio-y-derivados/
  - Source: https://sqm.com/en/noticia/sqm-anuncia-acuerdo-de-suministro-de-litio-a-largo-plazo-con-ford-motor-company/

### Cathode / precursor anchors

- **POSCO Future M** — cathode and precursor producer with plants in Korea, China, and Canada
  - Source: https://www.poscofuturem.com/en/business/energy.do
  - Source: https://www.poscofuturem.com/resources/file/2024poscofuturem_en.pdf
- **EcoPro BM / EcoPro group** — cathode-material producer with official corporate brochure material
  - Source: https://www.ecopro.co.kr/_files/brochure_pdf/20230403/9c425abd069a42e3334ab1557d1d0ecf.pdf

### Separator anchors

- **Asahi Kasei / Hipore / Celgard** — major separator footprint in North America, Japan, South Korea, and Canada
  - Source: https://www.asahi-kasei.com/news/2023/e231031.html
  - Source: https://www.asahi-kasei.com/news/2024/e240425.html
  - Source: https://www.celgard.com/
  - Source: https://www.celgard.com/about-us/locations
- **Toyota Tsusho** — useful anchor for battery-component supply-chain and separator partnerships in North America
  - Source: https://www.toyota-tsusho.com/english/press/detail/250731_006650.html
  - Source: https://www.toyota-tsusho.com/english/press/detail/250619_006626.html
  - Source: https://www.toyota-tsusho.com/english/ir/library/integrated-report/pdf/ar2025e_03.pdf

### Cell / pack / downstream demand anchors

- **LG Energy Solution** — battery manufacturer with explicit lithium offtake and North America expansion signals
  - Source: https://news.lgensol.com/company-news/press-releases/2435/
  - Source: https://news.lgensol.com/company-news/press-releases/2177/
  - Source: https://www.lgensol.com/assets/file/2023_company_profile_EN.pdf
- **Panasonic Energy** — North American EV cell manufacturing footprint in Nevada and Kansas
  - Source: https://na.panasonic.com/news/panasonic-energy-begins-mass-production-at-new-automotive-lithium-ion-battery-factory-in-kansas-aiming-for-annual-capacity-of-32-gwh-to-accelerate-us-local-production
  - Source: https://energy.na.panasonic.com/
- **Ford / Honda / Toyota-linked demand signals** — useful customer or downstream demand nodes for the graph
  - Source: https://sqm.com/en/noticia/sqm-anuncia-acuerdo-de-suministro-de-litio-a-largo-plazo-con-ford-motor-company/
  - Source: https://news.lgensol.com/company-news/press-releases/2177/
  - Source: https://www.asahi-kasei.com/news/2024/e241101_3.html

### Macro / public data anchors

- **USGS Lithium Statistics and Information** — public grounding for lithium supply-chain facts and scenario realism
  - Source: https://www.usgs.gov/centers/national-minerals-information-center/lithium-statistics-and-information
- **USGS Mineral Commodity Summaries 2026** — recent public battery-material context and supply-chain framing
  - Source: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf
- **USGS world minerals outlook for lithium capacity** — useful macro risk context
  - Source: https://pubs.usgs.gov/sir/2025/5021/Version%201.0/sir20255021.pdf

## Suggested synthetic entity set

Use the real firms above as inspiration, but seed the live demo with synthetic entities like:

- **Northstar Battery Components** — Nevada module plant
- **Jade Ridge Lithium Materials** — China-based precursor supplier inspired by Ganfeng/SQM/Albemarle style upstream players
- **Blue Mesa Lithium Chemicals** — alternate lithium refiner with North America relevance
- **Hanseong Cathode Processing** — Korean cathode/precursor processor inspired by POSCO Future M / EcoPro BM
- **Seika Separator Systems** — separator supplier inspired by Asahi Kasei / Celgard footprint
- **Continental Freight Gateways** — logistics / rerouting node
- **FleetMotion OEM** — commercial EV fleet customer node
- **North American Trade Policy Office** — regulator / export-control observer node

## How to model them in the graph

For each seeded firm/node, attach:

- `entity_type`: supplier / processor / separator_supplier / battery_maker / OEM / regulator / logistics_node / plant
- `country`
- `region`
- `material_role`
- `dependency_level`: critical / high / medium
- `shock_exposure`: export_controls / port_delay / quality_issue / demand_spike / policy_change
- `source_confidence`: official / public-statistics / synthetic-derived
- `source_url`

## What to fake confidently

Safe-to-synthesize fields for the demo:

- exact contract volumes
n- exact inventory levels at specific firms
- exact production allocations
- exact customer concentration

Keep real-world grounding on:

- who operates in which part of the chain
- which regions matter
- which materials or components they are associated with
- which categories of disruption are plausible

## Best immediate use in Ralph

1. Seed 8-12 high-signal entities from `battery-kg-seed-firms.json`
2. Keep the plant itself synthetic
3. Use official sources only as grounding references, not as claims that those firms are literally in the live scenario
4. If time is short, prioritize:
   - Ganfeng Lithium
   - Albemarle
   - SQM
   - POSCO Future M
   - EcoPro BM
   - Asahi Kasei / Celgard
   - LG Energy Solution
   - Panasonic Energy
   - Toyota Tsusho

## Caveat

This is a hackathon source pack, not procurement-grade intelligence. Use it to make the graph feel plausible and industry-literate, then keep the demo language honest.
