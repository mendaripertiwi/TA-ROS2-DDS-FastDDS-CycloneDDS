import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import argparse


class DDSPublisher(Node):
    def __init__(self, rate_hz, message_size):
        super().__init__('dds_publisher')
        self.publisher_ = self.create_publisher(String, 'dds_test_topic', 10)
        self.counter = 0
        self.message_size = message_size
        timer_period = 1.0 / rate_hz
        self.timer = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        send_time = time.time()
        payload = "x" * self.message_size
        msg = String()
        msg.data = f"{self.counter},{send_time},{payload}"
        self.publisher_.publish(msg)
        self.counter += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rate', type=float, default=10.0)
    parser.add_argument('--size', type=int, default=1024)
    args, unknown = parser.parse_known_args()

    rclpy.init()
    node = DDSPublisher(args.rate, args.size)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
