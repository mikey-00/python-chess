class MoveValidator:

    @staticmethod
    def is_valid_pawn_move(piece, sr, sc, er, ec):
        # White pawn
        if piece == "P":

            # One step forward
            if sc == ec and er == sr - 1:
                return True

            # Two steps from starting position
            if sr == 6 and sc == ec and er == sr - 2:
                return True

        # Black pawn
        elif piece == "p":

            if sc == ec and er == sr + 1:
                return True

            if sr == 1 and sc == ec and er == sr + 2:
                return True

        return False