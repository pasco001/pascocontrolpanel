from pasco import PASCOBLEDevice
from pasco import CodeNodeDevice, Icons
import threading
import time

#Flag variable to control the thread
terminate_thread_flag = False

def keep_scanning():
    global scanned_sensors
    global terminate_thread_flag

    while not terminate_thread_flag:
        #print("Here")
        scanned_sensors = mysensor.scan()
        #print("inside", scanned_sensors)

def scanned_sensors_list():
    return scanned_sensors

def display_scanned_sensors():
    for i,sensor in enumerate(scanned_sensors, start=1):
        name_and_number = sensor_name_and_number(sensor)
        print(f'{i}:{name_and_number}')

def sensor_name_and_number(sensor:PASCOBLEDevice)->str:
    return sensor.name.split('>')[0]

def main():
    global mysensor
    global scanned_sensors

    scanned_sensors = []
    mysensor = PASCOBLEDevice()

    #print("first:", scanned_sensors)

    scanning_thread = threading.Thread(target=keep_scanning)
    scanning_thread.start()

    while True:
        display_scanned_sensors()
        time.sleep(1)

        user_select = input("")        




if __name__ == "__main__":
    main()
