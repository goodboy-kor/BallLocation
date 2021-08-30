import math

# listener_custom에서 사용할 callback 함수


def cal_callback(msg):
    # getMsg(msg)
    calLocate(msg)


# 기본 함수 angle과 거리 출력
def getMsg(msg):
    print("====================")
    for i in range(360):
        distance = msg.ranges[i]
        if(distance != 0 and distance < 12):
            degree = math.degrees(msg.angle_min + msg.angle_increment*i)
            distance = msg.ranges[i]
            print(f"angles : {str(degree)} ranges : {str(distance)}")

# x좌표, y좌표 출력
def calLocate(msg):
    print("=====================")
    for i in range(360):
        degree = math.degrees(msg.angle_min + msg.angle_increment*i)
        rad = msg.angle_min + msg.angle_increment*i
        dist = msg.ranges[i]
        locate_x = 0
        locate_y = 0
        # print("degree : " + str(degree) + "distance : " + str(distance))
        if(dist != 0 and dist < 12):
            locate_x = dist*math.cos(rad)
            locate_y = dist*math.sin(rad)

            print("Angle :", round(degree, 2), "distance :", round(dist, 2), "x 좌표 :", round(locate_x, 2), "y 좌표 :",
                  round(locate_y, 2))
