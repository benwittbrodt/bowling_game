
class BowlingGame():
    def __init__(self):
        self.current_score = 0
        self.frame_totals = []
        self.frames_bowled = []

    def frame(self, throws):
        frame = {}
        # Map throws to keys in dictonary
        i = 1
        for item in throws:
            frame[f'throw {i}'] = item
            i += 1

        if len(throws) == 1 and len(throws[0] == 10):
            frame['is_strike'] = 1
            frame['bonus'] = 2
            frame['totals'] = [10]
        elif len(throws) == 2:
            frame['totals'] = [len(throws[0]), len(throws[1])]
            if len(throws[0])+len(throws[1]) == 10:
                frame['is_spare'] = 1
                frame['bonus'] = 1
        self.frames_bowled.append(frame)
        self.frame_totals.append(frame['totals'])
        return frame

    def game():
        pass
