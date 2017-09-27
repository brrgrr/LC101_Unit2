from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

title = ''


@app.route("/")
def index():
    title = 'Hello Form'
    return render_template(
        'hello_form.html',
        title=title
    )


@app.route("/hello", methods=['POST'])
def hello():
    title = 'Hello Greeting'
    first_name = request.form['first_name']
    return render_template(
        'hello_greeting.html',
        title=title,
        name=first_name
    )


tasks = []


@app.route('/todos', methods=['POST', 'GET'])
def todos():
    title = 'TODOs'

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template(
        'todos.html',
        title=title,
        tasks=tasks
    )


if __name__ == '__main__':
    app.run()
