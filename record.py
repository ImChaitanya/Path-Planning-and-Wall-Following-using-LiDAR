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
	
	def path_callback(self,ar_msg):
		i=0
		recorder.v_c = ar_msg.linear.x
		recorder.w_c = ar_msg.angular.z

	def top2csv(self):
		rospy.init_node('record')
		rate = rospy.Rate(100) # 10hz
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
		file_path = 'C:\catkin_ws' +"\Vel_Omega.csv"
		f = open(file_path, "w")
		temp = ['V_actual','OMEGA_actual', 'V_ref','OMEGA_ref']
		writer = csv.writer(f)
		writer.writerow(temp)
		while not rospy.is_shutdown():
			temp = [recorder.vs,recorder.ws,recorder.v_c,recorder.w_c]
			writer.writerow(temp)
			rate.sleep()
		f.close()

if __name__ == '__main__':

	try:
		rec = recorder()
		rospy.Subscriber('/odom',Odometry,rec.odometrycallback)
		rospy.Subscriber('/cmd_vel',Twist,rec.path_callback)
		rec.top2csv()
	except rospy.ROSInterruptException:
		pass
