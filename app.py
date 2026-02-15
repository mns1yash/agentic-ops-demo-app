from flask import Flask
import time
import random
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Agentic Ops Demo App is running"

@app.route("/slow")
def slow():
    time.sleep(random.randint(2, 6))  # simulate latency
    return "Slow response simulated"

@app.route("/error")
def error():
    raise Exception("Simulated application error")

@app.route("/env")
def env():
    # fails if ENV_VAR is missing
    value = os.environ["DEMO_ENV_VAR"]
    return f"ENV_VAR value: {value}"

if __name__ == "__main__":
    app.run()
