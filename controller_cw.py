#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	try:
		pub = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
		rospy.init_node('controller_lab3_cw')

		#@TODO : set the rate of publishing the command velocities
		rate = rospy.Rate(20) #example:20hz
		count=0

		while not rospy.is_shutdown():

			v_cmd =0 # Command linear velocity
			omega_cmd = 0	# Command angular velocity     			

                        #TODO : determine v_cmd and omega_cmd for the desired 
                        ############## WRITE YOUR CODE BELOW #####################
                        count=count+1
                        time=float(count/20)
                        if time<5: 
                            v_cmd =0.2
                        elif time<6:
                            omega_cmd=-1.3
                            v_cmd=0
                        elif time<11:
                            v_cmd=0.2
                            omega_cmd=0
                        elif time<12:
                            omega_cmd=-1.5
                            v_cmd=0
                        elif time<17:
                            v_cmd=0.2
                            omega_cmd=0
                        elif time<17.5:
                            omega_cmd=-1.5
                            v_cmd=0
                        elif time<23:
                            v_cmd=0.2
                            omega_cmd=0
                        else:
                            omega_cmd=0
                            v_cmd=0

# 			v_cmd =0.2       # range:  [-0.25,0.25]
# 			omega_cmd = -0.5 # range : [-1.8,1.8]

			
			################ YOUR CODE ENDS HERE ########################
			vel_msg=Twist()
			vel_msg.linear.x  = v_cmd
			vel_msg.angular.z = omega_cmd

			print("v_cmd : % 2f, omega_cmd : % 5.2f" %(v_cmd, omega_cmd))
			pub.publish(vel_msg)
			rate.sleep()

	except rospy.ROSInterruptException:
		pass
