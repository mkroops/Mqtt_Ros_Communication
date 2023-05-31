# Open_scout_ROS

4. ROS
4.1. Understanding ROS
Initially I have studied what is ROS and why it is very helpful for robotics. It helps me to
understand why simulation is needed and why simulation of robot will help us to debug our
problem. It is open source platform and we can use packages to reduce time in building software
from scratch. Because of more robotics packages available in opensource, It will be helpful for
our open scout project to reduce time of building software from scratch if we extend this project
in future use. Vision packages, gazebo simulation, rviz and more robotics tools can be used if
the project gets bigger.
4.2 Understanding ROS Topic publisher, subscriber and ROS Node
ROS topic is used to communicate messages from one node to another node. Ros topic
pub is used to publish messages from command line. I have tested publishing string message in
one terminal and echoing the same string message by using rostopic echo. I have tested how
much the rate of message is being published by giving values of 1, 5, 10 seconds. I have used the
command line and created python file to test this scenarios.
rostopic echo -n 1 /topic_name
to test the string message being published. rostopic list used to check active topic. Similarly tried
with rosnode to see current active node.
4.3 Creating ROS node
Publisher node and subscriber node is created in python file with topic name “chatter” to
check the string message is being published and received. This nodes are tested since I was
making a bridge between MQTT and ROS.
4.4 Understanding MQTT protocol
MQTT is light weight protocol used for connections with remote locations and it
exchanges data between devices and server. Arduino command velocity messages are sent to
MQTT server and MQTT server will send it to ROS node.
4.5 Understanding MQTT publisher and subscriber
Mosquitto pub command is used to test in command line to check how MQTT protocol
works. Similarly python file has been created for publisher and subscriber to test communication
between subscriber and publisher.
4.6 Creating Bridge between ROS and MQTT
We have to create a bridge between ROS and MQTT to communicate each other. The
protocol used by mqtt bridge is ROS message. JSON (or message pack) is used to serialize
messages from ROS for MQTT, while message pack is used to deserialize MQTT messages for
ROS topic. So MQTT messages ought to be compatible with ROS messages. (For message
conversion, we employ rosbridge library internal message conversion) Tested by sending some
messages from MQTT to ROS and ROS to MQTT.
Fig 2. MQTT ROS bridge
Source: http://wiki.ros.org/mqtt_bridge
4.7 Receiving Arduino Command velocity from MQTT to ROS
Arduino will send command velocity message on MQTT server. Tested sending of
command velocity on command line by using mosquito pub command. MQTT message will be
deserialized and stored according to Twist ROS message. mqtt_ros/receive_arduino_msg topic
has been used to receive message from MQTT.
4.8 Sending Joystick Command Velocity to Arduino from ROS to MQTT
ROS will send the Joystick command velocity to Arduino. This has been tested by
sending command velocity “x”:data.linear.x , “z”:data.angular.z. Linear velocity is used to move
robot forward and angular velocity is used to turn the robot. ros_mqtt/cmd_vel used to publish
message from ROS to MQTT.
