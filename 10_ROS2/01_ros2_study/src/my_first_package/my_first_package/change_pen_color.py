import rclpy
from rclpy.node import Node
from turtlesim.srv import SetPen
from turtlesim.msg import Pose

class PenColorChanger(Node):
    def __init__(self):
        super().__init__('pen_color_changer')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        self.subscription
        self.cli = self.create_client(SetPen, '/turtle1/set_pen')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def pose_callback(self, msg):
        request = SetPen.Request()
        if msg.x < 5.0:
            request.r = 255
            request.g = 0
            request.b = 0
        else:
            request.r = 0
            request.g = 0
            request.b = 0
        request.width = 3
        request.off = 0
        self.cli.call_async(request)

def main(args=None):
    rclpy.init(args=args)
    pen_color_changer = PenColorChanger()
    rclpy.spin(pen_color_changer)
    pen_color_changer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()