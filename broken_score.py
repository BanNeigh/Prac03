"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def get_score():
    score = float(input("Enter score: "))
    return score


def main(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    elif 0 <= score < 50:
        return "Bad"
    else:
        return "Invalid Score"


def get_random():
    return random.randint(0, 100)


print(main(get_score()))
print(main(get_random()))
