#!/usr/bin/env python3

import re
import json
import time
import rospy
import paho.mqtt.client as mqtt
from geometry_msgs.msg import Twist

#client config
client = mqtt.Client()
arduino_cmd_vel = Twist()
client.connect("localhost", 1883, 60)

#Publish joystick message from ROS to MQTT
def callback(data):

    joystick_cmd_vel = {
            "x":data.linear.x,
            "z":data.angular.z
        }
    rospy.loginfo("sending joystick command velocity to arduino from ros to mqtt:")
    rospy.loginfo(joystick_cmd_vel)
    client.publish("ros_mqtt/cmd_vel", json.dumps(joystick_cmd_vel))

#Deserialize arduino data from MQTT
def deserialize(data):

    data = str(data.payload.decode("utf-8"))
    regex = '\d+'
    match = re.findall(regex, data)
    arduino_cmd_vel.linear.x = match[0]
    arduino_cmd_vel.angular.z = match[1]

#Receive Message from MQTT
def on_message(client, userdata, message):

    deserialize(message)
    rospy.loginfo("received arduino cmd velocity from mqtt to ros:")
    rospy.loginfo(arduino_cmd_vel)

#Create node for MQTT_bridge
def mqtt_bridge():

    #create mode for MQTT bridge
    rospy.init_node('mqtt_bridge', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, callback)

    #Mqtt Subscribtion
    client.loop_start()
    client.subscribe("mqtt_ros/receive_arduino_msg")
    client.on_message=on_message
    time.sleep(30)
    client.loop_stop()
    rospy.spin()

if __name__ == '__main__':
    mqtt_bridge()

                                                       
