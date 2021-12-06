def count_fish(data, days):
    counter = {x:0 for x in range(9)}
    for x in data:
        counter[x] += 1

    for _ in range(days):
        newborn = counter[0]
        for i in range(8):
            counter[i] = counter[i + 1]

        counter[8] = newborn
        counter[6] += newborn

    return sum(counter.values())


def main():
    with open("data.txt", "r") as file:
        data = [int(x) for x in file.readline().split(",")]

    print(f"Solution part 1: {count_fish(data, 80)}")
    print(f"Solution part 1: {count_fish(data, 256)}")


if __name__ == "__main__":
    main()