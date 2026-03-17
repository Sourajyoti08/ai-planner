import os
from planner_engine import create_schedule

os.system("cls")

print("===== AI DAILY PLANNER =====\n")

tasks = input("What do you want to do today?\n\n> ")

schedule = create_schedule(tasks)

print("\n\n===== YOUR SCHEDULE =====\n")
print(schedule)

