import math

# listener_custom에서 사용할 callback 함수
def cal_callback(msg):
    printScan(msg)

def printScan(msg):
    for i in range(360):
        x = msg.ranges[i]
        degree = math.degrees(msg.angle_min + msg.angle_increment*i)
        if(x != 0):
            print("angle : " + str(degree) + "range : " + str(x))
