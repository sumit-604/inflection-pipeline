# Engineer's Village

A 3D maths and science puzzle game for children (Class 3 and Class 5 profiles).
The player is the village's new Junior Engineer. Villagers pose problems; solving
them changes the village: the bridge gets built, the school lights come on, the
windmill grinds, the tank fills, the roof is patched, and the market stall stocks up.

## Files

- `index.html`  the whole game in one file: styles, HTML, and the game script.
  It loads three.js from a CDN via an import map and needs no build step.

## Run it

Open `index.html` in a browser, or serve the folder with any static server.
Published copy: https://claude.ai/code/artifact/675adcb1-3c28-41fa-bf7f-274f4ca01c7e

## Content

- Six villager jobs with a harder Level 2 on replay: bridge (lengths), roof (area,
  packs, cost), school (circuits), tank (volume and rates), windmill (gears and
  ratios), market (balance scales and money).
- One hundred short situations carried by eight wandering villagers, across ten
  topics. Each regenerates its numbers on replay. See `SITUATIONS` in the script.
- Progress saves per profile in the browser (localStorage). A parent view shows
  attempts and topics covered (long press the notebook).
- Real shopping: pick items and quantities, work out the bill, hand over notes
  and coins from the wallet, count the change. Around 40 shops and stalls across
  Setugram Bazaar, the town, Sector 18 and two city market blocks.
- A backpack (B): eat food for energy, wear bought clothes and shoes, hold gear
  (bat, racket, football, kite, skipping rope, spinning top, marbles, chess) and
  play with it (F), read story books for a question and a reward.
- Larger interiors with several rooms joined by doorways: home, school, clinic,
  office, mall, supermarket, lobby, station and hall have floor plans.
- A zoomable map (M): scroll or buttons to zoom, drag to pan, a place list, and
  Find buttons. The corner minimap is a close-up around the player.
- Wheels roll at true speed with spokes and cranks; engine hum while riding,
  market murmur near bazaars, traffic rumble in the city.

## Version history

See `git log -- games/engineers-village`.
