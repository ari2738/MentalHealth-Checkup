from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    score = 0

    score += int(request.form['q1'])
    score += int(request.form['q2'])
    score += int(request.form['q3'])
    score += int(request.form['q4'])
    score += int(request.form['q5'])

    if score <= 3:
        result = "You seem mentally healthy 😊"
    elif score <= 6:
        result = "Mild stress detected. Take care of yourself."
    else:
        result = "High stress level detected. Please consult a professional."

    return result

if __name__ == "__main__":
    app.run(debug=True)
