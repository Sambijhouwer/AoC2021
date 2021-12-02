def main():
    with open("data.txt", "r") as file:
        data = file.readlines()
    data = [int(x.strip()) for x in data]

    # Solution 1
    print("Solution 1: ", end="")
    print(len([x for x in range(len(data) - 1) if data[x] < data[x + 1]]))

    # Solution 2
    data = list(zip(data, data[1:], data[2:]))
    print("Solution 2: ", end="")
    print(len([x for x in range(len(data) - 1) if sum(data[x]) < sum(data[x + 1])]))

if __name__ == "__main__":
    main()