import random
import curses as CURSES

SS = CURSES.initscr()
CURSES.curs_set(0)
SH, SW = SS.getmaxyx()
WW = CURSES.newwin(SH, SW, 0, 0)
WW.keypad(1)
WW.timeout(100)

SNK_X = SW/4
SNK_Y = SH/2
SNAKE = [
  [SNK_Y, SNK_X],
  [SNK_Y, SNK_X-1],
  [SNK_Y, SNK_X-2]
]

FOOD = [SH/2, SW/2]
WW.addch(int(FOOD[0]), int(FOOD[1]), CURSES.ACS_PI)

KEY = CURSES.KEY_RIGHT

while True:
  NEXT_KEY = WW.getch()
  KEY = KEY if NEXT_KEY == -1 else NEXT_KEY

  if SNAKE[0][0] in [0, SH] or SNAKE[0][1]  in [0, SW] or SNAKE[0] in SNAKE[1:]:
    CURSES.endwin()
    quit()

  NEW_HEAD = [SNAKE[0][0], SNAKE[0][1]]

  if KEY == CURSES.KEY_DOWN:
    NEW_HEAD[0] += 1
  if KEY == CURSES.KEY_UP:
    NEW_HEAD[0] -= 1
  if KEY == CURSES.KEY_LEFT:
    NEW_HEAD[1] -= 1
  if KEY == CURSES.KEY_RIGHT:
    NEW_HEAD[1] += 1

  SNAKE.insert(0, NEW_HEAD)

  if SNAKE[0] == FOOD:
    FOOD = None
    while FOOD is None:
      NF = [
        random.randint(1, SH-1),
        random.randint(1, SW-1)
      ]
      FOOD = NF if NF not in SNAKE else None
    WW.addch(FOOD[0], FOOD[1], CURSES.ACS_PI)
  else:
    TAIL = SNAKE.pop()
    WW.addch(int(TAIL[0]), int(TAIL[1]), ' ')

  WW.addch(int(SNAKE[0][0]), int(SNAKE[0][1]), CURSES.ACS_CKBOARD)
