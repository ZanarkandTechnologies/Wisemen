# Battery Knowledge Graph Quick Seed

Use this file as a compact grounding layer for the demo graph.

- Northstar Battery Components — Nevada battery-module factory serving commercial EV fleets
- Ganfeng Lithium — China-based lithium supplier and processor; key source of lithium precursor
- Albemarle — lithium supplier with battery-grade lithium products
- SQM — Chile-based lithium carbonate and hydroxide producer
- POSCO Future M — South Korea cathode and precursor producer
- EcoPro BM — South Korea cathode-material producer
- Asahi Kasei / Hipore — separator supplier with Japan / North America footprint
- Celgard — U.S. separator and membrane manufacturer
- Toyota Tsusho — supply-chain integrator with battery-material and separator partnerships
- LG Energy Solution — battery maker with North America demand pull
- Panasonic Energy — battery maker with Nevada and Kansas manufacturing footprint
- FleetMotion OEM — synthetic downstream commercial EV customer node
- Port of Long Beach — logistics chokepoint and rerouting node
- North American Trade Policy Office — synthetic regulator / export-control observer

Suggested key relationships:

- Ganfeng Lithium SUPPLIES lithium precursor
- Albemarle SUPPLIES battery-grade lithium products
- SQM SUPPLIES lithium carbonate / hydroxide
- POSCO Future M DEPENDS_ON lithium precursor and cathode feedstocks
- Asahi Kasei / Celgard SUPPLIES separator film
- Toyota Tsusho SHIPS_TO battery makers and component suppliers
- Northstar Battery Components PURCHASES_FROM upstream suppliers
- Northstar Battery Components DELIVERS_TO FleetMotion OEM
- Northstar Battery Components EXPOSED_TO lithium precursor delays
- North American Trade Policy Office REGULATES export flows
