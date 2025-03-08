import os
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('1422003')

# إعداد الاتصال بقاعدة البيانات
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=3306
)

# المسار الرئيسي (Home)
@app.route('/')
def home():
    return render_template('index.html')

# مسار صفحة "About"
@app.route('/about')
def about():
    return render_template('about.html')

# مسار صفحة "Contact"
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message)
        )
        db.commit()

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

# نقطة دخول التطبيق
if __name__ == '__main__':
    app.run(debug=True)


