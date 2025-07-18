# main.py
# by Marwa Fekri — COMP 348 Assignment 2
# Full interactive menu with all 7 options, including charts

from utils import load_athletes, save_athletes, delete_athletes_by_name, find_athlete_by_name
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BasketballPlayer, FootballPlayer, BallPlayer

import matplotlib.pyplot as plt

athletes = []
filename = ""
unsaved_changes = False

def show_menu():
    print("\n========== Athlete Management ==========")
    print("1. Load File")
    print("2. Print Stats")
    print("3. Delete Athlete")
    print("4. Save File")
    print("5. Athlete Info")
    print("6. Display Chart")
    print("7. Exit")
    print("========================================")

def print_stats():
    total = len(athletes)
    hockey = sum(1 for a in athletes if isinstance(a, HockeyPlayer))
    swimmer = sum(1 for a in athletes if isinstance(a, Swimmer))
    basketball = sum(1 for a in athletes if isinstance(a, BasketballPlayer))
    football = sum(1 for a in athletes if isinstance(a, FootballPlayer))
    ball = basketball + football

    print("\n--- Statistics ---")
    print(f"{total} athletes")
    print(f"{hockey} Hockey Players")
    print(f"{ball} Ball Players ({basketball} Basketball and {football} Football)")
    print(f"{swimmer} Swimmers")

    endorsements = {}
    for a in athletes:
        if isinstance(a, BallPlayer):
            brand = a.endorsement if a.endorsement else "None"
            endorsements[brand] = endorsements.get(brand, 0) + 1

    print("\nEndorsements:")
    for brand in sorted(endorsements):
        print(f"{brand}: {endorsements[brand]}")

    print("\nGoals scored:")
    goal_players = sorted(
        [a for a in athletes if isinstance(a, HockeyPlayer)],
        key=lambda x: (-x.goals_scored, x.name)
    )
    for p in goal_players:
        print(f"{p.goals_scored} {p.name}")

    print("\nTouchdowns:")
    td_players = sorted(
        [a for a in athletes if isinstance(a, FootballPlayer)],
        key=lambda x: (-x.touchdowns, x.name)
    )
    for p in td_players:
        print(f"{p.touchdowns} {p.name}")

def display_chart_menu():
    while True:
        print("\n----- Display Chart -----")
        print("1. Number of Athletes (level 1)")
        print("2. Number of Athletes (leaf level)")
        print("3. Athletes Salaries (level 1)")
        print("4. Athletes Salaries (leaf level)")
        print("5. Endorsements")
        print("6. Back to Main Menu")

        choice = input("Choose an option (1–6): ")

        if choice == "1":
            level1_athlete_chart()
        elif choice == "2":
            leaf_level_chart()
        elif choice == "3":
            salary_level1_chart()
        elif choice == "4":
            salary_leaf_chart()
        elif choice == "5":
            endorsement_chart()
        elif choice == "6":
            break
        else:
            print("Please enter a valid option.")

def level1_athlete_chart():
    hockey = sum(1 for a in athletes if isinstance(a, HockeyPlayer))
    swimmer = sum(1 for a in athletes if isinstance(a, Swimmer))
    ball = sum(1 for a in athletes if isinstance(a, BallPlayer))

    labels = ['HockeyPlayer', 'BallPlayer', 'Swimmer']
    counts = [hockey, ball, swimmer]

    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Athletes (Level 1)")
    plt.show()

def leaf_level_chart():
    hockey = sum(1 for a in athletes if isinstance(a, HockeyPlayer))
    swimmer = sum(1 for a in athletes if isinstance(a, Swimmer))
    basketball = sum(1 for a in athletes if isinstance(a, BasketballPlayer))
    football = sum(1 for a in athletes if isinstance(a, FootballPlayer))

    labels = ['Hockey', 'Swimmer', 'Basketball', 'Football']
    counts = [hockey, swimmer, basketball, football]

    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Athletes (Leaf Level)")
    plt.show()

def salary_level1_chart():
    groups = {'HockeyPlayer': [], 'BallPlayer': [], 'Swimmer': []}
    for a in athletes:
        if isinstance(a, HockeyPlayer) and a.salary > 0:
            groups['HockeyPlayer'].append(a.salary)
        elif isinstance(a, BallPlayer) and a.salary > 0:
            groups['BallPlayer'].append(a.salary)
        elif isinstance(a, Swimmer) and a.salary > 0:
            groups['Swimmer'].append(a.salary)

    labels = []
    values = []
    for group, salaries in groups.items():
        if salaries:
            labels.append(group)
            values.append(sum(salaries) / len(salaries))

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Average Salaries (Level 1)")
    plt.show()

def salary_leaf_chart():
    groups = {'Hockey': [], 'Swimmer': [], 'Basketball': [], 'Football': []}
    for a in athletes:
        if isinstance(a, HockeyPlayer) and a.salary > 0:
            groups['Hockey'].append(a.salary)
        elif isinstance(a, Swimmer) and a.salary > 0:
            groups['Swimmer'].append(a.salary)
        elif isinstance(a, BasketballPlayer) and a.salary > 0:
            groups['Basketball'].append(a.salary)
        elif isinstance(a, FootballPlayer) and a.salary > 0:
            groups['Football'].append(a.salary)

    labels = []
    values = []
    for group, salaries in groups.items():
        if salaries:
            labels.append(group)
            values.append(sum(salaries) / len(salaries))

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Average Salaries (Leaf Level)")
    plt.show()

def endorsement_chart():
    endorsements = {}
    for a in athletes:
        if isinstance(a, BallPlayer):
            brand = a.endorsement if a.endorsement else "None"
            endorsements[brand] = endorsements.get(brand, 0) + 1

    labels = list(endorsements.keys())
    counts = list(endorsements.values())

    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title("Endorsements by Ball Players")
    plt.show()

def main():
    global athletes, filename, unsaved_changes

    while True:
        show_menu()
        choice = input("Choose an option (1–7): ")

        if choice == "1":
            filename = input("Enter filename to load: ")
            athletes = load_athletes(filename)
            unsaved_changes = False

        elif choice == "2":
            if not athletes:
                print("No athletes loaded yet.")
            else:
                print_stats()

        elif choice == "3":
            if not athletes:
                print("There's no data to delete.")
            else:
                name = input("Enter the name of the athlete you want to delete: ")
                athletes = delete_athletes_by_name(athletes, name)
                unsaved_changes = True

        elif choice == "4":
            if not filename:
                print("No file has been loaded yet.")
            else:
                save_athletes(filename, athletes)
                unsaved_changes = False

        elif choice == "5":
            name = input("Enter the athlete's name: ")
            athlete = find_athlete_by_name(athletes, name)
            if athlete:
                athlete.printStats()
                athlete.printEndorsement()
            else:
                print("That athlete wasn't found.")

        elif choice == "6":
            if not athletes:
                print("You need to load some athletes first.")
            else:
                display_chart_menu()

        elif choice == "7":
            if unsaved_changes:
                confirm = input("You haven't saved changes. Are you sure you want to exit? (yes/no): ").lower()
                if confirm != "yes":
                    continue
            print("Goodbye!")
            break

        else:
            print("Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
