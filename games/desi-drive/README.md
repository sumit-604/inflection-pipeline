# Desi Drive

RishSchoolDays series, Game 2. Created by Rishabh Sharma, age 9.
Slogan: **Just live it!**

A 3D driving game in an Indian city. One HTML file. Three.js 0.160 loads
from the jsdelivr CDN.

## What is in the game

- **7 vehicles:** Chotu Hatch (free), Tuk-Tuk Auto, Rani Sedan, Sher SUV
  (off-road), Bharat Truck, City Bus, Toofan GT.
- **Garage:** buy cars, paint them (10 colours), repair them at the garage.
  Upgrade 5 parts (engine, tyres, brakes, nitro, body) up to level 5 with points.
- **World:** a city grid with buildings, traffic, 9 traffic signals,
  2 speed cameras, street lamps, a petrol pump, a garage, a parking lot,
  a park, a temple, a highway and a race circuit with stands.
- **Free drive:** points for distance, stars, drifts and near misses.
  Fines for jumping a red light (50) and speeding past a camera (40).
- **Races:** circuit race (3 laps against 3 drivers), highway sprint
  (against 2 drivers), time trial with your best-lap ghost.
- **Challenge a friend (online ghost racing):** drive one lap, then send
  the link. The friend opens it and races your ghost car. Live racing at the
  same moment needs a game server, so the game uses ghost links.
- **Missions:** taxi driver (3 rides), delivery rush (3 parcels with a
  timer), parking test, driving licence test (+500 points the first time).
- **Real feel:** fuel and petrol pump, crash damage, breakdown and tow
  truck, nitro, handbrake drift, gears and RPM, horn, indicators, night
  with headlights, rain with less grip, 4 camera views, rotating mini map,
  engine and crash sounds, touch buttons on phones.
- **Levels:** points also give XP. Level = floor(sqrt(XP / 120)) + 1.
- **Rishpur village and Sunrise Hill:** a winding village road west of the
  city with huts, fields and haystacks, then a spiral road up a hill with a
  temple, a flag and snowy mountains. Hills slow the car going up.
- **Stunt ramps:** 2 in the park and 1 big one in the village. Real jumps,
  points for air time.
- **Monsoon puddles:** in rain, puddles splash and slide the car.
- **Toll plaza:** on the highway. Stop at the barrier to pay 20 points.
  Races use the FASTag lane.
- **Car wash:** rain and grass make the car dirty; the wash makes it shine.
- **Petrol pump game:** stop the meter between 98% and 100%.
- **Daily gift:** grows with the day streak, up to 600 points on day 7.
- **Number plate and stickers:** your own plate text, 10 stickers.
- **Badges:** 22 badges, +50 points each.
- **About us:** Rishabh's photo, the series, and the game story.

## Controls

W or Up: accelerate. S or Down: brake, then reverse. A, D or arrows: steer.
Space: handbrake. N: nitro. C: camera. H: horn. L: night. R: rain.
Q and E: indicators. Esc: menu.

## Tests

`tests/regress.cjs` runs the full regression in Chromium with Playwright.
It drives the game through its step function, so it does not depend on
the frame rate.

```
# serve a copy whose importmap points at a local three.module.js
NODE_PATH=$(npm root -g) node tests/regress.cjs http://localhost:8765/test.html shots
```

## Versions

- v1: first release.
- v2: the car never gets stuck. Correct start lane, soft bumps with
  damage once per 0.7 s, auto-unstick, free pit crew at every race and
  mission start, a broken car or empty tank crawls at 18 km/h, traffic
  clears at mode start, safer touch buttons and keys. New regression
  checks run 8 modes in a row twice with traffic and real keys.
- v3: ideas 6 to 14: monsoon puddles, toll plaza, petrol pump game,
  daily gift, number plates and stickers, car wash, stunt ramps,
  22 badges, Rishpur village and Sunrise Hill. Grass no longer shows
  through roads on some screens. 102 regression checks.
