from collections import defaultdict
def mark_tiles(data, diagonal):
    grid = defaultdict(int)
    for p1, p2 in data:
        x1, y1 = p1
        x2, y2 = p2

        x_low, dx = min(x1, x2), abs(x1 - x2)
        y_low, dy = min(y1, y2), abs(y1 - y2)

        if x1 == x2:
            for i in range(dy + 1):
                grid[x1, y_low + i] += 1
        
        elif y1 == y2:
            for i in range(dx + 1):
                grid[x_low + i, y1] += 1

        elif diagonal:
            x_val = 1 if x2 > x1 else -1
            y_val = 1 if y2 > y1 else -1
            for i in range(dx + 1):
                grid[i * x_val + x1, i * y_val + y1] += 1
                
    return sum([1 if x > 1 else 0 for x in grid.values()])

def main():
    with open("data.txt", "r") as file:
        data = file.read().splitlines()

    v = [[[int(y) for y in x.split(",")]for x in line.split(" -> ")] for line in data]

    print(f"Solution part 1: {mark_tiles(v, False)}")
    print(f"Solution part 1: {mark_tiles(v, True)}")


if __name__ == "__main__":
    main()