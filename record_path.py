#!/usr/bin/env python
# license removed for brevity
import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float32
import csv
import os

class recorder:
  
	xs   = 0
	ys   = 0
	yaw  = 0
	vs   = 0
	ws   = 0
	v_c  = 0
	w_c  = 0
	path =np.zeros(5)
	
	def odometrycallback(self, msg):

		recorder.xs = msg.pose.pose.position.x
		recorder.ys = msg.pose.pose.position.y
		recorder.vs = np.sqrt(msg.twist.twist.linear.x**2 + msg.twist.twist.linear.y**2)
		recorder.ws = msg.twist.twist.angular.z	

	def top2csv(self):
		rospy.init_node('record_path')
		rate = rospy.Rate(100) # 10hz
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
		file_path = 'C:\catkin_ws' +"\path.csv"
		f = open(file_path, "w")
		temp = ['X','Y']
		writer = csv.writer(f)
		writer.writerow(temp)
		while not rospy.is_shutdown():
			temp = [recorder.xs,recorder.ys]
			writer.writerow(temp)
			rate.sleep()
		f.close()

if __name__ == '__main__':
	try:
		rec = recorder()
		rospy.Subscriber('/odom',Odometry,rec.odometrycallback)
		print("Saving data")
		rec.top2csv()

	except rospy.ROSInterruptException:
		pass
