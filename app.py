from flask import Flask, render_template

app = Flask(__name__)
# المسار الرئيسي (Home)
@app.route('/')
def home():
    return render_template('index.html')

# نقطة دخول التطبيق
if __name__ == '__main__':
    app.run(debug=True)
