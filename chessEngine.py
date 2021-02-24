import copy


class ChessEngine:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.moves = 0
        self.white_turn = True
        self.mypiece = 'w'
        self.ischeck = False
        self.checker = None
        self.wattacks = None
        self.battacks = None

    def king(self, row, col, inrow, incol):
        board = self.board

        # castling white hard coded :

        if self.white_turn:
            if (incol == 6 or incol == 2) and inrow == 7 and row == 7 and col == 4:
                if board[7][7] == 'wR' or board[7][0] == 'wR':
                    if incol == 6:
                        for sq in range(col + 1, incol + 1):
                            if board[7][sq] != '--':
                                return print("you cant castle with a piece between")
                        self.make_move(row, col, inrow, incol)
                        board[7][7] = '--'
                        board[7][5] = 'wR'
                        return
                    else:
                        for sq in range(1, col):
                            if board[7][sq] != '--':
                                return print("you cant castle with a piece between")
                        self.make_move(row, col, inrow, incol)
                        board[7][0] = '--'
                        board[7][3] = 'wR'
                        return
                else:
                    return print('theres no Rock')
        else:
            if (incol == 6 or incol == 2) and inrow == 0 and row == 0 and col == 4:
                if board[0][7] == 'wR' or board[0][0] == 'bR':
                    if incol == 6:
                        for sq in range(col + 1, incol + 1):
                            if board[0][sq] != '--':
                                return print("you cant castle with a piece between")
                        self.make_move(row, col, inrow, incol)
                        board[0][7] = '--'
                        board[0][5] = 'wR'
                        return
                    else:
                        for sq in range(1, col):
                            if board[0][sq] != '--':
                                return print("you cant castle with a piece between")
                        self.make_move(row, col, inrow, incol)
                        board[0][0] = '--'
                        board[0][3] = 'wR'
                        return
                else:
                    return print('theres no Rock')

        if (inrow == row + 1 or inrow == row - 1 or inrow == row) and (
                incol == col - 1 or incol == col + 1 or incol == col) and (board[inrow][incol][0] != self.mypiece):
            self.make_move(row, col, inrow, incol)
        else:
            return print('wrong move buddy2')

    def rock(self, row, col, inrow, incol):
        board = self.board
        if self.val_rock(board, row, col, inrow, incol) and self.board[inrow][incol][0] != self.mypiece:
            self.make_move(row, col, inrow, incol)

    def bishop(self, row, col, inrow, incol):
        board = self.board

        if self.val_bishop(board, row, col, inrow, incol) and board[inrow][incol][0] != self.mypiece:
            self.make_move(row, col, inrow, incol)
        else:
            return print('wrong move buddy')

    def queen(self, row, col, inrow, incol):
        board = self.board

        if board[inrow][incol][0] != self.mypiece:
            if self.val_bishop(board, row, col, inrow, incol) or self.val_rock(board, row, col, inrow, incol):
                self.make_move(row, col, inrow, incol)
        else:
            return print('wrong move buddy')

    def knight(self, row, col, inrow, incol):
        board = self.board

        if ((inrow == row + 1 or inrow == row - 1) and (incol == col + 2 or incol == col - 2)) or (
                (inrow == row + 2 or inrow == row - 2)
                and (incol == col + 1 or incol == col - 1)) and (board[inrow][incol][0] != self.mypiece):
            self.make_move(row, col, inrow, incol)
        else:
            return print('wrong move buddy222')

    # pawn goes anyware if theres a piece in top left or top right
    def pawn(self, row, col, inrow, incol):
        board = self.board
        onemove = -1
        twomove = -2
        if self.white_turn:
            onemove = 1
            twomove = 2
        if row != 6 and row != 1:
            twomove = 0
        # taking pieces diagonally
        try:
            if ((board[row - onemove][col + onemove] != '--' and incol == col + onemove) or (
                    board[row - onemove][col - onemove] != '--' and incol == col - onemove)) and (row-onemove == inrow):
                return self.make_move(row, col, inrow, incol)
        except IndexError:
            if col == 7:
                if board[row - onemove][col - onemove] != '--' and incol == col - onemove:
                    return self.make_move(row, col, inrow, incol)
            elif col == 0:
                if board[row - onemove][col + onemove] != '--' and incol == col + onemove:
                    return self.make_move(row, col, inrow, incol)

        if (inrow == row - onemove or inrow == row - twomove) and (incol == col) and (
                board[inrow][incol][0] != self.mypiece):
            if board[inrow][incol] != '--':
                return print('you cant eat like that ')
            self.make_move(row, col, inrow, incol)
        else:
            return print('wrong move buddy')

    def control(self, name):
        piece = name[0]
        row = int(name[1])
        col = int(name[2])
        inrow = int(name[4])
        incol = int(name[5])
        try:
            if self.board[row][col][1] != piece:
                return print('wrong move buddy')
            if self.board[inrow][incol][0] == self.mypiece:
                return print('you cant eat your own pieces')
            if self.board[row][col][0] != self.mypiece:
                return print('this is not your turn')

            if piece == 'R':
                self.rock(row, col, inrow, incol)
            elif piece == 'N':
                self.knight(row, col, inrow, incol)
            elif piece == 'B':
                self.bishop(row, col, inrow, incol)
            elif piece == 'Q':
                self.queen(row, col, inrow, incol)
            elif piece == 'K':
                self.king(row, col, inrow, incol)
            elif piece == 'P':
                self.pawn(row, col, inrow, incol)
        except IndexError:
            print("you can't go their buddy")
        self.print_board()

    def val_bishop(self, board, row, col, inrow, incol):
        valdrow = row
        valdcol = col

        if (inrow != row and incol != col) and (abs(inrow - row) == abs(incol - col)):
            if inrow < row:
                if incol < col:
                    for i in range((row - inrow) - 1):
                        valdrow -= 1
                        valdcol -= 1
                        if board[valdrow][valdcol] != '--':
                            return False
                elif incol > col:
                    for i in range((row - inrow) - 1):
                        valdrow -= 1
                        valdcol += 1
                        if board[valdrow][valdcol] != '--':
                            return False
            elif inrow > row:
                if incol < col:
                    for i in range((inrow - row) - 1):
                        valdrow += 1
                        valdcol -= 1
                        if board[valdrow][valdcol] != '--':
                            return False
                elif incol > col:
                    for i in range((inrow - row) - 1):
                        valdrow += 1
                        valdcol += 1
                        if board[valdrow][valdcol] != '--':
                            return False
            return True
        else:
            return False

    def val_rock(self, board, row, col, inrow, incol):
        valdrow = row
        valdcol = col

        if inrow == row or incol == col:
            if incol == col:
                for i in range(abs(row - inrow) - 1):
                    if row - inrow < 0:
                        valdrow += 1
                    else:
                        valdrow -= 1
                    if board[valdrow][col] != '--':
                        return False
            elif row == inrow:
                for i in range(abs(col - incol) - 1):
                    if col - incol < 0:
                        valdcol += 1
                    else:
                        valdcol -= 1
                    if board[row][valdcol] != '--':
                        return False
            return True
        else:
            return False

    def make_move(self, row, col, inrow, incol):
        # check if the move is legal when the player is in check
        if self.ischeck:
            copybord = copy.deepcopy(self.board)
            piece = copybord[row][col]
            copybord[row][col] = '--'
            copybord[inrow][incol] = piece
            self.allattacks(copybord, not self.white_turn)
            self.check_for_checksv2(copybord)
            if self.ischeck:
                return print('you are in check you cant make this move stupid')
        # make the move
        self.moves += 1
        board = self.board
        piece = board[row][col]
        board[row][col] = '--'
        board[inrow][incol] = piece
        # check if the move is a check
        self.allattacks(board, self.white_turn)
        self.white_turn = False if self.white_turn else True
        self.mypiece = 'w' if self.white_turn else 'b'
        # print(self.wattacks)
        # self.check_for_checks(self.board, piece, inrow, incol, True)
        self.check_for_checksv2(self.board)
        if self.ischeck:
            print('this is a CHECK !!!!!')
            if self.ischeck_matev2(board, self.white_turn): return print('checkMate')

    def check_for_checksv2(self, board):
        for row in range(8):
            for col in range(8):
                sqr = board[row][col]
                if sqr[0] == self.mypiece and sqr[1] == 'K':
                    checksqer = (row, col)
                    if checksqer in self.wattacks:
                        self.ischeck = True
                        return
        self.ischeck = False

    def ischeck_matev2(self, board, white):
        for row in range(8):
            for col in range(8):
                if board[row][col] == "--":
                    continue
                piece = board[row][col]
                for rowa in range(8):
                    for cola in range(8):
                        if board[rowa][cola][0] == board[row][col][0]:
                            continue
                        if piece[0] == 'b' and white:
                            continue
                        elif piece[0] == 'w' and not white:
                            continue
                        if row == rowa and col == cola:
                            continue
                        if piece[1] == 'K':
                            if (rowa == row + 1 or rowa == row - 1 or rowa == row) and (
                                    cola == col - 1 or cola == col + 1 or cola == col) and (
                                    board[rowa][cola][0] != board[row][col][0]):
                                if not self.checkmate_short(row, col, rowa, cola, white):
                                    return False
                        if piece[1] == 'R':
                            if self.val_rock(board, row, col, rowa, cola):
                                if not self.checkmate_short(row, col, rowa, cola, white):
                                    return False

                        elif piece[1] == 'B':
                            if self.val_bishop(board, row, col, rowa, cola):
                                if not self.checkmate_short(row, col, rowa, cola, white):
                                    return False

                        elif piece[1] == 'Q':
                            if self.val_bishop(board, row, col, rowa, cola) or self.val_rock(board, row, col, rowa,
                                                                                             cola):
                                if board[row][col][0] == board[rowa][cola][0]:
                                    continue
                                if not self.checkmate_short(row, col, rowa, cola, white):
                                    return False

                        elif piece[1] == 'N':
                            if ((row == rowa + 1 or row == rowa - 1) and (
                                    col == cola + 2 or col == cola - 2)) or (
                                    (row == rowa + 2 or row == rowa - 2)
                                    and (col == cola + 1 or col == cola - 1)):
                                if not self.checkmate_short(row, col, rowa, cola, white):
                                    return False

                        elif piece[1] == 'P':
                            if not white:
                                if (row + 1 == rowa and col + 1 == cola) or (
                                        row + 1 == rowa and col - 1 == cola):
                                    try:
                                        if board[rowa + 1][cola + 1] != '--' and board[rowa + 1][cola - 1] != '--':
                                            if not self.checkmate_short(row, col, rowa, cola, white):
                                                return False
                                    except:
                                        pass
                            else:
                                if (row - 1 == rowa and col + 1 == cola) or (
                                        row - 1 == rowa and col - 1 == cola):
                                    try:
                                        if board[rowa - 1][cola - 1] != '--' and board[rowa - 1][cola + 1] != '--':
                                            if not self.checkmate_short(row, col, rowa, cola, white):
                                                return False
                                    except:
                                        pass
        return True

    def checkmate_short(self, row, col, rowa, cola, white):
        copybord = copy.deepcopy(self.board)
        piece1 = copybord[row][col]
        copybord[row][col] = '--'
        copybord[rowa][cola] = piece1
        self.allattacks(copybord, not white)
        # print('attacked: ', self.wattacks)
        print(rowa, cola, piece1)
        # print(copybord)
        self.check_for_checksv2(copybord)
        if not self.ischeck:
            # maybe wrong check it if something went wrong
            self.ischeck = True
            return False
        return True

    def allattacks(self, board, white):
        self.wattacks = []
        for row in range(8):
            for col in range(8):
                if board[row][col] == "--":
                    continue
                piece = board[row][col]
                for rowa in range(8):
                    for cola in range(8):
                        if board[row][col][0] == 'b' and white:
                            continue
                        elif board[row][col][0] == 'w' and not white:
                            continue
                        if row == rowa and col == cola:
                            continue
                        if board[rowa][cola][0] == board[row][col][0]:
                            continue
                        if piece[1] == 'R':
                            if self.val_rock(board, row, col, rowa, cola):
                                if board[row][col][0] is not board[rowa][cola][0]: self.wattacks.append(
                                    (rowa, cola))

                        elif piece[1] == 'B':
                            if self.val_bishop(board, row, col, rowa, cola):
                                if board[row][col][0] is not board[rowa][cola][0]: self.wattacks.append(
                                    (rowa, cola))

                        elif piece[1] == 'Q':
                            if self.val_bishop(board, row, col, rowa, cola) or self.val_rock(board, row, col, rowa,
                                                                                             cola):
                                if board[row][col][0] == board[rowa][cola][0]:
                                    continue
                                if board[row][col][0] is not board[rowa][cola][0]: self.wattacks.append(
                                    (rowa, cola))

                        elif piece[1] == 'N':
                            if ((row == rowa + 1 or row == rowa - 1) and (
                                    col == cola + 2 or col == cola - 2)) or (
                                    (row == rowa + 2 or row == rowa - 2)
                                    and (col == cola + 1 or col == cola - 1)):
                                if board[row][col][0] is not board[rowa][cola][0]: self.wattacks.append(
                                    (rowa, cola))

                        elif piece[1] == 'P':
                            if white:
                                if (rowa + 1 == row and cola + 1 == col) or (
                                        rowa + 1 == row and cola - 1 == col):
                                    if board[row][col][0] is not board[rowa][cola][0]:
                                        try:
                                            if board[rowa+1][cola+1] != '--' and board[rowa+1][cola-1] != '--':
                                                self.wattacks.append((rowa, cola))
                                        except:
                                            pass
                            else:
                                if (row - 1 == rowa and col + 1 == cola) or (
                                        row - 1 == rowa and col - 1 == cola):
                                    if board[row][col][0] is not board[rowa][cola][0]:
                                        try:
                                            if board[rowa-1][cola-1] != '--' and board[rowa-1][cola+1] != '--':
                                                self.wattacks.append((rowa, cola))
                                        except:
                                            pass

    def print_board(self):
        for k, b in enumerate(self.board):
            print(k, b)
        print("   ", 0, "   ", 1, "   ", 2, "   ", 3, "   ", 4, "   ", 5, "   ", 6, "   ", 7)
        print('---------------------------------------------------')
        print("white's move") if self.white_turn else print("black's move")
