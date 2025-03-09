import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# الاتصال بقاعدة البيانات باستخدام المتغيرات البيئية
db = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME")
)

# المسار الرئيسي (Home)
@app.route('/')
def home():
    return render_template('index.html')

# # مسار صفحة "About"
# @app.route('/about')
# def about():
#     return render_template('about.html')

# مسار صفحة "Contact"
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor = db.cursor()

        # التحقق من وجود البريد الإلكتروني مسبقًا
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('This email is already registered!', 'warning')
        else:
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
