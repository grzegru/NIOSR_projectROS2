#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image # Image is the message type

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('publisher_')
        self.publisher_ = self.create_publisher(Image, 'image', 10)
        timer_period = 0.1  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Image()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
