import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class Controller(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("turtle_controller node created")
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.merry_go_round, 10)
        self.velocity_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

    def merry_go_round(self, msg : Pose):
        data_to_publish = Twist()
        if (msg.x <= 5.5):
            data_to_publish.linear.x = 1.0
            data_to_publish.angular.z = 1.0
            self.get_logger().info("x <= 5.5")
        else:
            data_to_publish.linear.x = 2.0
            data_to_publish.angular.z = 2.0
            self.get_logger().info("x > 5.5")
        self.velocity_publisher.publish(data_to_publish)

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    rclpy.spin(controller)
    rclpy.shutdown()

if __name__ == '__main__':
    main()