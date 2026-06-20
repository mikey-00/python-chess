from move_validator import MoveValidator

class Board:
    def __init__(self):
        self.current_turn = "white"

        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def display(self):
        print(f"\nCurrent Turn: {self.current_turn.capitalize()}")
        
        print("\n  a b c d e f g h")

        for i in range(8):
            print(8 - i, end=" ")

            for piece in self.board[i]:
                print(piece, end=" ")

            print()

    def position_to_index(self, pos):
        col = ord(pos[0].lower()) - ord('a')
        row = 8 - int(pos[1])

        return row, col

    def move_piece(self, start, end):
        sr, sc = self.position_to_index(start)
        er, ec = self.position_to_index(end)

        piece = self.board[sr][sc]

        # White's turn
        if self.current_turn == "white" and not piece.isupper():
            print("It's White's turn.")
            return

        # Black's turn
        if self.current_turn == "black" and not piece.islower():
            print("It's Black's turn.")
            return

        if piece == ".":
            print("No piece at starting position.")
            return

        # Validate pawns
        if piece in ["P", "p"]:
            if not MoveValidator.is_valid_pawn_move(
                    piece, sr, sc, er, ec):
                print("Illegal pawn move.")
                return

        self.board[er][ec] = piece
        self.board[sr][sc] = "."

        if self.current_turn == "white":
            self.current_turn = "black"
        else:
            self.current_turn = "white"