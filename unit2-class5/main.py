from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

time_form = '''
<style>
    .error {{ color: red; }}
</style>
<h1>Validate Time</h1>
<form method='POST'>
    <label>Hours (24-hour format)
        <input name='hours' type='text' value='{hours}' />
    </label>
    <p class='error'>{hours_error}</p>
    <label>Minutes
        <input name='minutes' type='text' value='{minutes}' />
    </label>
    <p class='error'>{minutes_error}</p>
    <input type='submit' value='Validate' />
</form>
'''


@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours < 0 or hours > 23:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes < 0 or minutes > 59:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not hours_error and not minutes_error:
        return 'Success!'
    else:
        return time_form.format(hours=hours, hours_error=hours_error, minutes=minutes, minutes_error=minutes_error)


if __name__ == '__main__':
    app.run()
