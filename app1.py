from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def device():
    return render_template('device.html')

@app.route('/iphone')
def iphone():
    return render_template('iphone.html')

@app.route('/imac')
def imac():
    return render_template('imac.html')

@app.route('/ipad')
def ipad():
    return render_template('ipad.html')

if __name__ == '__main__':
    app.run(debug=True)
