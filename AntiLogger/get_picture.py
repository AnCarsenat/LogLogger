
import cv2
import time, os


def init(cam_port = 0):
    cam = cv2.VideoCapture(cam_port)
    return(cam)
    
def get_pic(cam):
    result, image = cam.read() 
    current_date_time=time.strftime("%Y-%m-%d %H-%M", time.gmtime())
    if result: 
        cv2.imwrite(str((f'images/{current_date_time}.png')), image) 
    else: 
        print("No image detected. Please! try again") 


