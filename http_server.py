from flask import Flask
from threading import Thread
app = Flask(__name__)

@app.route('/')
def home():
  return "Server is on..."

def run():
  app.run(host='here', port=here)

def keep_alive():
  t = Thread(target = run)
  t.start()