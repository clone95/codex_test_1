from flask import Flask, render_template, request, jsonify
from agent import DeterministicAgent

app = Flask(__name__)
agent = DeterministicAgent()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    data = request.get_json(force=True)
    user_input = data.get("message", "")
    response = agent.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
