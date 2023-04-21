#!/usr/bin/env python3

import random
import math
import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn, TeleportAbsolute, SetPen


NODE_NAME = "draw_node"
TURTLE1 = "turtle1"
TURTLE2 = "turtle2"
TURTLE3 = "turtle3"

DEFAULT_PEN_WIDTH = 3
BORDER_POINT = 0.5

def get_default_color():
    return 255, 255, 255

def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

class InitialsTurtle:
    def __init__(self, name):
        rospy.init_node(NODE_NAME)
        
        self.name = name

        self.vel_pub = rospy.Publisher('/%s/cmd_vel' % name, Twist, queue_size=100)
        self.pose_sub = rospy.Subscriber(f'/{name}/pose', Pose, self.pose_callback) 
        
        self.twist = Twist()
        self.current_pose = Pose()
        self.rate = rospy.Rate(1)
        
    def pose_callback(self, data) -> Pose:
        self.current_pose = data
        self.current_pose.x = round(self.current_pose.x, 4)
        self.current_pose.y = round(self.current_pose.y, 4)
    
    def draw_digits(self):
        rospy.loginfo('drawing digits')
        
        self.rate.sleep()
        
        # Drawing digit 0:
        
        self.twist.angular.z = math.pi
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = math.pi
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.set_pen((0, 0, 0), 0, 1) # turning off pen
        self.teleport(self.current_pose.x + 1.0, self.current_pose.y, math.pi/2)
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0) # turning on pen
        
        # Drawing 2nd digit 0:
                
        self.twist.angular.z = -190 * math.pi / 180
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = -math.pi
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.set_pen((0, 0, 0), 0, 1) # turning off pen
        self.teleport(self.current_pose.x + 2.0, self.current_pose.y, math.pi/2)
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0) # turning on pen

        # Drawing digit 2:
        self.twist.angular.z = -math.radians(200)
        self.twist.linear.x = 2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = -math.radians(20)
        self.twist.linear.x = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 2.5
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = math.radians(120)
        self.twist.linear.x = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.angular.z = 0
        self.twist.linear.x = 1.5
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
    def draw_letters(self):
        rospy.loginfo('drawing letters')
        
        self.set_pen((0, 0, 0), 0, 1) # turning off pen
        self.teleport(3, 9, 0)
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0) # turning on pen
                
        self.rate.sleep() 

        # Drawing letter 'S'
        self.twist.linear.x = 0
        self.twist.angular.z = math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 1
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 2
        self.twist.angular.z = math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0.5
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 2
        self.twist.angular.z = -math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 1
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.set_pen((0, 0, 0), 0, 1) # turning off pen
        self.teleport(self.current_pose.x + 2.0, self.current_pose.y, math.pi/2)
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0) # turning on pen

        # Drawing letter 'N'
        self.twist.linear.x = 2.5
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = -2.5
        self.twist.linear.y = -1.3
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 2.5
        self.twist.linear.y = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.set_pen((0, 0, 0), 0, 1) # turning off pen
        self.teleport(self.current_pose.x + 1.0, self.current_pose.y, -math.pi/2)
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0) # turning on pen
        
        # Drawing letter 'B'
        
        self.twist.linear.x = 2.5
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0
        self.twist.linear.y = 0
        self.twist.angular.z = math.pi/2
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 1
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 2.2
        self.twist.angular.z = math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0.4
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0
        self.twist.angular.z = math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0.4
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 1.8
        self.twist.angular.z = math.pi
        self.vel_pub.publish(self.twist)
        self.rate.sleep()

        self.twist.linear.x = 1
        self.twist.angular.z = 0
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
        self.twist.linear.x = 0.3
        self.twist.angular.z = math.pi/3
        self.vel_pub.publish(self.twist)
        self.rate.sleep()
        
    
    def draw_border_square(self):
        self.set_pen(get_random_color(), DEFAULT_PEN_WIDTH, 0)
        
        self.rate.sleep()
        
        for i in range(1,5):
            self.twist.linear.x = 10
            self.twist.angular.z = 0
            self.vel_pub.publish(self.twist)
            self.rate.sleep()
                
            self.twist.linear.x = 0
            self.twist.angular.z = math.radians(90)
            self.vel_pub.publish(self.twist)
            self.rate.sleep()
                        
    def euclidean_distance(self, goal: Pose):
        return math.sqrt(pow((goal.x - self.current_pose.x), 2) + pow((goal.y - self.current_pose.y), 2))
    
    def steering_angle(self, goal: Pose):
        return math.atan2(goal.y - self.current_pose.y, goal.x - self.current_pose.x)
    
    def angular_vel(self, pose: Pose):
        return self.steering_angle(pose) - self.current_pose.theta
        
    def set_pen(self, rgb, width, off):
        rospy.wait_for_service(f'/{self.name}/set_pen')
        try:
            teleport = rospy.ServiceProxy(f'/{self.name}/set_pen', SetPen)
            teleport(rgb[0],rgb[1],rgb[2], width, off)
        except rospy.ServiceException as e:
            rospy.logerr(f"set_pen service call failed: {e}")
    
    def teleport(self, x, y, theta):
        rospy.wait_for_service(f'/{self.name}/teleport_absolute')
        try:
            teleport = rospy.ServiceProxy(f'/{self.name}/teleport_absolute', TeleportAbsolute)
            teleport(x, y, theta)
        except rospy.ServiceException as e:
            rospy.logerr(f"teleport_absolute service call failed: {e}")

def spawn_turtle(name, x, y, theta):
    rospy.wait_for_service('/spawn')
    try:
        spawn = rospy.ServiceProxy('/spawn', Spawn)
        spawn(x, y, theta, name)
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == '__main__':
    turtle = InitialsTurtle(TURTLE1)
    turtle.draw_letters()
    
    spawn_turtle(TURTLE2, 3, 5, math.pi/2)
    turtle2 = InitialsTurtle(TURTLE2)
    turtle2.draw_digits()
    
    spawn_turtle(TURTLE3, BORDER_POINT, BORDER_POINT, 0)
    turtle3 = InitialsTurtle(TURTLE3)
    turtle3.draw_border_square()