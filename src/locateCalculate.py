import math

# listener_custom에서 사용할 callback 함수


def cal_callback(msg):
    CalLocate(msg)


def getMsg(msg):
    print("====================")
    for i in range(360):
        length = msg.ranges[i]
        if(length != 0 and length < 12):
            degree = math.degrees(msg.angle_min + msg.angle_increment*i)
            length = msg.ranges[i]
            print("angles : " + str(degree) + " ranges : " + str(length))


def CalLocate(msg):
    print("=====================")
    for i in range(360):
        degree = math.degrees(msg.angle_min + msg.angle_increment*i)
        rad = msg.angle_min + msg.angle_increment*i
        length = msg.ranges[i]
        Locate_x = 0
        Locate_y = 0
        # print("degree : " + str(degree) + "length : " + str(length))
        if(length != 0 and length < 12):
            Locate_x = length*math.cos(rad)
            Locate_y = length*math.sin(rad)

            print("Angle :", round(degree, 2), "Length :", round(length, 3), "x 좌표 :", round(Locate_x, 3), "y 좌표 :",
                  round(Locate_y, 3))
