import chessEngine


engine = chessEngine.chessEngine()


# engine.control('P60 40')
# engine.control('P11 31')
# engine.control('P40 31')
# engine.control('N01 22')
# engine.control('P36 26')
# engine.control('R70 10')
# engine.control('B02 20')
# engine.control('R10 00')
# engine.control('Q03 01')
# engine.control('P61 51')
# engine.control('B20 31')
# engine.control('P66 56')
# engine.control('P16 36')
# engine.control('R00 01')
engine.control('P63 43')
engine.control('P12 32')
engine.control('P43 32')
engine.control('P13 33')
engine.control('Q73 33')
engine.control('P15 25')
engine.control('P64 54')
engine.control('Q03 30')
engine.control('P62 52')
engine.control('P16 36')
engine.control('B75 64')
engine.control('P10 20')
engine.control('B64 37')



engine.print_board()
while True:
    val = input("Enter your move: ")
    engine.control(val)



