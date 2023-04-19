from flask import Flask, request
import os

# app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='')

# @app.route("/")
# def checklive():
#     return "owendpersonal.com is live"

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if(request.method == 'POST'):
        store_signals(request.data)
        print(request.data)
        return "DATA Received"
    else:
        print("GET")
        return "GET data"

@app.route('/getLocation')
def galaxy():
    return app.send_static_file('first_page.html')

@app.route('/svg_map')
def refresh_map():
    os.system('python3 SignalProcess.py')
    return app.send_static_file('svg_map.html')

def store_signals(data):
    f = open("wifi_signals.txt", "w")
    data_string = data.decode("utf-8")
    mac_idx  = 0
    dB_idx   = 0
    mac_list = ["94:B4:0F:E6:35", "94:B4:0F:E6:45:C", "94:B4:0F:E6:44:E",
     "E8:26:89:37:9B", "E8:26:89:37:DB", "94:B4:0F:E6:45:E", "F0:5C:19:6E:A0",
     "94:B4:0F:E6:5F", "F0:5C:19:6E:74"]
    # Find mac and dB for each signal
    while(mac_idx >= 0 and dB_idx >= 0):
        mac_idx = data_string.find('MAC:')
        mac_address = data_string[mac_idx+len("MAC:"):mac_idx+len("MAC:")+16]
        data_string = data_string[mac_idx+len("MAC:")+16:]
        f.write(mac_address+" ")
        dB_idx = data_string.find('dB:')
        dB_string = data_string[dB_idx+len("dB:"):dB_idx+len("dB:")+3]
        if(dB_string == "100"):
            f.write(dB_string + " ")
        else:
            f.write(data_string[dB_idx+len("dB:"):dB_idx+len("dB:")+2] + " ")
        data_string = data_string[dB_idx+len("dB:")+2:]
        mac_idx = data_string.find('MAC:')
        f.write('\n')
    f.close()

if __name__ == '__main__':
    open('wifi_signals.txt', 'w').close()
    app.run(threaded=True, host='0.0.0.0', port=80)