with open("inputs/day4.txt", "r") as file:
    p1_score = 0
    p2_score = 0
    for line in file:
        elves = line.strip().split(",")
        elves = [elf.split("-") for elf in elves]

        if int(elves[0][0]) >= int(elves[1][0]) and int(elves[0][1]) <= int(elves[1][1]):
            p1_score += 1
        elif int(elves[0][0]) <= int(elves[1][0]) and int(elves[0][1]) >= int(elves[1][1]):
            p1_score += 1

        if int(elves[0][0]) <= int(elves[1][0]) <= int(elves[0][1]):
            p2_score += 1
        elif int(elves[1][0]) <= int(elves[0][0]) <= int(elves[1][1]):
            p2_score += 1

    print(p1_score)
    print(p2_score)
