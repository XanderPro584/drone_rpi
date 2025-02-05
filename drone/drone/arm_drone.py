import rclpy
from rclpy.node import Node
from mavros_msgs.srv import CommandBool

class DroneArmingClient(Node):
    def __init__(self):
        super().__init__('drone_arm_client')
        self.client = self.create_client(CommandBool, '/mavros/cmd/arming')

        # Wait for the service to be available
        self.get_logger().info("Waiting for /mavros/cmd/arming service...")
        if not self.client.wait_for_service(timeout_sec=10.0):
            self.get_logger().error("Service /mavros/cmd/arming not available!")
            return
        
        # Send the arming request
        self.send_arm_request()

    def send_arm_request(self):
        request = CommandBool.Request()
        request.value = True  # Request to arm the drone

        self.get_logger().info("Sending arm request to mavros ")
        self.future = self.client.call_async(request)
        self.future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info("Drone armed successfully!")
            else:
                self.get_logger().error("Failed to arm the drone.")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    node = DroneArmingClient()
    rclpy.spin(node)  # Run the node once to send request
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
