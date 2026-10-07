# Rish Hero

RishSchoolDays series, Game 3. Created by Rishabh Sharma, age 9.
Slogan: **Just live it!**

A top-down action hero game in one HTML file. No libraries, no downloads.
It runs on a computer and on a phone.

## The story

- **Prologue, The New Kid:** Rish is the new boy at Sunrise Public School.
  His father, army commando Major Arjun Sharma, went missing on a secret
  mission a year ago. Nobody in class wants to be Rish's friend.
- **Chapter 1, Blast at Assembly:** a bomb blows the school gate open.
  Viktor Kade and his Black Viper gang take the school to get the codes
  for SKYFALL, a satellite weapon. Rish fights back, picks up a gun and
  frees his classmates, even Bunty, who bullied him.
- **Chapter 2, Bombs in the Building:** defuse 4 bombs before the timer ends.
- **Chapter 3, Rooftop Showdown:** boss fight with Bruno "The Bull" Kassar.
  The police arrive. Kade is going to Black Rock Island.
- **Chapter 4, City Under Fire:** gunmen, drones and a sniper attack the
  city. Rescue the people and reach the harbour.
- **Chapter 5, Black Rock Island:** lasers, turrets, shield troopers and
  3 keycards. Rish finds his father, alive, in the prison block.
- **Chapter 6, Skyfall:** final boss Viktor Kade in a battle suit with a
  minigun, rockets, drones and an energy shield. Enter the code to stop
  the launch.
- **Ending:** the world news calls Rish a hero, the school gives him the
  Golden Hero Medal, Bunty says sorry, and everyone wants to be his friend.

The Black Viper gang and all the people are made up. Defeated enemies are
knocked down and arrested; the game has no blood.

## Moves and weapons

- Move: W A S D or the arrows. Phone: the stick.
- Guns: pistol, SMG, shotgun, assault rifle. Walk near a gun and Rish picks
  it up. Shoot: mouse or Space (hold). Aim: the mouse, or Rish aims at the
  nearest enemy he can see. R reload, Q or 1 to 4 switch, ammo boxes refill.
- Fight: J punch (3 punches = uppercut that dazes), K kick (knocks shields
  away), L or Shift roll (bullets miss), G grenade, F focus (slow motion).
- E: talk, free hostages, defuse bombs, and TAKEDOWN a dazed or unaware enemy.
- Enemies: thugs, riflemen, heavies, grenadiers, shield troopers, snipers
  with a red laser, drones, turrets, and two bosses.
- Training: spend stars on health, armor, fighting, shooting, speed,
  grenades and focus. Settings: Easy, Normal or Hard.

## Tests

`tests/regress.cjs` plays every chapter in Chromium with Playwright,
through the game's step function, so it does not depend on the frame rate.

```
# serve the folder with the game, then:
NODE_PATH=$(npm root -g) node tests/regress.cjs http://localhost:8766/index.html shots
```

## Versions

- v1: first release. 7 chapters, 4 guns, 6 moves, 10 enemy types, 2 bosses,
  training, phone controls. 30 regression checks.
