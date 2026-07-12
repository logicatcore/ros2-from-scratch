#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class DemoNode(Node):
    def __init__(self):
        super().__init__("DemoNode")
        self.get_logger().info("DemoNode has been started")
        self.counter_ = 0
        self.timer_ = self.create_timer(1.0, self.timer_callback) 
        
    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info(f"Timer called {self.counter_} times")

def main(args=None):
    rclpy.init(args=args)
    node = DemoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()