import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'number', 10)
        self.timer = self.create_timer(1.0, self.publish_number)
        self.number = 0
        self.get_logger().info('Number Publisher Node has been started.')

    def publish_number(self):
        msg = Int32()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {self.number}')
        self.number += 1

def main(args=None):
    rclpy.init(args=args)
    number_publisher = NumberPublisher()
    rclpy.spin(number_publisher)
    rclpy.shutdown()