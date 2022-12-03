from itertools import islice

# Part 1
with open("inputs/day3.txt", "r") as file:
    score = 0

    for line in file:
        line = line.strip()
        first_half, second_half = line[:len(line) // 2], line[len(line) // 2:]
        seen = set(first_half).intersection(set(second_half))
        letter = seen.pop()

        if letter.isupper():
            increment = ord(letter) - ord("A") + 27
        else:
            increment = ord(letter) - ord("a") + 1
        score += increment

    print(score)

# Part 2
with open("inputs/day3.txt", "r") as file:
    score = 0

    while True:
        group = list(islice(file, 3))
        if not group:
            break

        seen = (set(group[0].strip()).intersection(group[1].strip())).intersection(group[2].strip())
        letter = seen.pop()

        if letter.isupper():
            increment = ord(letter) - ord("A") + 27
        else:
            increment = ord(letter) - ord("a") + 1
        score += increment

    print(score)

