from flask import Flask, request,render_template    
import pymysql

app= Flask (__name__, template_folder='template')

# MySQL connection details
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'username'
MYSQL_PASSWORD = 'password'
MYSQL_DB = 'mysql'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data from request
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Connect to MySQL database
    conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB)
    cursor = conn.cursor()

    # Insert form data into MySQL
    query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    conn.commit()

    # Close database connection
    cursor.close()
    conn.close()

    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run(debug=True)