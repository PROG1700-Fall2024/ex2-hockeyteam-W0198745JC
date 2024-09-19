# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    #YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("Hello and Welcome to the Hockey Team Calculator!")
    #input ask user name of team
    TeamName = input ("Please enter you team name:")
    #input ask user number of wins
    Wins = input ("How many wins have the {0} had this season?".format(TeamName)) 
    #input ask user number of losses
    Losses = input("How many Losses Have The {0} had this season?".format(TeamName))
    print("Please wait while we calculate your answer")
    #cast wins and losses into integer and add together to create total games
    TotalGames = int(Wins)+int(Losses)
    #divide wins by total games

    #put it all together in a single string
    print("The {0} have {1} wins and {2} Losses This Season with a winning percentage of ... ".format(TeamName,Wins,Losses) + str(round(int(Wins) / TotalGames,4)))
    # YOUR CODE ENDS HERE

main()