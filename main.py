import network
from machine import Pin, PWM
import socket
import time

# -------- Motor Right  --------
mR_ctrl_1 = Pin(13, Pin.OUT)
mR_ctrl_2 = Pin(12, Pin.OUT)
mR_pwm = PWM(Pin(27), freq=2000)

# -------- Motor Left --------
mL_ctrl_1 = Pin(32, Pin.OUT)
mL_ctrl_2 = Pin(33, Pin.OUT)
mL_pwm = PWM(Pin(26), freq=2000)
led_on = Pin(15, Pin.OUT)
led_back = Pin(4, Pin.OUT)

#---------Buzzer Config------
buzzer = Pin(2, Pin.OUT)
buzzer.value(0)

SPEED = 800

# -------- Motor Control Functions --------
def mR_forward():
    mR_ctrl_1.value(0)
    mR_ctrl_2.value(1)
    mR_pwm.duty(SPEED)

def mR_backward():
    mR_ctrl_1.value(1)
    mR_ctrl_2.value(0)
    mR_pwm.duty(SPEED)
    
def mR_stop():
    mR_ctrl_1.value(0)
    mR_ctrl_2.value(0)
    mR_pwm.duty(0)
    
def mL_forward():
    mL_ctrl_1.value(0)
    mL_ctrl_2.value(1)
    mL_pwm.duty(SPEED)
    
def mL_backward():
    mL_ctrl_1.value(1)
    mL_ctrl_2.value(0)
    mL_pwm.duty(SPEED)
    
def mL_stop():
    mL_ctrl_1.value(0)
    mL_ctrl_2.value(0)
    mL_pwm.duty(0)

# -------- Vehicle Control Functions --------
def forward():
    print("FORWARD")
    mR_forward()
    mL_forward()
    led_on.value(0)

def backward():
    print("BACKWARD")
    mR_backward()
    mL_backward()
    led_on.value(1)
    led_back.value(1)

def left():
    print("LEFT")
    mR_forward()
    mL_backward()
    led_on.value(0)

def right():
    print("RIGHT")
    mR_backward()
    mL_forward()
    led_on.value(0)

def stop():
    print("STOP")
    buzzer.value(0)
    mR_stop()
    mL_stop()
    led_on.value(0)
    led_back.value(0)
    
    
def sound():
    print("Sound")
    buzzer.value(1)
   

# -------- Web Server Setup --------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)

print("Web server started. Waiting for commands...")
stop()

# -------- Main Loop --------
while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        
        # Look for commands in the URL (e.g., /f, /b, /l, /r, /s)
        if '/f' in request:
            forward()
        elif '/b' in request:
            backward()
        elif '/l' in request:
            left()
        elif '/r' in request:
            right()
        elif '/so' in request:
            sound()
        elif '/s' in request:
            stop()

        # Send a basic response to the app/browser
        response = "HTTP/1.1 200 OK\nAccess-Control-Allow-Origin: *\n\nOK"
        conn.send(response)
        conn.close()
    except Exception as e:
        print("Error:", e)



