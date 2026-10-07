# Rish Hero

RishSchoolDays series, Game 3. Created by Rishabh Sharma, age 9.
Slogan: **Just live it!**

A 3D action story game in one HTML file (Three.js). It runs on a computer
and on a phone. Version label: **Rish Hero v3** (bottom right).

## The story

Same school, classmates and teachers as RishSchoolDays Game 1: Sunrise
Public School, Suryanagar. Aarav, Diya, Kabir, Meher, Rohan, Sana.
Mrs. Anjali Rao, Mr. Iyer, Ms. D'Souza, Mr. Khan, Computer Sir Arjun,
Coach Vikram, Principal Mrs. Verma.

- **Prologue, One Year Alone:** Rish joins the school in April. His father,
  Major Rajveer Sharma, is away on an army posting. Rish walks through 7
  months of his year. Kabir throws his tiffin away. Coach Vikram benches
  him and Kabir pushes him down. Mr. Iyer blames him for a beaker that
  Rohan broke. Kabir and Rohan trip him; Sana walks away; Ms. D'Souza tells
  him to stop crying. Nobody takes his birthday sweets, only Diya. On
  Annual Day, one year later, Kabir and Rohan lock him in the storeroom.
- **Chapter 1, Locked In (no gun):** a bomb blows the school gate. Kick the
  door open (quick move), sneak past guards, take them down from behind.
  The phone is dead. A guard's radio: bombs in the lab, hostages in the hall.
- **Chapter 2, The Science Lab (no gun):** fight 5 men by hand. The captain
  drops the bomb manual. Defuse 2 bombs: read the manual, cut the right
  wire. A wrong wire or the timer = BOOM. Mr. Iyer says sorry.
- **Chapter 3, Hostages in the Hall (no gun):** 6 armed men. Rish uses
  stealth and the room: throw a duster at a hanging light, a book at a fire
  extinguisher, kick a glass case. Save Kabir (quick move). Untie 9
  classmates and teachers. Coach Vikram says sorry. Kade takes the
  Principal and Diya.
- **Chapter 4, Rooftop (no gun):** run and jump 4 m gaps, slide under a
  low pipe, beat Bull: dodge his charge so he hits the wall, break his
  grab, finish him.
- **Chapter 5, Chase:** a bicycle chase after Kade's van, 1.4 km through
  the Suryanagar market. Change lanes, hop crates, use ramps. The van stops
  at a railway crossing.
- **Chapter 6, Railway Yard (the only gun chapter):** a pistol, and a
  machine gun from a guard. Shots change the yard: red barrels explode,
  steam valves spray, the crane container falls, crates break, bullet holes
  stay. Kade fights with a gun, then kicks the gun away: hand to hand. Then
  the abort code: 4 riddles, one digit each, 3 tries.
- **Ending:** the news, the Sunrise Gold Medal, every teacher and bully
  says sorry, everyone becomes his friend, and Dad comes home.

The Black Viper gang and every person are made up. Defeated enemies are
knocked out and arrested. No blood.

## Moves

- Move: W A S D, or arrows (up and down walk, left and right turn). Drag
  to look around. Phone: the stick.
- Shift run · Space jump · C crouch (sneak), or slide while running
- J punch (3 in a row = uppercut) · K kick (breaks guards and crates) ·
  L block (block just as he swings = COUNTER) · Q dodge roll
- E: takedown from behind, untie, pick up, use · F: throw a book, duster or
  brick (at an enemy, or at a light or extinguisher near him)
- Chapter 6 only: F or click shoots (hold F for the machine gun), R reload,
  X switch guns. The red laser shows the target; a gold ring means the room
  can do the work.
- **Finding the way:** a gold arrow at Rish's feet points the way to the
  next gold marker, through the doors. The school has a MAIN ENTRANCE from
  the campus and a SIDE DOOR on the left.
- **Skip:** tap ⏭ Skip twice to skip a hard part (fight, bomb, code,
  chase). Talks have their own Skip. The fail screen has "Skip this part".
  The pause menu has "Skip this chapter".

## Tests

`tests/regress.cjs` plays the whole game in Chromium with Playwright
(swiftshader WebGL): real walking, stealth, fights, quick moves, bombs,
parkour, the chase, guns and the code, doors, the guide arrow and the E prompts, plus phone controls. 65 checks.

    NODE_PATH=$(npm root -g) node tests/regress.cjs index.html shots [three.module.js]

The optional third argument serves Three.js 0.160 from a local file
instead of the CDN.
