import os

with open(os.path.join(os.path.dirname(__file__), "day02.txt"), "r") as f:
    data = f.read().splitlines()

strategy = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

scores = [strategy[k] for k in data]

new_strategy = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

new_scores = [new_strategy[k] for k in data]

print(sum(scores))
print(sum(new_scores))
