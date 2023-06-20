import tkinter as tk
import tkinter.font as tkfont

'''
GLOBAL VARIABLES
'''

root = tk.Tk()

root.title("PASCO")

'''
윈도우 사이즈
'''

wsize = 400
hsize = 600

root.geometry(f'{wsize}x{hsize}')

'''
root.width = wsize
root.height = hsize
'''

'''
제어판 제목
'''
title_str = "IOT 센서 데이터 연동 설정 제어판"
title_label = tk.Label(root, text= title_str, font=("맑은 고딕", 12, "bold"))
title_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)

'''
모둠 아이디 - 새로운 프레임 안에 만들어서 그룹하기 
'''
mid_frame = tk.Frame(root,width=wsize,height=200, bg="lightgray")

mid_str = "모둠 아이디 입력"
mid_label = tk.Label(mid_frame, text=mid_str)
mid_label.grid(row=0, column=0, sticky=tk.W)

mid_input_var = tk.StringVar()
mid_entry = tk.Entry(mid_frame, textvariable=mid_input_var)

#This function is called whenever the user clicks the button
#It retrieves the data inside the entry
#mid_input_var is the text inside entry
def check_connection():
    mid_input = mid_input_var.get()
    '''
    여기서 API 연결 확인하기
    '''
    global connect_popup
    connect_popup = tk.Toplevel(root)
    connect_popup.title("모둠 아이디 확인")
    connect_popup.geometry("100x100")
    connect_popup.config(bg="white")

    '''
    API와 잘 연결 상태에 따라 메세지 보여주기
    '''

    api_connected = True

    connected_label = tk.Label(connect_popup)
    if api_connected:
        #connected_label = tk.Label(connect_popup, text="연결 되었습니다")
        connected_label.config(text="연결 되었습니다!")
    else:
        #notconnected_label = tk.Label(connect_popup, text="문제가 발생했습니다. 다시 시도해 주세요.")
        connected_label.config(text="문제가 발생했습니다. 다시 시도해 주세요")
    connected_label.pack()

    #닫기 버튼
    close_button = tk.Button(connect_popup, text="닫기", command=connect_popup.destroy)
    close_button.pack()

    print(f"input text: {mid_input}")

mid_button = tk.Button(mid_frame, text="모둠 아이디 확인하기", command=check_connection)

mid_entry.grid(row=0, column=1)
mid_button.grid(row=0, column=2)

mid_detail_str = "지능형 과학실 ON의 모든 번호를 복사해서 붙여 넣은 후 모듬 번호 확인하기 버튼을 클릭하세요"
mid_detail_label = tk.Label(mid_frame, text=mid_detail_str)
mid_detail_label.grid(row=1, column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W)

mid_frame.grid(row=1, column=0)

'''
센서 연결
'''
sensor_popup = None

#센서 연결하는 함수
def connect_sensors(sensor_checkboxes):
    for sensor in sensor_checkboxes:
        is_selected = sensor_checkboxes[sensor].get()
        
            


#센서 스캔하는 팝업 만들기
def scan_sensors():
    global sensor_popup

    if sensor_popup is not None:
        sensor_popup.destroy()

    sensor_popup = tk.Toplevel(root)
    sensor_popup.title("센서 스캔하기")
    sensor_popup.geometry("200x400")

    sensor_list = ["sensor1", "sensor2"] #call scan function and get the sensors
    #Make checkboxes for each detected sensor
    sensor_checkboxes = {}
    for sensor in sensor_list:
        checkbox_var = tk.IntVar()
        #text has to be the type and the serial number of the sensor
        checkbox = tk.Checkbutton(sensor_popup, text=sensor, variable=checkbox_var)
        checkbox.deselect()
        checkbox.pack()
        sensor_checkboxes[sensor] = checkbox_var
    
    connect_button = tk.Button(sensor_popup, text="센서 연결하기", command=lambda: connect_sensors(sensor_checkboxes)) 
    connect_button.pack()

sensor_frame = tk.Frame(root, width=wsize, height=400, bg="lightgray")

sensor_label1_str = "탐구에 활용할 센서를 반드시 확인하세요"
sensor_label1 = tk.Label(sensor_frame, text=sensor_label1_str)
sensor_label1.pack()

scan_button = tk.Button(sensor_frame, text="센서 스캔하기", command=scan_sensors)
scan_button.pack()

#This will be the actual detected sensors




sensor_frame.grid(row=2, column=0)


root.mainloop()

