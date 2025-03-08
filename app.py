import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '1422003'  # مفتاح سري لأمان الجلسات

# إعداد الاتصال بقاعدة البيانات
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  # تأكد أن كلمة المرور فارغة إذا لم تقم بتغييرها
    database='portfolio_db'
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

if __name__ == '__main__':
    app.run(debug=True)
