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

## Version history

See `git log -- games/engineers-village`.
