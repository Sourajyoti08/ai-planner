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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <body style="background: #242424 radial-gradient(circle at top, #252525, #000000);
    margin-bottom: 250px;
    font-family: 'JetBrains Mono', monospace;
    color:white;
    ">
    <div style="
        display:flex;
        justify-content:center;
        align-items: center;
        margin-top: 20px;
        ">
    <p style="
        color: rgb(255, 110, 110);
        background-color: #670000;
        border: 1px solid rgb(255, 110, 110);
        width: 200px;
        height: 30px;
        font-size: 13px;
        border-radius: 30px;
        display:flex;
        justify-content:center;
        align-items:center;
        font-weight: 100;
        ">● Time<span style="color: #ffd35a;">IT&nbsp;</span> App</p></div>
    <h1 style="
        text-align:center;
        font-size: clamp(35px, 8vw, 60px);
        margin-top:10px;
        font-family: 'Special Elite',  monospace;
        letter-spacing:2px;
    ">
       <span style="color:#00bfff; font-size: clamp(40px, 9vw, 70px);">AI </span>Daily Planner
    </h1>
<hr style="width:60%; margin:30px auto; border:0.5px solid #3c3c3c;">

    <p style="
        text-align:center;
        color:#bdbdbd;
        font-size: clamp(14px, 3.5vw, 18px);
        margin: 10px 20px;
        line-height: 25px;
    ">AI-powered daily planning in seconds.<br>
        Turn your <span style="
        font-size: clamp(20px, 6vw, 35px);
        filter: blur(0.8px);
        color: rgb(255, 132, 132);
        letter-spacing: 2px;
        ">
        messy</span> thoughts into a perfectly structured day.
    </p>
    <hr style="width:50%; margin:30px auto; border:0.5px solid #3c3c3c;">


    <div style="
        display:flex;
        justify-content:center;
        align-items:center;
        margin-top:30px;
        padding:10px;
    ">

        <form method="post" style="
            width:100%;
            max-width:500px;
            background: rgba(255, 255, 255, 0.045);
            padding:25px;
            border-radius:20px;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 20px rgba(52, 52, 52, 0.5);
            text-align:center;
        ">

            <textarea name="tasks"
            placeholder="What do you want to do today?

Example: &quot;feeling low energy today, I just want to revise one chapter, maybe read a bit, take proper breaks, and relax in the evening....&quot;"
            "
            
            style="
                width:90%;
                height:180px;
                padding:15px;
                border-radius:10px;
                border:none;
                outline:none;
                background: rgba(139, 139, 139, 0.121);
                color:white;
                font-size:14px;
                box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
                resize:none;
            "></textarea>

            <button type="submit" onclick="this.innerText='GENERATING...';" style=" 
                margin-top:20px;
                padding:14px;
                width:100%;
                max-width:200px;
                font-family: 'Special Elite', monospace;
                font-size:14px;
                letter-spacing:1px;
                background: linear-gradient(to right, #000014, #3d008c, #6f00ff, #3d008c, #000014);
                background-size:200%;
                border-radius:10px;
                border:1px solid white;
                color:white;
                cursor:pointer;
                transition:0.3s;
            ">
                GENERATE
            </button>

        </form>

    </div>
<div style="
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    background: #111;
    color: #b9b9b9;
    padding: 10px;
    font-size: 12px;
">
    Made by a Solo DEV ⚡ | <a style="text-decoration: none; color: white" href="mailto:sourajyotidey2008@gmail.com"> Contact Me</a>
</div>
</body>
<div style="
        padding: 20px;
        width: 90%;
        max-width: 800px;
        margin: 20px auto;
        border: none;
        ">
    <pre style="
    color: white;
    font-family: "Special Elite", monospace;
    white-space: pre-wrap;
    word-wrap: break-word;
    overflow-wrap: break-word;
    
    ">{schedule}</pre></div>
    """

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
