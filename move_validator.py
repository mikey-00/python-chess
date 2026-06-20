class MoveValidator:

    @staticmethod
    def is_valid_pawn_move(piece, sr, sc, er, ec, board):

        # White pawn
        if piece == "P":

            # One square forward
            if sc == ec and er == sr - 1:
                return board[er][ec] == "."

            # Two squares from starting position
            if sr == 6 and sc == ec and er == sr - 2:
                return (
                    board[sr - 1][sc] == "."
                    and board[er][ec] == "."
                )

            # Capture
            if er == sr - 1 and abs(ec - sc) == 1:
                return board[er][ec].islower()

        # Black pawn
        elif piece == "p":

            # One square forward
            if sc == ec and er == sr + 1:
                return board[er][ec] == "."

            # Two squares from start
            if sr == 1 and sc == ec and er == sr + 2:
                return (
                    board[sr + 1][sc] == "."
                    and board[er][ec] == "."
                )

            # Capture
            if er == sr + 1 and abs(ec - sc) == 1:
                return board[er][ec].isupper()

        return False