with open("inputs/day1.txt", "r") as file:
    elves = [0]
    current = 0

    for num in file:
        if num.strip() != "":
            elves[current] += int(num)
        else:
            elves.append(0)
            current += 1

print(max(elves))
elves.sort()
print(sum(elves[-3:]))
