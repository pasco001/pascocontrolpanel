from pasco import PASCOBLEDevice
from pasco import CodeNodeDevice, Icons
import threading

'''
GLOBAL VARIABLE
'''
mysensor = PASCOBLEDevice()
global scanned_sensors
scanned_sensors = []

'''
SCAN PASCO SENSORS
'''

'''
Keep scanning for sensors
'''

def scan_sensors():
    while True:
        scanned_sensors = mysensor.scan()
        print("inside scan_sensors()")
        print(scanned_sensors)


'''
Returns the serial number of the PASCO sensor object
'''
def get_serial_number(pasco_sensor:PASCOBLEDevice) -> str:
    serial_number = pasco_sensor.name.split('>')[0].split()[1]
    return serial_number


'''
Returns the sensor type of the PASCO sensor object
'''
def get_sensor_type(pasco_sensor:PASCOBLEDevice) -> str:
    sensor_type = pasco_sensor.name.split('>')[0].split()[0]
    return sensor_type

'''
Scans PASCO sensors and returns a list of the detected PASCO sensors.
'''
def scan_sensors() -> list[PASCOBLEDevice]:
    pasco_sensor = PASCOBLEDevice()
    scanned_sensors = pasco_sensor.scan()
    return scanned_sensors

'''
Check if the selected sensors are contained in the scanned sensors and
returns a list of matching sensors
'''
def selected_in_detected(selected_sensors:[str], scanned_sensors:[PASCOBLEDevice]) -> [PASCOBLEDevice]:
    matching = []
    if scanned_sensors != [] and selected_sensors != []:
        for sensor in scanned_sensors:
            serial_number = get_serial_number(sensor)
            if serial_number in selected_sensors:
                matching.append(sensor)
    return matching

'''
Scan sensors until the user inputs selected sensors and the selected sensors
match the the scanned sensors
'''
def scan_until_selection(selected_sensors:[str]) -> [PASCOBLEDevice]:
    while True:
        scanned_sensors = scan_sensors()
        #print("스캔 : ", scanned_sensors)
        matching = selected_in_detected(selected_sensors, scanned_sensors)
        #print("매칭 : ", matching)
        if matching != [] and len(matching) == len(selected_sensors):
            #print("사용 : ", matching)
            return matching 
    

'''
CONNECT TO SENSOR
'''        

def read_sensor_data(using_sensors:[PASCOBLEDevice]) -> None:
    if len(using_sensors) == 1:
        current_sensor = using_sensors[0]
        serial_number = get_serial_number(current_sensor)
        sensor_type = get_sensor_type(current_sensor)
        current_sensor.connect_by_id(serial_number)
        for i in range(100):
            current_value = current_sensor.read_data(sensor_type)
            print(current_value)
        current_sensor.disconnect()

'''
HELPER FUNCTIONS
'''

'''
Prints the detected PASCO sensors
'''
def print_detected_sensors(detected_sensors : list[PASCOBLEDevice]):
    print('\nDevices Found')
    for i, ble_device in enumerate(detected_sensors):
        display_name = ble_device.name.split('>')
        print(f'{i}: {display_name[0]}')
        serial_number = get_serial_number(ble_device)

def main():
    '''
    scanning_thread = threading.Thread(target=scan_sensors())
    scanning_thread.start()
    '''
    scan_sensors()



if __name__ == "__main__":

    '''
    using_sensors = scan_until_selection(["472-582"])
    print(using_sensors)
    read_sensor_data(using_sensors)
    '''
    main()