from flask import Flask, render_template

app = Flask(__name__)

# BASE ROUTE = '/'
@app.route('/')
def landingPage():
    return 'Pizza parlor dashboard: under construction go to "/dashboard"'

@app.route('/dashboard')
def dashboard():
    friend = 'Jane Pancakes'
    friends = ['Eric', 'Joshua', 'Dante', 'Kevni', 'Liz', 'John']
    return render_template('dashboard.html', friend1 = friend, friends = friends )

if __name__ == '__main__':
    app.run(debug=True)