import random

# Team A name
team_a = input("Enter the name for your team (city and mascot): ")

# Pool of names for Team B
team_b_names = ["Seattle WinterHawks", "Austin Cowboys", "Montreal Lumberjacks", "Toronto Lakers"]

# Choose a random name for Team B
team_b = random.choice(team_b_names)

# Introduce Team B
print(f"Opposition: {team_b}")

# Initialize scores
score_a = 0
score_b = 0

# Flag to indicate if the game is over
game_over = False

# Number of periods in the game
periods = 3

# Main game loop
while not game_over:
    # Check if all periods have been played
    if periods == 0:
        game_over = True
        break

    # Introduce the beginning of a period
    print(f"Period {3 - periods + 1} is about to begin!")

    # Prompt the user to continue the game (so that it is not all shown at once! :) )
    continue_game = input("Do you want to continue the game (Y/N)? ")
    if continue_game.lower() != "y":
        game_over = True
        break

    # One period has been played
    periods -= 1

    # Number of plays in this period (min 3 max 8, so that score does not go out of control)
    plays = random.randint(3, 8)

    # Play the game
    while plays > 0:
        # Choose a random number between 0 and 1 to represent the outcome of the play
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

        # Print the current score
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
