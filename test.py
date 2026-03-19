from flask import Flask, request
import os
from planner_engine import create_schedule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    schedule = ""

    if request.method == "POST":
        tasks = request.form.get("tasks")
        schedule = create_schedule(tasks)

    return f"""
    <body style="background-color: rgb(31, 31, 31);">
    
    <h2 style="font-family: Special Elite, monospace;color: white;font-size: 50px;">AI Daily Planner.</h2>
    <div style="display: flex; justify-content: center; align-items: center;">
    <form method="post">
        <textarea style="font-family: jetbrains mono;
    padding: 5px;
    background-color: rgb(192, 192, 192);
    border-radius: 5px;
    box-shadow: 0 0 5px rgb(121, 121, 121), 0 0 25px rgb(97, 97, 97), 0 0 100px rgb(75, 75, 75);" name="tasks" rows="10" cols="50"
        placeholder="What do you want to do today?"></textarea><br><br>
        <button style=" padding: 20px 20px;
  width: 180px;
  font-family: Special Elite, monospace;
  font-size: 14px;
  letter-spacing: 1px;
  background: linear-gradient(to right, rgb(0, 0, 20), rgb(61, 0, 140), rgb(111, 0, 255),  rgb(61, 0, 140), rgb(0, 0, 20));
  background-size: 200%;
  border-radius: 10px;
  border: 1px solid white;
  color: white;
  animation: animationGradient 8s infinite linear;
  transition: 0.3s ease-in;
  cursor: pointer;" type="submit">GENERATE</button>
    </form>
    </div>
</body>
    <pre style="color: white; font-family: "Special Elite", monospace;">{schedule}</pre>
    """

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
