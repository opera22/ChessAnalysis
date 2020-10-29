import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("games.csv", usecols=["white_rating", "black_rating", "turns", "winner"])

# winner counts bar chart
winner_counts = df["winner"].value_counts()
count_wins_white = winner_counts["white"]
count_wins_black = winner_counts["black"]
white_win_percent = count_wins_white / len(df["winner"])
black_win_percent = count_wins_black / len(df["winner"])

print("white wins: " + str(count_wins_white))
print("black wins: " + str(count_wins_black))
#difference of 894 with original dataset

plt.bar(["White", "Black"], [count_wins_white, count_wins_black])
plt.title("White wins: " + str(count_wins_white) + " Black wins: " + str(count_wins_black) + \
    "\nProbability that white wins: " + str(round(white_win_percent, 3)) + \
    "\nProbability that black wins: " + str(round(black_win_percent, 3)))   
plt.show()
