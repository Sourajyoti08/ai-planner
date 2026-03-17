import google.generativeai as genai
from settings import SETTINGS
import os
# configure AI
genai.configure(api_key="AIzaSyBgcR4hrby06uIU-CgfiW_gRm2i5rK3V90")

model = genai.GenerativeModel("gemini-3-flash-preview")


def create_schedule(user_tasks):

    prompt = f"""
You are an intelligent daily planner.

User tasks:
{user_tasks}

Constraints:
Wake up: {SETTINGS['wake']}
Lunch: {SETTINGS['lunch']}
Dinner: {SETTINGS['dinner']}
Sleep: {SETTINGS['sleep']}

Rules:
- minimal
- create a balanced schedule
- include small breaks
- keep it realistic
- output only the schedule with times

Example format:

07:00 AM - Wake up
07:30 AM - Study
09:00 AM - Break
"""

    response = model.generate_content(prompt)

    return response.text
