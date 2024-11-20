from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"

@app.route("/random_cs_jokes")
def random_programming_jokes():
    url = "https://v2.jokeapi.dev/joke/Programming"
    response = requests.get(url).json()
    return f"Here is your joke:\n{response["joke"]}"


if __name__ == "__main__":
    app.run(debug=True)