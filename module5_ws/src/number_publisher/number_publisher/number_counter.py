import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32

class NumberCounter(Node):
    def __init__(self):
        super().__init__('number_counter')
        self.subscription = self.create_subscription(Int32, 'number', self.add_values, 10)
        self.get_logger().info('Number Counter Node has been started.')
        self.sum_ = 0
    
    def add_values(self, msg):
        self.sum_ += msg.data
        self.get_logger().info(f'Received: {msg.data}, Sum: {self.sum_}')

def main(args=None):
    rclpy.init(args=args)
    number_counter = NumberCounter()
    rclpy.spin(number_counter)
    rclpy.shutdown()

if __name__ == '__main__':
    main()