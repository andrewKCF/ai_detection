import rospy
from vision_msgs.msg import Detection2D, Detection2DArray
from time import sleep
from gpiozero import LED
import time

led=LED(18)
start_time_=0
end_time_=0


def detect_info():
	led=LED(18)
	while True:
		led.on()
		sleep(1)
		led.off()
		sleep(1)

def detectCB(data):
	global start_time_
	global led
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	rospy.loginfo('%s',str(data.detections[0].results[0].id))
	rospy.loginfo('%s',str(data.detections[0].results[0].score))
	if (data.detections[0].results[0].score>0.5) and ((end_time_-start_time_)>5):
		start_time_ = time.time()
		print(start_time_)
		led.on()
		#sleep(1)
		#led.off()
		#sleep(1)		


if __name__=='__main__':
	rospy.init_node('ai_detecton')
	rospy.loginfo("hello")
	#rospy.Subscriber('/detectnet/detections',Detection2DArray,detectCB)
	while True:
		data = rospy.wait_for_message('/detectnet/detections',Detection2DArray)
		if  (data.detections[0].results[0].score>0.5) :
			led.on()
			sleep(1)
			led.off()
			sleep(1)

