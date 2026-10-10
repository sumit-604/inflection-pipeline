# Rish Board Games

RishSchoolDays series, Game 4. Created by Rishabh Sharma, age 9.
Slogan: **Just live it!**

Fifteen board games in one HTML file, for a phone or a computer. Play the
computer, or play with family on one screen. Version label: **Rish Board
Games v3** (bottom right).

## The games

- **Ludo:** 2 to 4 players. Each colour (red, green, yellow, blue) is a
  player, the computer, or off. Roll a 6 to bring a token out. A 6, a cut
  or a token reaching home gives another roll. Three 6s in a row lose the
  turn. The 4 start squares and 4 ★ squares are safe. Home needs the exact
  number. The game goes on until every place (1st to 4th) is decided. The
  computer cuts when it can, goes home, comes out on a 6, looks for safe
  squares and runs from danger.
- **Chess:** every rule: castling, en passant, promotion (you pick the
  piece), check, checkmate, stalemate, the 50-move rule, three times the
  same position, and too few pieces to win. Play the computer (Easy,
  Medium, Hard) as White or Black, or 2 players. 💡 Hint shows a good
  move. Undo, Flip, captured pieces and the move list (e4, Nf3, O-O,
  Qxf7#).
- **Saanp Seedi:** snakes and ladders, 1 to 100, 2 to 4 players. 8
  ladders and 8 snakes. A 6 rolls again. 100 needs the exact number.
- **Checkers:** 8 x 8, 12 pieces each. Jumping is a must, a jump goes on
  while it can, and the far row makes a king. Play the computer (Easy,
  Medium, Hard) or 2 players. Undo.

- **Carrom (v2):** a real carrom board with physics: coins slide, bounce
  and hit each other. Slide the striker along your line, press on it and
  pull back like a slingshot (the arrow and the power show the shot), let
  go. Your coin in = shoot again. The striker in a pocket is a foul: one
  of your coins comes back. The red queen counts only when you cover it
  with one of your coins in the same or the next shot, and the last coin
  needs the queen covered first. The computer plays each shot out in its
  head before it shoots. 2 players: white at the bottom, black at the top.
- **Chaar Line (v2):** connect four. Drop discs; 4 in a line wins. The
  computer blocks and attacks (Easy, Medium, Hard).
- **Reversi (v2):** trap the other colour to flip it; a turn with no
  move is skipped; most discs wins.
- **Kaata Zero (v2):** tic-tac-toe. The Hard computer never loses.
- **Dots and Boxes (v2):** 5 x 5 dots. The 4th side of a box wins it and
  another line. The computer takes free boxes and avoids giving any away.

- **Rish Business (v3):** 2 to 4 players or computers, ₹1,500 each. A
  28-square board of Indian cities in 6 colours (Agra to Mumbai), 3
  railway stations, the Electric Co. and Water Works, Chance and Treasury
  cards, Income and Luxury Tax, Jail and Rest House. Buy what you land
  on, pay rent on others' squares, own a whole colour to double the rent
  and build up to 3 houses. Start pays ₹200; doubles roll again, 3
  doubles go to Jail; pay ₹50 or roll doubles to leave. Short (15
  rounds), normal (25) or no limit: the last player with money, or the
  richest at the end, wins.
- **Navakankari (v3):** India's old game of mills (nine men's morris).
  Place 9 pieces, then move them; 3 in a row takes an enemy piece; 3
  pieces left can fly. The computer looks 1 to 3 moves ahead.
- **Bagh Bakri (v3):** tigers and goats (bagh-chal). 4 tigers jump goats
  to eat them; 20 goats try to trap every tiger. Play either side against
  the computer, or 2 players.
- **Mancala (v3):** sowing seeds round 12 pits, like Pallanguzhi. Last
  seed in your store plays again; an empty pit on your side captures the
  seeds across.
- **Navy Battle (v3):** battleship against the computer: 5 ships each,
  move yours before the first shot. Medium and Hard hunt round a hit.
- **Panch Line (v3):** gomoku on a 15 x 15 board: 5 in a row wins. The
  computer blocks your lines and finishes its own.

## Pictures (v2)

Wooden frames and shaded squares on every board; 3D tokens, dice and
discs; shaded Ludo yards with gold safe stars; coloured, striped snakes
with eyes and wooden ladders; chess pieces with light and dark shading
that phones never turn into emoji; the carrom board drawn at the
screen's full sharpness.

## More

- Your name on the home screen goes into the games.
- Wins and games played for each game, kept on this device.
- Sounds for the dice, moves, cuts, ladders, snakes and wins (🔊 on or off).
- Space or Enter rolls the dice in Ludo and Saanp Seedi.
- Light and dark screens follow the phone or computer setting.

## Tests

`tests/regress.cjs` plays the page in Chromium with Playwright: the home
screen and saving, chess rules against the standard move counts (perft:
start 20/400/8902, Kiwipete 48/2039, and three more positions), tapping
moves, scholar's mate, castling, en passant, pins, stalemate, promotion,
the computer, hints and undo; Ludo rules (coming out, cuts, safe squares,
exact home, three 6s, winning) and a full 4-computer game; Saanp Seedi
ladders, snakes, exact 100 and a full game; Checkers forced jumps, double
jumps, kings, winning, undo and computer games;
the new games (Kaata Zero never loses to 40 random games; Chaar Line
blocking and winning; Reversi flips, passes and full games; Dots and
Boxes boxes and a full game; Carrom rack, pots, fouls, the queen rule,
a win, the sharp board and a full computer game); the v3 games (Panch
Line wins and blocks, Navakankari mills, flying and losing, Bagh Bakri
jumps and traps, Mancala sowing and captures, Navy Battle hits and
hunting, Rish Business buying, rent, houses, Start, Jail, cards,
running out of money and a full computer game); and the phone layout.
35 checks.

    NODE_PATH=$(npm root -g) node tests/regress.cjs index.html
