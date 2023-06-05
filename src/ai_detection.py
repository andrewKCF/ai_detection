import rospy
from vision_msgs.msg import Detection2D, Detection2DArray
from time import sleep
from gpiozero import LED
import time

led=LED(18)

if __name__=='__main__':
	rospy.init_node('ai_detecton')
	rospy.loginfo("hello")
	#rospy.Subscriber('/detectnet/detections',Detection2DArray,detectCB)
	while True:
		data = rospy.wait_for_message('/detectnet/detections',Detection2DArray)
		#if  (data.detections[0].results[0].score>0.5) :
		led.on()
		sleep(1)
		led.off()
		sleep(0.5)

