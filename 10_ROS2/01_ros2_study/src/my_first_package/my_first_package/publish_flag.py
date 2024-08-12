import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class FlagPublisher(Node):
    def __init__(self):
        super().__init__('flag_publisher')
        self.publisher_ = self.create_publisher(Int32, 'set_flag', 10)
        timer_period = 5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = 1
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    flag_publisher = FlagPublisher()
    rclpy.spin(flag_publisher)
    flag_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()