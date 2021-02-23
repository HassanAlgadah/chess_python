import chessEngine
import pygame
import random

# engine = chessEngine.ChessEngine()

# engine.control('P64 44')
width, height = 800, 800
win = pygame.display.set_mode((width, height))
IMAGES = {}
SQ_SIZE = 800 // 8


def draw(board, playerclick):
    # win.fill((0, 0, 0), (sqr.x, sqr.y))
    # win.fill((230, 12, 44))
    drawBoard()
    drawPieces(board)

    if len(playerclick)>0:
        s = pygame.Surface((SQ_SIZE, SQ_SIZE))  # the size of your rect
        s.set_alpha(128)  # alpha level
        s.fill(pygame.Color('red'))  # this fills the entire surface
        win.blit(s, (playerclick[0][1] *SQ_SIZE,playerclick[0][0]*SQ_SIZE))
    pygame.display.update()


def drawBoard():

    colors = [pygame.Color('gray'), pygame.Color('dark green')]
    for r in range(8):
        for c in range(8):
            color = colors[((r + c) % 2)]
            pygame.draw.rect(win, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(board):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != '--':
                win.blit(IMAGES[piece], pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bP', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("chessPics/" + piece + ".png"), (800 // 8, 800 // 8))


def main():
    run = True
    clock = pygame.time.Clock()
    loadImages()
    engine = chessEngine.ChessEngine()
    sqr = ()
    playerclick = []

    while run:
        # loop for only 60 times per second
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sqr == (row,col):
                    sqr = ()
                    playerclick = []
                else:
                    sqr = (row, col)
                    playerclick.append(sqr)
                if len(playerclick) == 2:
                    piece = engine.board[playerclick[0][0]][playerclick[0][1]]
                    val = piece[1]+str(playerclick[0][0])+str(playerclick[0][1])+" "+str(playerclick[1][0])+str(playerclick[1][1])
                    engine.control(val)
                    # print(val)
                    playerclick = []

        draw(engine.board,playerclick)

    pygame.quit()


if __name__ == "__main__":
    main()

# engine.print_board()
# while True:
#     val = input("Enter your move: ")
#     engine.control(val)
