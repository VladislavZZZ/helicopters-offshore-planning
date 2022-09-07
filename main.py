import os
import configparser

from utils.custom import load_res, init_installations, init_helicopters

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")


if __name__ == '__main__':
    CONFIG = configparser.ConfigParser()
    CONFIG.read(CONFIG_PATH)

    installations = load_res(CONFIG["installations"]["resource_path"])
    helicopters = load_res(CONFIG["helicopters"]["resource_path"])
    inst = init_installations(installations)
    helic = init_helicopters(helicopters)

    print("dpne")
