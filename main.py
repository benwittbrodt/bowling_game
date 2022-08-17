from bowl import BowlingGame
from ref import *

t = BowlingGame()

# for item in throws:
#     t.frame(item)


cumulative_score = t.game(frames_bowled)

score = t.update_score(cumulative_score)

print(score)
