# by Marwa Fekri — COMP 348 Assignment 2
# Defines the HockeyPlayer class (subclass of Athlete)

from athlete import Athlete, HockeyPosition

class HockeyPlayer(Athlete):
    # to track how many HockeyPlayer objects created
    hockey_count = 0  

    def __init__(self, name, age, country="", salary=0.0, position=None, goals_scored=0, stick_brand="", skates_size=0):
        # Call the Athlete constructor first using super
        super().__init__(name, age, country, salary)

        # Set hockey-specific attributes
        self.position = position  
        self.goals_scored = int(goals_scored) if goals_scored else 0
        self.stick_brand = stick_brand
        self.skates_size = int(skates_size) if skates_size else 0

        HockeyPlayer.hockey_count += 1
        print(f"{self.name} was added as a hockey player. Total: {HockeyPlayer.hockey_count}")

    def printStats(self):
        pos = self.position.name if self.position else "Unknown"
        print(f"{self.name}: Position = {pos}, Goals = {self.goals_scored}, Stick = {self.stick_brand}, Skates = {self.skates_size}")

    @staticmethod
    def parse(text_line):
        try:
            parts = text_line.split(":")[1].split(",")
            parts = [p.strip() for p in parts]

            name = parts[0] if len(parts) > 0 else ""
            age = parts[1] if len(parts) > 1 else 0
            country = parts[2] if len(parts) > 2 else ""
            salary = parts[3] if len(parts) > 3 else 0.0
            position_str = parts[4] if len(parts) > 4 else None
            goals = parts[5] if len(parts) > 5 else 0
            stick = parts[6] if len(parts) > 6 else ""
            skates = parts[7] if len(parts) > 7 else 0

            # convert string to enum
            pos = HockeyPosition[position_str] if position_str in HockeyPosition.__members__ else None

            return HockeyPlayer(name, age, country, salary, pos, goals, stick, skates)
        except:
            print("Could not load hockey player.")
            return None
