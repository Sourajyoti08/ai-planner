import google.generativeai as genai
from settings import SETTINGS
import os
# configure AI
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")


def create_schedule(user_tasks):

    prompt = f"""
You are an intelligent daily planner.

User tasks:
{user_tasks}

Constraints:
Wake up: {SETTINGS['wake']}
Breakfast: {SETTINGS['breakfast']}
Lunch: {SETTINGS['lunch']}
Dinner: {SETTINGS['dinner']}
Sleep: {SETTINGS['sleep']}

Rules:
- minimal
- create a balanced schedule
- include small breaks
- keep it realistic
- output only the schedule with times
- give 3 custom tips for the day, in order to reach the goals. Like secret tips.
Example format:

07:00 AM - Wake up
07:30 AM - Study
09:00 AM - Break
....
....

TIPs:
1..................................
2.
3.
"""

    response = model.generate_content(prompt)

    return response.text
