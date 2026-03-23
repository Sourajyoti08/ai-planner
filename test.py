from flask import Flask, request, render_template
import os
from planner_engine import create_schedule

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    schedule = ""

    if request.method == "POST":
        tasks = request.form.get("tasks")
        schedule = create_schedule(tasks)

    return render_template("index.html", schedule=schedule)

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
