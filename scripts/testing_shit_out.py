#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import message_filters

rospy.init_node("lol_node")

class my_class:
    def __init__(self):
        self.odom = Odometry()
        self.imu = Imu()
        self.subs_odom = message_filters.Subscriber("/odom", Odometry)
        self.subs_imu = message_filters.Subscriber("/imu", Imu)
        self.ts = message_filters.TimeSynchronizer([self.subs_odom, self.subs_imu], 10)
        self.ts.registerCallback(self.callback_func)
    def callback_func(self, message1, message2):
        self.odom = message1
        self.imu = message2

my_obj = my_class()
publisher = rospy.Publisher("/lol_topic", Odometry, queue_size = 1)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
        publisher.publish(my_obj.odom)
        rate.sleep()

