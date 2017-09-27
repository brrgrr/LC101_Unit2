from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

title_mod = ''


@app.route("/")
def index():
    title_mod = 'Hello Form'
    return render_template(
        'hello_form.html',
        title_mod=title_mod
    )


@app.route("/hello", methods=['POST'])
def hello():
    title_mod = 'Hello Greeting'
    first_name = request.form['first_name']
    return render_template(
        'hello_greeting.html',
        title_mod=title_mod,
        name=first_name
    )


tasks = []


@app.route('/todos', methods=['POST', 'GET'])
def todos():
    title_mod = 'TODOs'

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template(
        'todos.html',
        title_mod=title_mod,
        tasks=tasks
    )


if __name__ == '__main__':
    app.run()
