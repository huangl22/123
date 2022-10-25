from flask import Flask, request, render_template
import subprocess
import shlex
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_1.html')


@app.route('/action', methods=['POST'])
def do_action():
    ueip = request.form['ueip']
    teid = request.form['teid']
    address = request.form['address']
    dictionary = {"ueip": ueip, "teid": teid, "address": address}
    print(dictionary)
    
    #60.60.0.2 => 192.168.0.2
    if ueip == "192.168.0.2" and teid == "3":
        # outstr1 = "table_add tognb gtpu_encap " + ueip + " => " + teid + " 11.11.11.1 11.11.11.231\n"
        process.stdin.write(f"table_add tognb gtpu_encap {ueip} => {teid} 11.11.11.1 11.11.11.231\n".encode())
        process.stdin.flush()
        hint = process.stdout.readline().decode()
        print(hint)

        # outstr2 = "table_add toupf gtpu_decap 11.11.11.231 11.11.11.1 " + str(int(teid) * 2 - 1) + " " + ueip + " =>\n"
        teid = str(int(teid) * 2 - 1)
        process.stdin.write(f"table_add toupf gtpu_decap 11.11.11.231 11.11.11.1 {teid} {ueip} =>\n".encode())
        process.stdin.flush()
        hint = process.stdout.readline().decode()
        print(hint)

        # outstr3 = "table_add forarp arp_response " + ueip + " => " + ueip + "\n"
        process.stdin.write(f"table_add forarp arp_response {ueip} => {ueip}\n".encode())
        process.stdin.flush()
        hint = process.stdout.readline().decode()
        print(hint)
        return "success"
    return "drop"

if __name__ == "__main__":
    process = subprocess.Popen(shlex.split("python3 ~/0919-p4/behavioral-model/tools/runtime_CLI.py --thrift-port 9090"), stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    app.run(debug=True)
