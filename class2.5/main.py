from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

title_mod = ''


@app.route('/validate-time')
def display_time_form():
    title_mod = 'Validate Time'
    return render_template(
        'form.html',
        title_mod=title_mod,
        hours='',
        hours_error='',
        minutes='',
        minutes_error=''
    )


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
        time = str(hours) + ':' + str(minutes)
        return redirect('valid-time?time={0}'.format(time))
    else:
        return render_template(
            'form.html',
            title_mod=title_mod,
            hours=hours,
            hours_error=hours_error, minutes=minutes,
            minutes_error=minutes_error
        )


@app.route('/valid-time')
def valid_time():
    title_mod = 'Validated Time'
    time = request.args.get('time')
    return render_template(
        'valid.html',
        title_mod=title_mod,
        time=time)


if __name__ == '__main__':
    app.run()
