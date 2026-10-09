# Rish Board Games

RishSchoolDays series, Game 4. Created by Rishabh Sharma, age 9.
Slogan: **Just live it!**

Four board games in one HTML file, for a phone or a computer. Play the
computer, or play with family on one screen. Version label: **Rish Board
Games v1** (bottom right).

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
jumps, kings, winning, undo and computer games; and the phone layout.
21 checks.

    NODE_PATH=$(npm root -g) node tests/regress.cjs index.html
