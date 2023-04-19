# Function to parse the data in wifi_signals.txt
# and take the average of each line's wifi signals
import os
import time
locw = 0
loch = 0
cart1_loc = "Not sure where your cart is"

if (os.path.getsize('wifi_signals.txt') == 0):
        locw = 300
        loch = 20
        cart1_loc = "NOT SURE"
else:
    with open("wifi_signals.txt", 'r') as f:
        mac_list = []
        dB_list = []
        for line in f:
            # average_strength = 0
            # idx = 0

            # find mac address
            index = line.find(" ")
            mac_list.append(line[:index-1])

            sub_line = line[index+1:]
            num = ""
            for n in sub_line:
                # make sure it is a number
                if(n != " "):
                    num = num + n
                else:
                    # each number is seperated by a space
                    dB_list.append(int(num))
                    num = ""
        max_num = max(dB_list)
        max_index = dB_list.index(max_num)
        mac_address = mac_list[max_index]
        print(mac_address)

        if("94:B4:0F:E6:5F" in mac_address):
            locw = 10
            loch = 500
            cart1_loc = "Phillips 238"

        elif("F0:5C:19:6E:74" in mac_address):
            locw = 200
            loch = 520
            cart1_loc = "Phillips 239"

        elif("F0:5C:19:6E:A0" in mac_address):
            locw = 200
            loch = 420
            cart1_loc = "Phillips 237"

        elif("94:B4:0F:E6:35" in mac_address):
            locw = 30
            loch = 100
            cart1_loc = "Phillips 200-1"

        elif("94:B4:0F:E6:45:C" in mac_address):
            locw = 30
            loch = 180
            cart1_loc = "Phillips 200-2"

        elif("94:B4:0F:E6:44:E" in mac_address):
            locw = 300
            loch = 230
            cart1_loc = "Phillips 200-3"

        elif("E8:26:89:37:9B" in mac_address):
            locw = 5
            loch = 100
            cart1_loc = "Phillips 203"

        elif("E8:26:89:37:DB" in mac_address):
            locw = 5
            loch = 250
            cart1_loc = "Phillips 219"

        elif("94:B4:0F:E6:45:E" in mac_address):
            locw = 500
            loch = 230
            cart1_loc = "Phillips 232"

# record the current location
with open("path_history.txt", "a") as f:
    f.write("CART1 location: " + cart1_loc + ", " + time.strftime('%l:%M%p %Z on %b %d, %Y'))
    f.write('\n')
f.close()
    
# overwrite html file location.html
with open("./static/location_template.html", "r") as template_f:
    with open ("./static/location.html", "w") as out_f:
        tmp = template_f.read()
        tmp = tmp.replace("CART1_LOC", '"' + cart1_loc + '"')
        out_f.write(tmp)
    out_f.close()
template_f.close()

# overwrite html file map.html
with open("./static/map_template.html", "r") as template_f:
    with open ("./static/map.html", "w") as out_f:
        tmp = template_f.read()
        tmp = tmp.replace("LOCW", str(locw))
        tmp = tmp.replace("LOCH", str(loch))
        out_f.write(tmp)
    out_f.close()
template_f.close()