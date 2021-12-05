def bingo_check(board):
    if not all([any(row) for row in board]):
        return True
    elif not all([any([row[i] for row in board]) for i in range(len(board))]):
        return True
    else:
        return False

def board_score(board, num):
    s = sum([int(num) for row in board for num in row if num != False])
    return num * s

def part_1(moves, boards):
    for num in moves:
        for index, board in enumerate(boards):
            boards[index] = [[False if num == int(number) else number 
                            for number in row] 
                            for row in board]
            if bingo_check(boards[index]):
                return board_score(boards[index], num)

def part_2(moves, boards):
    for num in moves:
        winners = []
        for index, board in enumerate(boards):
            boards[index] = [[False if num == int(number) else number for number in row] for row in board]
            if bingo_check(boards[index]):
                if len(boards) == 1:
                    return board_score(boards[index], num)
                winners.append(index)
        for winner in winners[::-1]:
            boards.pop(winner)

               
def main():
    with open("data.txt", "r") as file:
        data = file.read().strip().split("\n\n")

    moves = [int(x) for x in data.pop(0).split(",")]
    boards = [[y.split() for y in x.split("\n")] for x in data]
    print(f"Solution part 1: {part_1(moves, boards)}")
    print(f"Solution part 2: {part_2(moves, boards)}")

if __name__ == "__main__":
    main()