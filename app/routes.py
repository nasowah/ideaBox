from flask import Flask, request, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ideaBox'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    defining a function to connect to a mysql db and performing a login.
    '''

    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.get_db().cursor()
    data = cursor.execute(
        "select * from ideaBox.User where username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()

    if data is None:
        return "Username or Password is wrong"
    else:
        return render_template('login.html')

    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
