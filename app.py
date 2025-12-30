from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def chataluna_chat():
    return render_template('chat.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

#38.50