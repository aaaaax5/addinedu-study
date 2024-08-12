import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

class FlagSubscriber(Node):
    def __init__(self):
        super().__init__('flag_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'set_flag',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription

    def listener_callback(self, msg):
        if msg.data == 1:
            twist = Twist()
            twist.angular.z = 2.0
            self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    flag_subscriber = FlagSubscriber()
    rclpy.spin(flag_subscriber)
    flag_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()