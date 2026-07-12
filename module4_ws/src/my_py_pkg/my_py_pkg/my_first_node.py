#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class DemoNode(Node):
    def __init__(self):
        super().__init__("DemoNode")
        self.get_logger().info("DemoNode has been started")


def main(args=None):
    rclpy.init(args=args)
    node = DemoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()