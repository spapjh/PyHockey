import random
import time

print("""\
                    ._.                 .__                   __                 
 | | ______ ___.__.|  |__   ____   ____ |  | __ ____ ___.__. | | 
 |_| \____ <   |  ||  |  \ /  _ \_/ ___\|  |/ // __ <   |  | |_| 
 |-| |  |_> >___  ||   Y  (  <_> )  \___|    <\  ___/\___  | |-| 
 | | |   __// ____||___|  /\____/ \___  >__|_ \\___  > ____| | | 
 |_| |__|   \/          \/            \/     \/    \/\/      |_|
 Welcome to PyHockey! An incredibly simple hockey game developed by @spapjh
                    """)


# Roster for Users Team
team_a_roster = "G - Connor Russell\nD - Pedro Hernandez\nD - Cameron Ethington\nLW - Neil Cushard\nC - Zac Wojcik\nRW - Kelly Kolanos"


# Roster for Team B (Seattle WinterHawks)
team_b_roster_seattle = "G - Mike Thompson\nD - Linden Smith\nD - James Rodriguez\nLW - Sam Williams\nC - Jack Anderson\nRW - Johannes Van Der Berg"

# Roster for Team B (Austin Cowboys)
team_b_roster_austin = "G - Kriztian Vadjuk\nD - Emilian Sorensen\nD - Jason Smith\nLW - Emmanuel Rodriguez\nC - Gary Thompson\nRW - Jay Deveraux"

# Roster for Team B (Montreal Lumberjacks)
team_b_roster_montreal = "G - Juri Polakampaluu\nD - Valteri Kananen\nD - Mark Thompson\nLW - Juul Katinen\nC - George Smithy\nRW - Jean D'Abonnette"

# Roster for Team B (Toronto Lakers)
team_b_roster_toronto = "G - Jasper Raikkonen\nD - Oscar Enlund\nD - Eric Salomonson\nLW - Viktor Vorobev\nC - Bobby Sarich\nRW - Enio Aalavara"


# Team A name (user input)
team_a = input("Enter the name for your team (city and mascot): ")

# Pool of names for Team B
team_b_names = ["Seattle WinterHawks", "Austin Cowboys", "Montreal Lumberjacks", "Toronto Lakers"]

# Choose a Team B as a random choice from team_b_names pool, then creating an if loop to choose the right roster from that randomly selected team
team_b = random.choice(team_b_names)
if team_b == "Seattle WinterHawks":
    team_b_roster = team_b_roster_seattle
elif team_b == "Montreal Lumberjacks":
    team_b_roster = team_b_roster_montreal
elif team_b == "Austin Cowboys":
    team_b_roster = team_b_roster_austin
else: team_b_roster = team_b_roster_toronto


# Introduce the game Team B
print(f"Today's Game will see {team_a} face the {team_b}")


# Display starting lineups, sleep time definition for line ups
sleep_time2=1
time.sleep(sleep_time2)
print(f"Starting Lineup for {team_a}:\n {team_a_roster}")
time.sleep(sleep_time2)
print(f"And this will be the line up for the visitor's team\n {team_b_roster}")

# Initialize scores
score_a = 0
score_b = 0

# Flag to indicate if the game is over
game_over = False

# Sleep Time definition for game progress
sleep_time=2

# Number of periods in the game
periods = 3

# Main game loop, a while loop that takes place while game is NOT over
while not game_over:
    # Check if all periods have been played, if so, game over equals True
    if periods == 0:
        game_over = True
        break

    # Introduce the beginning of the period
    print(f"Period {3 - periods + 1} is about to begin!")

    # Prompt the user to continue the game
    continue_game = input("Do you want to continue the game (Y/N)? ")
    if continue_game.lower() != "y":
        game_over = True
        break

    # One period has been played
    periods -= 1

    # Number of plays in this period
    plays = random.randint(3, 8)

    # Play the game
    while plays > 0:
        # Choose a random number between 0 and 1 to represent the outcome of the play
        time.sleep(sleep_time)
        outcome = random.random()

        # If the outcome is less than 0.2, Team A scores a goal
        if outcome < 0.2:
            # Choose a random type of goal for Team A
            goal_type = random.choice(["counterattack", "long possession", "breakaway"])
            score_a += 1
            print(f"{team_a} scores a {goal_type} goal!")
        # If the outcome is between 0.2 and 0.6, Team B scores a goal
        elif outcome < 0.6:
            # Choose a random type of goal for Team B
            goal_type = random.choice(["counterattack", "long possession", "breakaway"])
            score_b += 1
            print(f"{team_b} scores a {goal_type} goal!")
        # Otherwise, the play is saved by the goalie or defense
        else:
            # Choose a random description of the save
            save_type = random.choice(["Fantastic save by the goalie", "Blocked by the defense"])
            

             # Identify the defending team
            if save_type == "Fantastic save by the goalie":
                if team_a == "Team A":
                    defending_team = team_b
                else:
                    defending_team = team_a
            else:
                if team_a == "Team A":
                    defending_team = team_a
                else:
                    defending_team = team_b

            print(f"{save_type} for {defending_team}!")

        # Print the current scoreH
        print(f"Current score: {team_a} {score_a} - {team_b} {score_b}")

        # Decrement the number of plays
        plays -= 1

        # Check if the game is over
        if periods == 0 and score_a != score_b:
            game_over = True
            break

# Determine the winner
if score_a > score_b:
    print(f"{team_a} wins the game!")
elif score_b > score_a:
    print(f"{team_b} wins the game!")
else:
    print("The game is a tie!")
