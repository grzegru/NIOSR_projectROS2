#!/usr/bin/env python3
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from geometry_msgs.msg import Point # Image is the message type
from cv_bridge import CvBridge # ROS2 package to convert between ROS and OpenCV Images
import cv2 # Python OpenCV library
from std_msgs.msg import String
import numpy as np


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('point')
        self.window_name = "mouse_control_panel"
        self.subscription = self.create_subscription(Image,'image',self.listener_callback,10)     
        self.subscription  
        self.point = None
        self.pointRectangle = None
        self.publisher = self.create_publisher(Point,'point',10)
        self.out_of_control = -1
        self.line1_start_point = (0,150)
        self.line1_end_point = (700,150)
        self.line2_start_point = (0,350)
        self.line2_end_point = (700,350)
        self.line3_start_point = (150,0)
        self.line3_end_point = (150,550)
        self.line4_start_point = (550,0)
        self.line4_end_point = (550,550)
        
        

    def listener_callback(self, image_data):
        image = np.zeros((500,700,3), np.uint8)
        if(self.point is not None):
            cv2.rectangle(image,self.point,self.pointRectangle,(0,255,0),2)
        cv2.line(image, self.line1_start_point,self.line1_end_point, (207,41,41), 4)
        cv2.line(image, self.line2_start_point,self.line2_end_point, (207,41,41), 4)
        cv2.line(image, self.line3_start_point,self.line3_end_point, (207,41,41), 4)
        cv2.line(image, self.line4_start_point,self.line4_end_point, (207,41,41), 4)
        cv2.imshow(self.window_name, image)
        cv2.waitKey(25)
        cv2.setMouseCallback(self.window_name, self.draw) 

    def draw(self, eventType, x, y, flags, param):
        point= Point()
        if eventType == cv2.EVENT_LBUTTONDOWN: 
            self.point = (x-30,y-30)
            self.pointRectangle = (x+30,y+30)
            point.x = np.float(x)
            point.y = np.float(y)
            
        else:
            self.point = None
            point.x = self.out_of_control
            point.y = self.out_of_control
        self.publisher.publish(point)




def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
