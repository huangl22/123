from flask import Flask, redirect, url_for, request, render_template, make_response, session
import config
import os

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'
@app.route('/')
# def index():
#     return render_template
def index():
    return render_template('index_1.html')

@app.route('/action', methods = ['POST'])
def do_action():
    ueip = request.form['ueip']
    teid = request.form['teid']
    address = request.form['address']
    dictionary = {"ueip":ueip, "teid":teid, "address":address}

    if ueip == "60.60.0.2" and teid == "3":
        outstr1 = "table_add tognb gtpu_encap " + ueip + " => " + int(teid) + " 11.11.11.1 11.11.11.231\n"
        os.popen(outstr1)
        outstr2 = "table_add toupf gtpu_decap 11.11.11.231 11.11.11.1 " + int(teid)*2-1 + " " + ueip + " =>\n"
        os.popen(outstr2)
        outstr3 = "table_add forarp arp_response " + ueip + " => " + ueip + "\n"
        os.popen(outstr3)
if __name__== "__main__":
    app.run(debug=True)
