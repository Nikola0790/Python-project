class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def setup(self):
        # Black pieces
        self.board[0] = [
            Rook("black", 0, 0),
            Knight("black", 1, 0),
            Bishop("black", 2, 0),
            Queen("black", 3, 0),
            King("black", 4, 0),
            Bishop("black", 5, 0),
            Knight("black", 6, 0),
            Rook("black", 7, 0),
        ]

        self.board[1] = [Pawn("black", x, 1) for x in range(8)]

        # Empty middle rows
        for y in range(2, 6):
            self.board[y] = [None for _ in range(8)]

        # White pieces
        self.board[6] = [Pawn("white", x, 6) for x in range(8)]
        self.board[7] = [
            Rook("white", 0, 7),
            Knight("white", 1, 7),
            Bishop("white", 2, 7),
            Queen("white", 3, 7),
            King("white", 4, 7),
            Bishop("white", 5, 7),
            Knight("white", 6, 7),
            Rook("white", 7, 7),
        ]

    def list_allowed_moves(self, x, y):
        # 1. Check board boundaries
        if not (0 <= x <= 7 and 0 <= y <= 7):
            return None

        piece = self.board[y][x]

        # 2. No piece on square
        if piece is None:
            return None

        # 3. Wrong player's piece
        if piece.color != self.color:
            return None

        # 4. Ask piece for its moves
        return piece.list_allowed_moves(self)

    def move(self, from_x, from_y, to_x, to_y):
        # 1. Get allowed moves for the selected square
        allowed_moves = self.list_allowed_moves(from_x, from_y)

        # 2. If no piece or wrong player
        if allowed_moves is None:
            raise ValueError("Illegal move")

        # 3. If target square not allowed
        if (to_x, to_y) not in allowed_moves:
            raise ValueError("Illegal move")

        # 4. Get the piece
        piece = self.board[from_y][from_x]

        # 5. Get the piece on destination
        target = self.board[to_y][to_x]

        # 6. Move the piece
        piece.move(to_x, to_y)
        self.board[to_y][to_x] = piece
        self.board[from_y][from_x] = None

        # 7. Check if captured piece was a King
        if target is not None and isinstance(target, King):
            if target.color == "white":
                return "BLACK WON"
            else:
                return "WHITE WON"

        # 8. Switch turn
        self.color = "black" if self.color == "white" else "white"



class Figure:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    # Internal helper for diagonals (Bishop/Queen)
    def _get_diagonal_moves(self, chessboard):
        allowed_moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dx, dy in directions:
            for step in range(1, 8):
                new_x = self.x + dx * step
                new_y = self.y + dy * step

                if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                    break

                target = chessboard.board[new_y][new_x]

                if target is None:
                    allowed_moves.append((new_x, new_y))
                else:
                    if target.color != self.color:
                        allowed_moves.append((new_x, new_y))
                    break  # stop in both cases

        return allowed_moves

    # Internal helper for horizontal & vertical (Rook/Queen)
    def _get_horizontal_and_vertical_moves(self, chessboard):
        allowed_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            for step in range(1, 8):
                new_x = self.x + dx * step
                new_y = self.y + dy * step

                if not (0 <= new_x <= 7 and 0 <= new_y <= 7):
                    break

                target = chessboard.board[new_y][new_x]

                if target is None:
                    allowed_moves.append((new_x, new_y))
                else:
                    if target.color != self.color:
                        allowed_moves.append((new_x, new_y))
                    break  # stop in both cases

        return allowed_moves


class Pawn(Figure):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.has_moved = False

    def list_allowed_moves(self, chessboard):
        allowed_moves = []

        direction = -1 if self.color == "white" else 1

        # One step forward
        one_step_y = self.y + direction

        if 0 <= one_step_y <= 7:
            if chessboard.board[one_step_y][self.x] is None:
                allowed_moves.append((self.x, one_step_y))

                # Two step forward
                two_step_y = self.y + 2 * direction
                if not self.has_moved and 0 <= two_step_y <= 7:
                    if chessboard.board[two_step_y][self.x] is None:
                        allowed_moves.append((self.x, two_step_y))

        # Diagonal captures
        for dx in [-1, 1]:
            new_x = self.x + dx
            new_y = self.y + direction

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                target = chessboard.board[new_y][new_x]
                if target is not None and target.color != self.color:
                    allowed_moves.append((new_x, new_y))

        return allowed_moves

    def move(self, x, y):
        self.x = x
        self.y = y
        self.has_moved = True


class Knight(Figure):
    def list_allowed_moves(self, chessboard):
        allowed_moves = []
        move_offsets = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        for dx, dy in move_offsets:
            new_x = self.x + dx
            new_y = self.y + dy

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                target = chessboard.board[new_y][new_x]

                if target is None or target.color != self.color:
                    allowed_moves.append((new_x, new_y))

        return allowed_moves


class Rook(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_horizontal_and_vertical_moves(chessboard)


class King(Figure):
    def list_allowed_moves(self, chessboard):
        allowed_moves = []
        move_offsets = [
            (1, 0),  # right
            (-1, 0),  # left
            (0, 1),  # up
            (0, -1),  # down
            (1, 1),  # up-right
            (1, -1),  # down-right
            (-1, 1),  # up-left
            (-1, -1),  # down-left
        ]

        for dx, dy in move_offsets:
            new_x = self.x + dx
            new_y = self.y + dy

            if 0 <= new_x <= 7 and 0 <= new_y <= 7:
                target = chessboard.board[new_y][new_x]

                if target is None or target.color != self.color:
                    allowed_moves.append((new_x, new_y))

        return allowed_moves


class Bishop(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_diagonal_moves(chessboard)


class Queen(Figure):
    def list_allowed_moves(self, chessboard):
        return self._get_diagonal_moves(
            chessboard
        ) + self._get_horizontal_and_vertical_moves(chessboard)


def show(chessboard):
    for y in range(7, -1, -1):  # print from top (row 7) to bottom (row 0)
        row_str = ""
        for x in range(8):
            piece = chessboard.board[y][x]
            if piece is None:
                row_str += ". "  # empty square
            else:
                # Represent each piece by its first letter
                letter = piece.__class__.__name__[0]  # P, K, R, B, Q, etc.
                if piece.color == "black":
                    letter = letter.lower()  # lowercase for black pieces
                row_str += letter + " "
        print(row_str)
    print()  # extra line after the board


chessboard = Chessboard()
chessboard.setup()

show(chessboard)

chessboard.move(4, 6, 4, 4)  # white pawn forward 2
show(chessboard)

print(chessboard.color)  # should now be "black"
