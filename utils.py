# by Marwa Fekri — COMP 348 Assignment 2
# Utility functions for loading, saving, deleting, and searching athlete data

from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BasketballPlayer, FootballPlayer

def load_athletes(filename):
    athletes = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("HockeyPlayer:"):
                    athlete = HockeyPlayer.parse(line)
                elif line.startswith("Swimmer:"):
                    athlete = Swimmer.parse(line)
                elif line.startswith("BasketballPlayer:"):
                    athlete = BasketballPlayer.parse(line)
                elif line.startswith("FootballPlayer:"):
                    athlete = FootballPlayer.parse(line)
                else:
                    print(f"Couldn’t recognize this line: {line}")
                    athlete = None

                if athlete:
                    athletes.append(athlete)

        print(f"{len(athletes)} athletes were loaded from '{filename}'")
        return athletes

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except:
        print("Something went wrong while loading athletes.")
        return []

# -------------------------
def save_athletes(filename, athletes):
    try:
        confirm = input("Are you sure you want to overwrite the file? (yes/no): ").lower()
        if confirm != "yes":
            print("Save cancelled.")
            return

        with open(filename, "w") as file:
            for athlete in athletes:
                line = to_text_line(athlete)
                file.write(line + "\n")

        print(f"Saved {len(athletes)} athletes to '{filename}'")
    except:
        print("Could not save the file.")

# -------------------------
def to_text_line(athlete):
    # Converts an athlete object to a text line (for saving)
    if isinstance(athlete, HockeyPlayer):
        pos = athlete.position.name if athlete.position else ""
        return f"HockeyPlayer: {athlete.name},{athlete.age},{athlete.country},{athlete.salary},{pos},{athlete.goals_scored},{athlete.stick_brand},{athlete.skates_size}"
    elif isinstance(athlete, Swimmer):
        return f"Swimmer: {athlete.name},{athlete.age},{athlete.stroke_style},{athlete.country},{athlete.salary},{athlete.personal_best_time}"
    elif isinstance(athlete, BasketballPlayer):
        return f"BasketballPlayer: {athlete.name},{athlete.age},{athlete.team_name},{athlete.jersey_number},{athlete.country},{athlete.salary},{athlete.endorsement},{athlete.three_point_pct},{athlete.rebounds}"
    elif isinstance(athlete, FootballPlayer):
        return f"FootballPlayer: {athlete.name},{athlete.age},{athlete.team_name},{athlete.jersey_number},{athlete.country},{athlete.salary},{athlete.endorsement},{athlete.touchdowns},{athlete.passing_yards}"
    else:
        return ""

# -------------------------
def delete_athletes_by_name(athletes, name):
    matches = [a for a in athletes if a.name.lower() == name.lower()]
    if not matches:
        print(f"No athlete named '{name}' found.")
        return athletes

    if len(matches) > 1:
        confirm = input(f"There is more than one athlete named '{name}'. Do you want to delete them all? (yes/no): ").lower()
        if confirm != "yes":
            print("Nothing was deleted.")
            return athletes

    athletes = [a for a in athletes if a.name.lower() != name.lower()]
    print(f"{len(matches)} athlete named '{name}' were deleted.")
    return athletes

# -------------------------
def find_athlete_by_name(athletes, name):
    for a in athletes:
        if a.name.lower() == name.lower():
            return a
    return None
