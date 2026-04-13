import pytest
from game import Chessboard, Pawn, Knight, Rook, Bishop, Queen, King


def test_initial_setup():
    board = Chessboard()
    board.setup()

    # Check a few initial positions
    assert isinstance(board.board[0][0], Rook)
    assert board.board[0][0].color == "black"
    assert isinstance(board.board[7][4], King)
    assert board.board[7][4].color == "white"
    assert all(cell is None for row in board.board[2:6] for cell in row)


def test_pawn_first_move():
    board = Chessboard()
    board.setup()

    pawn = board.board[6][0]  # white pawn
    moves = pawn.list_allowed_moves(board)
    # Should allow 1 or 2 steps forward
    assert (0, 5) in moves or (0, 4) in moves


def test_knight_moves():
    board = Chessboard()
    board.setup()

    knight = board.board[7][1]  # white knight
    moves = knight.list_allowed_moves(board)
    # Knight can jump over pieces
    assert (0, 5) in moves or (2, 5) in moves


def test_rook_moves_blocked():
    board = Chessboard()
    board.setup()

    rook = board.board[7][0]  # white rook
    moves = rook.list_allowed_moves(board)
    # Should be blocked by pawns in front
    assert moves == []


def test_bishop_moves():
    board = Chessboard()
    board.setup()

    bishop = board.board[7][2]  # white bishop
    moves = bishop.list_allowed_moves(board)
    # Should have no moves initially
    assert moves == []


def test_queen_moves():
    board = Chessboard()
    board.setup()

    queen = board.board[7][3]  # white queen
    moves = queen.list_allowed_moves(board)
    assert moves == []


def test_king_moves():
    board = Chessboard()
    board.setup()

    king = board.board[7][4]  # white king
    moves = king.list_allowed_moves(board)
    assert moves == []


def test_list_allowed_moves_from_board():
    board = Chessboard()
    board.setup()

    # White pawn at 6,0
    moves = board.list_allowed_moves(0, 6)
    assert (0, 5) in moves
    assert (0, 4) in moves

    # Trying to list moves for black pawn when it's white's turn
    assert board.list_allowed_moves(0, 1) is None


def test_basic_move():
    board = Chessboard()
    board.setup()

    # Move white pawn 6,0 -> 4,0
    board.move(0, 6, 0, 4)
    assert board.board[4][0] is not None
    assert board.board[6][0] is None
    assert board.color == "black"


def test_illegal_move_raises():
    board = Chessboard()
    board.setup()

    # Try to move white pawn when it's white's turn but illegal square
    with pytest.raises(ValueError):
        board.move(0, 6, 0, 3)


def test_capture_and_game_end():
    board = Chessboard()
    board.board = [[None] * 8 for _ in range(8)]

    # Place white queen and black king adjacent
    white_queen = Queen("white", 0, 0)
    black_king = King("black", 1, 0)
    board.board[0][0] = white_queen
    board.board[0][1] = black_king
    board.color = "white"

    result = board.move(0, 0, 1, 0)
    assert result == "WHITE WON"
    assert board.board[0][1] == white_queen
    assert board.board[0][0] is None


def test_pawn_diagonal_capture():
    board = Chessboard()
    board.board = [[None] * 8 for _ in range(8)]

    white_pawn = Pawn("white", 4, 4)
    black_pawn = Pawn("black", 3, 3)
    board.board[4][4] = white_pawn
    board.board[3][3] = black_pawn
    board.color = "white"

    moves = white_pawn.list_allowed_moves(board)
    assert (3, 3) in moves  # diagonal capture
