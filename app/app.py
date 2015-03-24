from flask import Flask
from flask import request
from flaskext.mysql import MySQL

'''
Below are parameters for connecting to a MySQL DB
when using pip install Flask-MySQL
'''

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ideaBox'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def index_page():
    return 'Welcome to ideaBox!'


@app.route('/Authenticate', methods=['POST', 'GET'])
def authenticate():
    '''
    defining a function to connect to a mysql db and performing a login.
    '''
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.get_db().cursor()
    data = cursor.execute("select * from ideaBox.User where username='" + username + "' and password='" + password + "'")
    data = cursor.fetchone()
    
    if data is None:
        return "Username or Password is wrong"
    else:
        return "Logged in successfully"

    
if __name__ == '__main__':
    app.run(debug=True)
    
    