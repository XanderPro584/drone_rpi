import rclpy
from rclpy.node import Node
from geographic_msgs.msg import GeoPoseStamped

class FakeGPS(Node):
    def __init__(self):
        super().__init__('fake_gps_publisher')
        self.pub = self.create_publisher(GeoPoseStamped, '/mavros/setpoint_position/global', 10)
        self.timer = self.create_timer(1.0, self.publish_fake_gps)

    def publish_fake_gps(self):
        msg = GeoPoseStamped()
        msg.pose.position.latitude = 37.7749
        msg.pose.position.longitude = -122.4194
        msg.pose.position.altitude = 10.0
        self.pub.publish(msg)
        self.get_logger().info("Publishing Fake GPS Data")

def main():
    rclpy.init()
    node = FakeGPS()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
