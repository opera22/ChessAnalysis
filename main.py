import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np

# created an "original" dataframe (df_original) because the other copy (df) is often modified
df_original = pd.read_csv("games.csv", usecols=["white_rating", "black_rating", "turns", "winner", "opening_ply", "opening_name"])
df = df_original

# winner counts bar chart
def winner_counts_bar_chart():

    winner_counts = df["winner"].value_counts()
    count_wins_white = winner_counts["white"]
    count_wins_black = winner_counts["black"]
    white_win_percent = count_wins_white / len(df["winner"])
    black_win_percent = count_wins_black / len(df["winner"])

    # white goes first in chess, so these numbers should be slightly different
    print("white wins: " + str(count_wins_white))
    print("black wins: " + str(count_wins_black))

    plt.bar(["White", "Black"], [count_wins_white, count_wins_black])
    plt.title("White wins: " + str(count_wins_white) + " Black wins: " + str(count_wins_black) + \
        "\nProbability that white wins: " + str(round(white_win_percent, 3)) + \
        "\nProbability that black wins: " + str(round(black_win_percent, 3)))   
    plt.show()

# Average rating and average amount of book moves at opening ()
def book_moves_by_rating():

    # this bit of code creates an avg_rating column
    avg_ratings = []

    for index in range(len(df["white_rating"])):
        avg = ( df["white_rating"][index] + df["black_rating"][index] ) // 2
        avg_ratings.append(avg)

    df["avg_rating"] = avg_ratings

    df_avg_opening_ply = df.groupby(["avg_rating"])["opening_ply"].mean()

    df_avg_opening_ply.to_csv("games_new.csv", index = True, header = True)

    df_avg_opening_ply = pd.read_csv("games_new.csv")

    plt.plot(df_avg_opening_ply["avg_rating"], df_avg_opening_ply["opening_ply"])
    plt.xlabel("Ratings")
    plt.ylabel("Average Amt. of Book Moves at Opening")
    plt.title("Book Moves by Rating")
    plt.show()

def book_moves_by_rating_mavg():

    # this bit of code creates an avg_rating column
    avg_ratings = []

    for index in range(len(df["white_rating"])):
        avg = ( df["white_rating"][index] + df["black_rating"][index] ) // 2
        avg_ratings.append(avg)

    df["avg_rating"] = avg_ratings

    df_avg_opening_ply = df.groupby(["avg_rating"])["opening_ply"].mean()
    df_avg_opening_ply.to_csv("games_new.csv", index = True, header = True)
    df_avg_opening_ply = pd.read_csv("games_new.csv")

    df_avg_opening_ply["MA"] = df_avg_opening_ply["opening_ply"].rolling(30, min_periods=1).mean()
    df_avg_opening_ply.to_csv("games_new.csv", index = True, header = True)
    df_avg_opening_ply = pd.read_csv("games_new.csv")

    plt.plot(df_avg_opening_ply["avg_rating"], df_avg_opening_ply["opening_ply"])
    plt.plot(df_avg_opening_ply["avg_rating"], df_avg_opening_ply["MA"])
    plt.xlabel("Ratings")
    plt.ylabel("Average Amt. of Book Moves at Opening")
    plt.title("Book Moves by Rating -- Moving Average")
    plt.show()

# winner counts bar chart
def opening_counts_bar_chart():


    df["opening_counts"] = df['opening_name'].map(df['opening_name'].value_counts())
    
    sorted_df = df.sort_values(["opening_counts"], ascending=[False])
    sorted_df = sorted_df.drop_duplicates("opening_name", keep="first")

    print(sorted_df)


    """ plt.bar(["White", "Black"], [count_wins_white, count_wins_black])
    plt.title("White wins: " + str(count_wins_white) + " Black wins: " + str(count_wins_black) + \
        "\nProbability that white wins: " + str(round(white_win_percent, 3)) + \
        "\nProbability that black wins: " + str(round(black_win_percent, 3)))   
    plt.show() """

# Default number of entries is 10,000 but it can be changed by the user
entries = 10000
df = df_original.head(entries)

print("-----------------------------")
print("Welcome to the Chess Analyzer")
print("-----------------------------")

exit_loop = False
while exit_loop == False:

    print("Select an option:")
    print("(W) View the Winner Counts bar chart")
    print("(B) View the Book Moves by Rating graph")
    print("(M) View the Book Moves by Rating MOVING AVG graph")
    print("(O) View the Opening Counts bar chart")
    print("(E) Change the amount of entries (" + str(entries) + ")")
    print("(X) Exit")
    user_input = input().lower()

    if user_input == "w":
        winner_counts_bar_chart()
    elif user_input == "b":
        book_moves_by_rating()
    elif user_input == "m":
        book_moves_by_rating_mavg()
    elif user_input == "o":
        opening_counts_bar_chart()
    elif user_input == "e":
        num = int(input("Enter a number 100-20000: "))
        if num < 100 or num > 20000:
            print("That number is out of range!")
        else:
            entries = num
            df = df_original.head(entries)
    elif user_input == "x":
        exit_loop = True

print("~~ Goodbye! ~~")




#df = pd.read_csv("games_new.csv")
#pd.to_csv("games_new.csv", index = True, header = True)