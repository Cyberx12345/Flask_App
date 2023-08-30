from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/contact')
def contact_us():
    return render_template('navigate.html')


@app.errorhandler(404)
def error_page(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True )
