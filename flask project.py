#Create a Flask Application that takes the user name in the query parameter from the URL and converts it to UPPER CASE and displays it on the browser.
# **BONUS - Be a little creative and try to create some cool functions in your Flask App.**

from flask import Flask, request
import random
from datetime import datetime

app = Flask(__name__)

# Bonus function 1: return emoji based on name length
def get_emoji(name):
    if len(name) <= 3:
        return "😎"
    elif len(name) <= 6:
        return "🤩"
    else:
        return "🚀"

# Bonus function 2: return motivational message randomly
def get_message():
    messages = [
        "Keep shining! ✨",
        "You are awesome! 💪",
        "Believe in yourself! 🌟",
        "Code like a pro! 👨‍💻",
        "Dream big! 🌈"
    ]
    return random.choice(messages)

# Bonus function 3: change background based on time
def get_background():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "linear-gradient(to right, #FFDEE9, #B5FFFC)"  # morning
    elif 12 <= hour < 18:
        return "linear-gradient(to right, #f7971e, #ffd200)"  # afternoon
    elif 18 <= hour < 21:
        return "linear-gradient(to right, #0f2027, #203a43, #2c5364)"  # evening
    else:
        return "linear-gradient(to right, #2c3e50, #4ca1af)"  # night

@app.route("/")
def home():
    name = request.args.get("name", "Guest").upper()
    emoji = get_emoji(name)
    message = get_message()
    background = get_background()

    html_content = f"""
    <html>
        <head>
            <title>Welcome Page</title>
            <style>
                body {{
                    background: {background};
                    font-family: Arial, sans-serif;
                    text-align: center;
                    color: white;
                    padding-top: 100px;
                }}
                h1 {{
                    font-size: 60px;
                    margin-bottom: 20px;
                    text-shadow: 2px 2px 5px #000000;
                }}
                p {{
                    font-size: 24px;
                    text-shadow: 1px 1px 3px #000000;
                }}
                .note {{
                    margin-top: 40px;
                    font-size: 16px;
                    color: #ffe4e1;
                }}
            </style>
        </head>
        <body>
            <h1>HELLO {name} ! {emoji}</h1>
            <p>{message}</p>
            <p class="note">Try adding your name in the URL: <code>?name=alex</code></p>
        </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(debug=True)
