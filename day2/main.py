def main():
    with open("data.txt", "r") as file:
        data = file.readlines()
    # Part 1 & Part 2
    x = y = aim = 0
    data = [x.strip().split() for x in data]
    for command, number in data:
        number = int(number)
        if command == "forward":
            x += number
            y += aim * number
        elif command == "down":
            aim += number
        else:
            aim -= number
    
    print(f"Solution part 1: {x * aim}")
    print(f"Solution part 2: {x * y}")

if __name__ == "__main__":
    main()