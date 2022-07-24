from bowl import *

throws = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
          [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10]]]


t = BowlingGame()

for item in throws:
    t.frame(item)

print(t.frame_totals)
