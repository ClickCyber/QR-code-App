from flask import Flask, render_template, request
from time import time
from lib.QR import makeQR, remove_later
import hashlib
app = Flask(__name__, template_folder='html')



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/setup-QR', methods=["POST"])
def QR_CODE():
    csrf = hashlib.sha256(str(time()).encode()).hexdigest()
    print(csrf)
    makeQR(request.form['link'], csrf, request.form['color'])
    remove_later(csrf)
    return render_template('index.html', qr_code=f'static/{csrf}.png', qr_link=request.form['link'])




if __name__ == '__main__':
    app.run(port=80)