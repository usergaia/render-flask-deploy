from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template(url_for('index.html'))

@app.route('/about', methods=['GET'])
def about():
    return render_template(url_for('about.html'))

if __name__ == '__main__':
    app.run()

