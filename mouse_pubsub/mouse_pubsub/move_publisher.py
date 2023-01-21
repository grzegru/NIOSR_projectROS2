#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point



def move_turtle(point, move):
        msg = Twist()
        if(point.y < 150 and (point.x > 150 and point.x <550) ) :
        	msg.linear.x = move
        elif(point.y > 350 and (point.x > 150 and point.x <550) ) :
        	msg.linear.x = -move
        elif(point.x < 150 and (point.y > 150 and point.y < 350) ):
        	msg.angular.z = move
        elif(point.x > 550 and (point.y > 150 and point.y < 350) ):
        	msg.angular.z = -move       
        elif((point.x < 150 and point.x > 0) and (point.y > 0 and point.y < 150)):
        	msg.linear.x = move
        	msg.angular.z = move
        elif(point.x < 150 and point.y > 350):
        	msg.linear.x = -move
        	msg.angular.z = move        
        elif(point.x > 550 and point.y < 150):
        	msg.linear.x = move
        	msg.angular.z = -move
        elif(point.x > 550 and point.y > 350):
        	msg.linear.x = -move
        	msg.angular.z = -move  
        else:
                msg.linear.x = 0.0
                msg.angular.z = 0.0  
        return msg      	     	


class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('move')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Point,'point',self.listener_callback,10)
        self.subscription
        self.declare_parameter('move', 1.0)
        self.velocity = self.get_parameter('move').value 
        timer_period = 0.5  # seconds
        self.msg = Twist()
        
    def timer_callback(self):
        self.publisher_.publish(self.msg)
        
    def listener_callback(self,point):
        self.msg = move_turtle(point, self.velocity)
        self.publisher_.publish(self.msg)


        
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
        self.publisher_.publish(self.msg)
