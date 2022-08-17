class BowlingGame():
    def __init__(self):
        self.current_score = 0
        self.frame_totals = []
        self.frames_bowled = []
        self.scoreboard = []

    def frame(self, throws):
        """
        Processes the throws into frame data 
        Input: throws - list of pins knocked down in a frame
        Output: Frame dictionary with throw data, result (strike, spare, open),
        bonus (for strike and spare), totals (for score keeping)
        """
        frame = {}

        # Map throws to keys in dictonary
        for i, item in enumerate(throws):
            i += 1
            frame[f'throw {i}'] = item
        # Check for a strike
        if len(throws) == 1 and len(throws[0]) == 10:
            frame['result'] = 'strike'
            frame['bonus'] = 2
            frame['totals'] = [10]
        # Check for a spare
        elif len(throws) == 2:
            frame['totals'] = [len(throws[0]), len(throws[1])]
            if len(throws[0])+len(throws[1]) == 10:
                frame['result'] = 'spare'
                frame['bonus'] = 1
        # Otherwise it's an open frame
        else:
            frame['bonus'] = 0
            frame['result'] = 'open'

        self.frames_bowled.append(frame)
        self.frame_totals.append(frame['totals'])

        return frame

    def update_score(self, cumulative_score):
        """
        Update the current score with running total
        Overwrites the scoreboard with the current tot_score list
        """
        tot_score = []
        for i, item in enumerate(cumulative_score):
            tot_score.append(sum(cumulative_score[:i+1]))
        self.scoreboard = tot_score
        self.current_score = tot_score[-1:]
        return tot_score

    def game(self, frames_bowled):
        """
        Scores a game of bowling given a dictionary of all frames bowled

        """
        cumulative_score = []
        for count, frame in enumerate(frames_bowled):

            this_frame = frames_bowled[count]['totals']
            # define "next frame" and "second next" for bonus calculation
            if count < 9:
                next_frame = frames_bowled[count+1]['totals']
            if count < 8:
                second_next_frame = frames_bowled[count+2]['totals']
            elif count == 8:
                second_next_frame = 9
            # handle exceptions for 10th frame
            elif count == 9 and len(this_frame) == 3:
                pass

            frame_plus_next_ball = sum(this_frame)+next_frame[0]
            if count < 9:
                if frame['bonus'] == 1:
                    frame_score = frame_plus_next_ball

                elif frame['bonus'] == 2:
                    if len(next_frame) == 2:
                        frame_score = frame_plus_next_ball+next_frame[1]
                    elif len(next_frame) == 1:
                        frame_score = frame_plus_next_ball+second_next_frame[0]
                else:
                    frame_score = sum(this_frame)
            elif count == 9:
                frame_score = sum(this_frame)

            cumulative_score.append(frame_score)

        return cumulative_score
