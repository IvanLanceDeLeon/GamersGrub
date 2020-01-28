from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/games')
def games():
    return render_template('games.html')
if __name__ == "__main__":
    app.run(debug=True,host="192.168.0.16", port="33")