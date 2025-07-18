# Athlete Data Manager

A modular Python application that reads, parses, and manages athlete data across multiple sports using object-oriented programming principles.

## Overview

This project processes athlete data from a structured text file and categorizes each athlete based on their sport (e.g., Hockey, Swimming, Basketball, Football). Each sport-specific class inherits from a common `Athlete` superclass. The program handles missing or partial data and is designed to be easily extended with additional features or sports.

## Features

- Reads and parses athlete data from a `.txt` file
- Implements class inheritance and method overriding
- Modular structure for clean code organization
- Handles missing or malformed data gracefully
- Easily extendable for future enhancements

## Project Structure

```
athlete.py         # Base Athlete class  
hockey.py          # HockeyPlayer class  
swimmer.py         # Swimmer class  
ball.py            # BasketballPlayer and FootballPlayer classes  
utils.py           # Helper functions for parsing and formatting  
main.py            # Entry point for the application  
athletes.txt       # Input data file with athlete records  
```

## Input Format (athletes.txt)

Each line describes a single athlete, beginning with the type of sport. Examples:

```
HockeyPlayer: Liam Carter,27,Canada,3500000.0,,0,,0  
Swimmer: Ava Thompson,23,Freestyle,USA,250000.0,52.3  
BasketballPlayer: Jaylen Moore,24,Chicago Blaze,8,USA,4500000.0,Nike,0.38,6  
FootballPlayer: Tyrone Jackson,29,Atlanta Hawks,12,USA,5200000.0,Nike,18,3500  
```

## How to Run

Make sure you have Python 3 installed. Then run:

```
python main.py
```

Ensure the `athletes.txt` file is located in the same directory as `main.py`.

## Concepts Demonstrated

- Object-Oriented Programming (OOP)
- File I/O and string parsing
- Data validation and error handling
- Modular and maintainable code design

## Possible Extensions

- Export results to CSV or JSON
- Add a graphical user interface (GUI)
- Include statistics and data visualizations
- Connect to a database for persistent storage

## Author

**Marwa Fekri**  
Software Engineering Student, Concordia University  
GitHub: marwaf04

