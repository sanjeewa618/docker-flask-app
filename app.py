from flask import Flask
from config import Config
from models import db, Task
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

 
with app.app_context():
    for i in range(10):
        try:
            db.create_all()
            print("✅ Database connected and tables created.")
            break
        except OperationalError:
            print("⏳ Waiting for PostgreSQL...")
            time.sleep(2)

@app.route("/")
def home():
    tasks = Task.query.all()

    if not tasks:
        return "<h2>No Tasks Found</h2>"

    output = "<h1>Task List</h1><ul>"

    for task in tasks:
        output += f"<li>{task.title}</li>"

    output += "</ul>"

    return output

@app.route("/add/<title>")
def add_task(title):
    task = Task(title=title)
    db.session.add(task)
    db.session.commit()

    return f"Task '{title}' Added Successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)