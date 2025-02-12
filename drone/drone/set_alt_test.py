from mavros_msgs.msg import AttitudeTarget
import rclpy
from rclpy.node import Node

class AttitudeControl(Node):
    def __init__(self):
        super().__init__('attitude_control')
        self.attitude_pub = self.create_publisher(AttitudeTarget, '/mavros/setpoint_raw/attitude', 10)
        self.timer = self.create_timer(0.1, self.publish_attitude)

    def publish_attitude(self):
        msg = AttitudeTarget()
        msg.thrust = 0.6  # 60% throttle
        msg.type_mask = 7  # Ignore roll, pitch, and yaw (use throttle only)
        self.attitude_pub.publish(msg)
        self.get_logger().info(f'Setting throttle: {msg.thrust}')

def main():
    rclpy.init()
    node = AttitudeControl()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
