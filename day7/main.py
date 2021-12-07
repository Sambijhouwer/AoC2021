from math import ceil, floor
from statistics import median, mean

def main():
    with open("data.txt", "r") as file:
        data = [int(x) for x in file.readline().split(",")]

    # Brute Force
    fuel = lambda x: x * (x + 1) / 2
    # win1 = min([sum([abs(y - x) for y in data]) for x in range(max(data))])
    # win2 = min([sum([fuel(abs(y - x)) for y in data]) for x in range(max(data))])

    # Trying to be clever
    m = median(data)
    a = mean(data)
    win1 = sum([abs(x - m) for x in data])
    win2 = min([sum([fuel(abs(y - x)) for y in data]) for x in [ceil(a), floor(a)]])

    print(f"Solution part 1: {win1}")
    print(f"Solution part 1: {win2}")


if __name__ == "__main__":
    main()