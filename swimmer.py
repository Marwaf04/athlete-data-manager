# by Marwa Fekri — COMP 348 Assignment 2
# Defines the Swimmer class

from athlete import Athlete

class Swimmer(Athlete):
    swimmer_count = 0  # Tracks number of swimmers

    def __init__(self, name, age, stroke_style, country="", salary=0.0, personal_best_time=0.0):
        # Call the parent constructor usif super
        super().__init__(name, age, country, salary)

        # Set swimmer  attributes
        self.stroke_style = stroke_style
        self.personal_best_time = float(personal_best_time) if personal_best_time else 0.0

        Swimmer.swimmer_count += 1
        print(f"{self.name} was added as a swimmer. Total: {Swimmer.swimmer_count}")

    def printStats(self):
        print(f"{self.name}: Style = {self.stroke_style}, Best Time = {self.personal_best_time} sec")

    @staticmethod
    def parse(text_line):
        try:
            parts = text_line.split(":")[1].split(",")
            parts = [p.strip() for p in parts]

            name = parts[0] if len(parts) > 0 else ""
            age = parts[1] if len(parts) > 1 else 0
            stroke_style = parts[2] if len(parts) > 2 else ""
            country = parts[3] if len(parts) > 3 else ""
            salary = parts[4] if len(parts) > 4 else 0.0
            best_time = parts[5] if len(parts) > 5 else 0.0

            return Swimmer(name, age, stroke_style, country, salary, best_time)
        except:
            print("Could not load swimmer.")
            return None
