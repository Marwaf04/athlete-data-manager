# by Marwa Fekri — COMP 348 Assignment 2
# Defines BallPlayer, BasketballPlayer, and FootballPlayer classes

from athlete import Athlete

class BallPlayer(Athlete):
    ballplayer_count = 0

    def __init__(self, name, age, country="", salary=0.0, team_name="", jersey_number=0, endorsement=""):
        super().__init__(name, age, country, salary)
        self.team_name = team_name
        self.jersey_number = int(jersey_number) if jersey_number else 0
        self.endorsement = endorsement
        BallPlayer.ballplayer_count += 1

    # This will later be overriden
    def printEndorsement(self):
        pass   

# Basketball player class
class BasketballPlayer(BallPlayer):
    basketball_count = 0

    def __init__(self, name, age, team_name, jersey_number, country="", salary=0.0, endorsement="", three_point_pct=0.0, rebounds=0):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        self.three_point_pct = float(three_point_pct) if three_point_pct else 0.0
        self.rebounds = int(rebounds) if rebounds else 0
        BasketballPlayer.basketball_count += 1
        print(f"{self.name} was added as a basketball player. Total: {BasketballPlayer.basketball_count}")

    def printStats(self):
        print(f"{self.name}: 3PT% = {self.three_point_pct}, Rebounds = {self.rebounds}")

    def printEndorsement(self):
        print(f"{self.name}'s endorsement: {self.endorsement if self.endorsement else 'None'}")

    @staticmethod
    def parse(text_line):
        try:
            parts = text_line.split(":")[1].split(",")
            parts = [p.strip() for p in parts]

            name = parts[0] if len(parts) > 0 else ""
            age = parts[1] if len(parts) > 1 else 0
            team = parts[2] if len(parts) > 2 else ""
            jersey = parts[3] if len(parts) > 3 else 0
            country = parts[4] if len(parts) > 4 else ""
            salary = parts[5] if len(parts) > 5 else 0.0
            endorsement = parts[6] if len(parts) > 6 else ""
            three_pt = parts[7] if len(parts) > 7 else 0.0
            rebounds = parts[8] if len(parts) > 8 else 0

            return BasketballPlayer(name, age, team, jersey, country, salary, endorsement, three_pt, rebounds)
        except Exception as e:
            print("Something went wrong while reading basketball player info.")
            return None

# Football Player class
class FootballPlayer(BallPlayer):
    football_count = 0

    def __init__(self, name, age, team_name, jersey_number, country="", salary=0.0, endorsement="", touchdowns=0, passing_yards=0):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        self.touchdowns = int(touchdowns) if touchdowns else 0
        self.passing_yards = int(passing_yards) if passing_yards else 0
        FootballPlayer.football_count += 1
        print(f"{self.name} was added as a football player. Total: {FootballPlayer.football_count}")

    def printStats(self):
        print(f"{self.name}: Touchdowns = {self.touchdowns}, Passing Yards = {self.passing_yards}")

    def printEndorsement(self):
        print(f"{self.name}'s endorsement: {self.endorsement if self.endorsement else 'None'}")

    @staticmethod
    def parse(text_line):
        try:
            parts = text_line.split(":")[1].split(",")
            parts = [p.strip() for p in parts]

            name = parts[0] if len(parts) > 0 else ""
            age = parts[1] if len(parts) > 1 else 0
            team = parts[2] if len(parts) > 2 else ""
            jersey = parts[3] if len(parts) > 3 else 0
            country = parts[4] if len(parts) > 4 else ""
            salary = parts[5] if len(parts) > 5 else 0.0
            endorsement = parts[6] if len(parts) > 6 else ""
            touchdowns = parts[7] if len(parts) > 7 else 0
            yards = parts[8] if len(parts) > 8 else 0

            return FootballPlayer(name, age, team, jersey, country, salary, endorsement, touchdowns, yards)
        except Exception as e:
            print("Something went wrong while reading football player info.")
            return None
