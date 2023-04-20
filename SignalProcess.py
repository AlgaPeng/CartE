# Function to parse the data in wifi_signals.txt
# and take the average of each line's wifi signals
import os
import time
locw = 0
loch = 0
cart1_loc = "Not sure where your cart is"

def find_cart(mac_address):
    w = 0
    h = 0
    loc = "Not sure where your cart is"
    if("94:B4:0F:E6:34" in mac_address):
        w = 10
        h = 500
        loc = "Phillips 238"

    elif("F0:5C:19:6E:74" in mac_address):
        w = 200
        h = 520
        loc = "Phillips 239"

    elif("F0:5C:19:6E:A0" in mac_address):
        w = 200
        h = 420
        loc = "Phillips 237"

    elif("94:B4:0F:E6:35" in mac_address):
        w = 30
        h = 100
        loc = "Phillips 200-1"

    elif("94:B4:0F:E6:45:C" in mac_address):
        w = 30
        h = 180
        loc = "Phillips 200-2"

    elif("94:B4:0F:E6:44:E" in mac_address):
        w = 300
        h = 230
        loc = "Phillips 200-3"

    elif("E8:26:89:37:9B" in mac_address):
        w = 5
        h = 100
        loc = "Phillips 203"

    elif("E8:26:89:37:DB" in mac_address):
        w = 5
        h = 250
        loc = "Phillips 219"

    elif("94:B4:0F:E6:45:E" in mac_address):
        w = 500
        h = 230
        loc = "Phillips 232"
    
    return w, h, loc

if (os.path.getsize('wifi_signals.txt') == 0):
        locw = 300
        loch = 20
        cart1_loc = "NOT SURE"
else:
    with open("wifi_signals.txt", 'r') as f:
        mac_list = []
        dB_list = []
        for line in f:

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
        # max_num = max(dB_list)
        # max_index = dB_list.index(max_num)
        # mac_address = mac_list[max_index]
        # print(mac_address)

        # record the current location
        with open("path_history.txt", "w") as f:
            for i in mac_list:
                curr_locw, curr_loch, curr_cart1_loc = find_cart(i)
                f.write("CART1 location: " + curr_cart1_loc + ", " + time.strftime('%l:%M%p %Z on %b %d, %Y'))
                f.write('\n')
        f.close()

        mac_address = mac_list[len(mac_list)-1]
        locw, loch, cart1_loc = find_cart(mac_address)

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
    with open ("./static/p2_map.html", "w") as out_f:
        tmp = template_f.read()
        tmp = tmp.replace("LOCW", str(locw))
        tmp = tmp.replace("LOCH", str(loch))
        out_f.write(tmp)
    out_f.close()
template_f.close()
