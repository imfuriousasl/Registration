from flask import Flask, render_template, request
import sqlite3
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    full_name = request.form['full_name']
    age = request.form['age']
    phone = request.form['phone']
    address = request.form['address']
    weeks_pregnant = request.form['weeks_pregnant']
    expected_delivery = request.form['expected_delivery']
    registration_date = date.today().strftime('%Y-%m-%d')
    notes = request.form['notes']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO mothers 
                   (
                   full_name,
                    age,
                    phone,
                    address,
                    weeks_pregnant,
                    expected_delivery,
                    registration_date,
                    notes
                   )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',

                   (
                    full_name,
                    age,
                    phone,
                    address, 
                    weeks_pregnant, 
                    expected_delivery, 
                    registration_date, 
                    notes
                    ))
    conn.commit()
    conn.close()
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
