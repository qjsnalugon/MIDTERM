from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registration.html', methods=['POST'])
def register():
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)