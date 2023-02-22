#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist

class Test():
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    def pub_z(self):
        
        angle = 90.0 #deg目的の角度
        speed = 20 #deg/s目的の速度
        cost_time = angle / speed # [s]
        
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = speed * 3.1415 / 180.0 #rad
        print(angle)

        start_time = time.time()
        end_time = time.time()

        # cost_time を越えるまで走行
        rate = rospy.Rate(50)
        while end_time - start_time <= cost_time:
            self.pub.publish(twist)
            end_time = time.time()
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('tcmdvel_publisher')
    test = Test()
    test.pub_z()
