#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

if __name__ == '__main__':
	try:
		pub = rospy.Publisher('/cmd_vel', Twist, queue_size=100)
		rospy.init_node('controller_lab3_cw')

		#@TODO : set the rate of publishing the command velocities
		rate = rospy.Rate(20) #example:20hz
		count=0
        #dt=0
    

		while not rospy.is_shutdown():
			v_cmd =0 # Command linear velocity
			omega_cmd = 0	# Command angular velocity 
    			

                        #TODO : determine v_cmd and omega_cmd for the desired 
                        ############## WRITE YOUR CODE BELOW ####################
                        count=count+1
                        
                        time=float(count/20)
                        if time<=2.5: 
                            v_cmd =0.2041
                            omega_cmd=0.0414
                        elif time>2.5 and time<=3.95:
                            omega_cmd=0.9183
                            v_cmd=0.0003
                        elif time>3.9 and time<=6.8:
                            v_cmd=0.2041
                            omega_cmd=0.0414
                        elif time>6.8 and time<=8:
                            omega_cmd=0.9183
                            v_cmd=0.0003
                        elif time>7.9 and time<=10:
                            v_cmd=0.2041
                            omega_cmd=0.0414
                        elif time>10 and time<=12:
                            omega_cmd=0.9183
                            v_cmd=0.0003
                        elif time>11.72 and time<=14.4:
                            v_cmd=0.2041
                            omega_cmd=0.0003
                        else:
                            omega_cmd=0
                            v_cmd=0
                
               
                   
			#omega_cmd =-0.5 # range : [-1.8,1.8]
            

			
			################ YOUR CODE ENDS HERE ########################
			vel_msg=Twist()
			vel_msg.linear.x  = v_cmd
			vel_msg.angular.z = omega_cmd

			print("v_cmd : % 2f, omega_cmd : % 5.2f" %(v_cmd, omega_cmd))
			pub.publish(vel_msg)
			rate.sleep()

	except rospy.ROSInterruptException:
		pass
