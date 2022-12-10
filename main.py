import os
import random


def create_mask_mac():
    init_mac = ["0", "8", "0", "0", "2", "7"]
    characters = ["a", "b", "c", "d", "e", "f"]
    number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # new mask mac
    mac = init_mac[:]
    for char in range (3):
        segment_1 = random.choice(characters)
        segment_2 = random.choice(number)
        segment = segment_1 + segment_2
        mac += segment

    # format mac xx:xx:xx:xx:xx:xx
    str_mac = ""
    for seg in mac:
        str_mac += seg

    new_mac = ""
    i=0
    while(i < len(str_mac)):
        if i & 1 == 1:
            new_mac += str_mac[i]
            new_mac += ":"
            i=i+1
        else:
            new_mac += str_mac[i]
            i=i+1

    new_mac = new_mac[:17]
    return new_mac



def run():
    new_mac = create_mask_mac()
    network = input("Network interface-> ") # chosee interface network
    try:
        while True:
            # down interface network
            command_down_interface = "ifconfig {} down".format(network)
            os.popen(command_down_interface)

            # command for change mac
            command_change_mac = "macchanger --mac={} {}".format(new_mac, network)
            os.popen(command_change_mac)

            # up interface network
            command_up_interface = "ifconfig {} up".format(network)
            os.popen(command_up_interface)

    except Exception as error:
        print(str(error))
        

if __name__ == '__main__':
    run()
