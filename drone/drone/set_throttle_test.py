from mavros_msgs.msg import ManualControl
import rclpy
from rclpy.node import Node

class ManualThrottle(Node):
    def __init__(self):
        super().__init__('manual_throttle')
        self.manual_pub = self.create_publisher(ManualControl, '/mavros/manual_control/send', 10)
        self.timer = self.create_timer(0.1, self.publish_manual_control)

    def publish_manual_control(self):
        msg = ManualControl()
        msg.x = 0.0  # Pitch
        msg.y = 0.0  # Roll
        msg.z = 0.5  # 50% throttle (range 0 to 1)
        msg.r = 0.0  # Yaw
        self.manual_pub.publish(msg)
        self.get_logger().info(f'Setting throttle to 50%')

def main():
    rclpy.init()
    node = ManualThrottle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
