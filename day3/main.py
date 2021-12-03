from collections import Counter

def part_2(data, reverse):
    for x in range(len(data[0])):
        c = sorted(Counter(list(zip(*data))[x]).items(), key=lambda y: (-y[1], -int(y[0])))
        bit = c[0][0] if reverse else c[-1][0]
        data = list(filter(lambda n: n[x] == bit, data))
    return int(data[0], 2)

def main():
    with open("data.txt", "r") as file:
        data = file.read().splitlines()

    d = "".join([Counter(x).most_common()[0][0] for x in zip(*data)])
    gamma = int(d, 2)
    eps = int("".join('1' if x == '0' else '0' for x in d), 2)


    print(f"Solution part 1: {gamma * eps}")
    print(f"Solution part 2: {part_2(data, False) * part_2(data, True)}")

if __name__ == "__main__":
    main()