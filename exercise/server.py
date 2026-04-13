from flask import Flask, request, session
import datetime
import random

app = Flask(__name__)
app.secret_key = "game-secret-key"

@app.route("/")
def hello():
    return "Hello user"

@app.route('/hello/<name>')
def helloName(name):
    return "Hello " + name

@app.route('/time')
def currentTime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return time

@app.route('/lotto')
def lotto_numbers():
    list_5_numbers = random.sample(range(1, 49), 5)
    return list_5_numbers

@app.route('/form', methods=['GET'])
def index():
    # Display the form
    return """
        <form action="/greet" method="post">
            <label>
                Name:
                <input type="text" name="user_name">
            </label>
            <label>
                Surname:
                <input type="text" name="user_surname">
            </label>
            <button type="submit">Submit</button>
        </form>
    """

@app.route('/greet', methods=['POST'])
def get_from_form():
    if request.method == "POST":
        user_name = request.form["user_name"]
        user_surname = request.form["user_surname"]
        return "Hello " + user_name + ' ' + user_surname


# Exercise 9
@app.route('/game-form', methods=["GET"])
def form():
    if 'number' not in session:
        session['number'] = random.randrange(1, 100)
    return """
        <form action="/game-answer" method="post">
            <label>
                Guess the number
                <input type="number" name="guess-number">
            </label>
            <button type="submit">Submit</button>
        </form>
    """

@app.route('/game-answer', methods=['POST'])
def guess_number():
    guess = int(request.form["guess-number"])
    number = session['number']
    if guess == number:
        session.pop("number")
        return "Congratulations, you made it!"
    elif guess < number:
        return "too little! <a href='/game-form'>Try again</a>"
    elif guess > number:
        return "too many! <a href='/game-form'>Try again</a>"

#Exercise 10

@app.route('/send-request')
def send_request_form():
    return """
        <form action="/request" method="post">
            <label>
                Method POST
            </label>
            <button type="submit">Send POST</button>
        </form>
        <form action="/request" method="get">
            <label>
                Method GET
            </label>
            <button type="submit">Send GET</button>
        </form>
    """



@app.route('/request', methods=["GET", "POST"])
def index_request():
    if request.method == "POST":
        return "You have sent a POST"
    else:
        return "You have sent a GET"
    
if __name__ == "__main__":
    app.run(debug=True)