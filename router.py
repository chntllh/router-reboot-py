import sys
import os.path
import json
import router_1
import router_2
import router_3

def main():
    print("Wadacome")

    arguments = [int(arg) for arg in sys.argv[1:4]]

    if(not os.path.isfile('./config.json')):
        print("Config does not exist")
        return
    
    config_file = open('./config.json')
    config = json.load(config_file)
    config_file.close()

    for argument in arguments:
        if argument == 1:
            print("Rebooting main router")
            website = config["1"]["website"]
            username = config["1"]["username"]
            password = config["1"]["password"]
            router_1.reboot(website, username, password)
            print("Rebooted main router")
        elif argument == 2:
            print("Rebooting tenda router")
            website = config["2"]["website"]
            router_2.reboot(website)
            print("Rebooted tenda router")
        elif argument == 3:
            print("Rebooting tp-link router")
            website = config["3"]["website"]
            password = config["3"]["password"]
            router_3.reboot(website, password)
            print("Rebooted tp-link router")
        else:
            print("Not a valid argument")

if __name__ == "__main__":
    main()