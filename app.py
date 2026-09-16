from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample tasks
tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "completed": False
    },
    {
        "id": 2,
        "title": "Create GitHub Actions workflow",
        "completed": False
    }
]


# Home page
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


# Add a new task
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")

    if title:
        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "completed": False
        }

        tasks.append(new_task)

    return redirect(url_for("home"))


# Complete / uncomplete a task
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break

    return redirect(url_for("home"))


# Delete a task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks

    tasks = [
        task
        for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("home"))


# Health-check endpoint
@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "DevOps Task Tracker"
    }, 200


# Start application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )