from collections import Counter

def part_2(data, reverse):
    for x in range(len(data[0])):
        c = list(map(int, list(zip(*data))[x]))
        s = sorted(c, key=lambda y: (c.count(y), y))
        bit = s[0] if reverse else s[-1]
        data = list(filter(lambda n: n[x] == str(bit), data))

        # Different solution, less clean
        # c = Counter(list(zip(*data))[x])
        # s = sorted(c.items(), key=lambda y: (-y[1], -int(y[0])))
        # bit = s[0][0] if reverse else s[-1][0]

    return int(data[0], 2)

def main():
    with open("data.txt", "r") as file:
        data = file.read().splitlines()

    # Part 1
    d = "".join([Counter(x).most_common()[0][0] for x in zip(*data)])
    gamma = int(d, 2)
    eps = int("".join('1' if x == '0' else '0' for x in d), 2)


    print(f"Solution part 1: {gamma * eps}")
    print(f"Solution part 2: Co2: {part_2(data, False)}, Oxy: {part_2(data, True)}")

if __name__ == "__main__":
    main()
