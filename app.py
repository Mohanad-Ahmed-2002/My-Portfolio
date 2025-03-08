import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os

# تحميل متغيرات البيئة من ملف .env
load_dotenv()


app = Flask(__name__)
app.secret_key = '1422003'  # مفتاح سري لأمان الجلسات

# إعداد الاتصال بقاعدة البيانات
db = mysql.connector.connect(
    host=os.getenv("CC_DB_HOST"),
    user=os.getenv("CC_DB_USER"),
    password=os.getenv("CC_DB_PASSWORD"),
    database=os.getenv("CC_DB_NAME")
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

# Vercel تحتاج إلى استدعاء متغير التطبيق مباشرة
app = app


