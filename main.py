from board import Board

def main():
    board = Board()

    while True:
        board.display()

        move = input(
            "\nEnter move (e2 e4) or 'quit': "
        )

        if move.lower() == "quit":
            break

        try:
            start, end = move.split()
            board.move_piece(start, end)

        except ValueError:
            print("Use format: e2 e4")

if __name__ == "__main__":
    main()