# by Marwa Fekri — COMP 348 Assignment 2
# Contains the Athlete base class and HockeyPosition enum used by HockeyPlayer

from enum import Enum

class HockeyPosition(Enum):
    Forward = "Forward"
    Defenseman = "Defenseman"
    Goalie = "Goalie"

# This is the base class for all athletes that will be created
class Athlete:
    athlete_count = 0  # this will be used to count how many athletes were created

    def __init__(self, name, age, country="", salary=0.0):
        self.name = name
        self.age = int(age)
        self.country = country
        self.salary = float(salary) if salary else 0.0

        Athlete.athlete_count += 1
        print(f"{self.name} (age {self.age}) was added. Total athletes: {Athlete.athlete_count}")

    # This will be used later in subclasses
    def printStats(self):
        pass

    # Only ball players will use this ones
    def printEndorsement(self):
        pass