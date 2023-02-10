#!/usr/bin/env python
import rospy
import math
import numpy as np
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import Float64MultiArray
import tf_conversions
from std_msgs.msg import Float32
import pandas as pd 
import csv 

class recorder:
  
  xs   = 0
  ys   = 0
  vs   = 0
  ws   = 0
  yaw  = 0
  ref_path =[]
    
  def odometrycallback(self, msg):

        recorder.xs = msg.pose.pose.position.x
        recorder.ys = msg.pose.pose.position.y	
	recorder.vs = np.sqrt( (msg.twist.twist.linear.y)**2 + (msg.twist.twist.linear.x)**2 )
	recorder.ws = msg.twist.twist.angular.z
	quaternion = (
    		msg.pose.pose.orientation.x,
    		msg.pose.pose.orientation.y,
    		msg.pose.pose.orientation.z,
    		msg.pose.pose.orientation.w)
	euler = tf_conversions.transformations.euler_from_quaternion(quaternion)
	recorder.yaw = euler[2]
	
  def path_callback(self,ar_msg):
	i=0
        recorder.path=[]
	for x in ar_msg.data : 
        	recorder.path.append(x)
  def velocity(self):
        rospy.init_node('record_cw')
        rate = rospy.Rate(100) # 10hz
	pi  = np.pi
	dt = 0.012
        #file = open("path_cw.csv","w")

	with open('path_cw.csv','a') as f:
	        writer=csv.writer(f)

        while not rospy.is_shutdown():
		temp = np.array([recorder.xs,recorder.ys,recorder.yaw,recorder.vs,recorder.ws])         
		writer.writerow(str(temp))
		print(temp)
		rate.sleep() 
        f.close()  

if __name__ == '__main__': 
        
        try:         
	 rec = recorder()
	 rospy.Subscriber('/odom',Odometry,rec.odometrycallback)
    	 rospy.Subscriber('/ref_array',Float64MultiArray,rec.path_callback)
	 rec.velocity()
          	
        except rospy.ROSInterruptException:
          pass





    
