class Board:
    def __init__(self):
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

        if piece == ".":
            print("No piece at starting position.")
            return

        self.board[er][ec] = piece
        self.board[sr][sc] = "."