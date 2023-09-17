from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'sql_injection_easy.db'  # Path to the shared schema file


# Initialize the database
def connect_db():
    return sqlite3.connect(DATABASE)



# Display the login page for the SQL Injection lab
@app.route('/sql_injection/easy')
def sql_injection_easy():
    return render_template('sql_injection_easy.html')


# Handle the login form for the SQL Injection lab
@app.route('/sql_injection/easy/login', methods=['POST'])
def sql_injection_easy_login():
    username = request.form['username']
    password = request.form['password']

    db = connect_db()

    # Simulate SQL injection vulnerability (DO NOT use this in a production environment)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    try:
        cursor = db.execute(query)
        user = cursor.fetchone()
        db.close()

        if user:
            return render_template('response.html', response='Login Successful')
        else:
            return render_template('response.html', response='Login Failed')

    except sqlite3.Error as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
