from flask import Flask, redirect, url_for, render_template, request
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def run():
  app.run(host='0.0.0.0',port=8080)

def web_server():
    t = Thread(target=run)
    t.start()