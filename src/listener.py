#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import locateCalculate

def listener():
    rospy.init_node('listener', anonymous=True)
    # rospy.Subscriber('scan', LaserScan, callback)
    rospy.Subscriber('scan', LaserScan, locateCalculate.cal_callback)
    # rospy.Subscriber('scan', LaserScan, locateCalculate.cal_callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
