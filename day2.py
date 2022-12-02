with open("inputs/day2.txt", "r") as file:
    score_p1 = 0
    score_p2 = 0

    lines = []

    for line in file:
        lines.append(line.strip().split(" "))

    for line in lines:
        # Convert letters to 1: Rock, 2: Paper, 3: Scissors
        line[0] = ord(line[0]) - ord("A") + 1
        line[1] = ord(line[1]) - ord("X") + 1

        score_p1 += line[1]

        # Mod Circle to see if I won
        if line[0] == (line[1] + 1) % 3 + 1:
            score_p1 += 6
        if line[0] == line[1]:
            score_p1 += 3

        # For part 2, add my score if I draw or win
        score_p2 += ((line[1] - 1) * 3)

        if line[1] == 2:  # If I draw
            score_p2 += line[0]
        elif line[1] == 1:  # If I win
            score_p2 += (line[0] + 1) % 3 + 1
        else:  # If I lose
            score_p2 += (line[0] % 3) + 1

    print(score_p1)
    print(score_p2)
