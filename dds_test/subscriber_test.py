import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import csv


class DDSSubscriber(Node):
    def __init__(self):
        super().__init__('dds_subscriber')
        self.subscription = self.create_subscription(
            String,
            'dds_test_topic',
            self.listener_callback,
            10
        )

        self.received_count = 0
        self.last_counter = None
        self.lost_count = 0

        self.csv_file = open('dds_result.csv', 'w', newline='')
        self.writer = csv.writer(self.csv_file)
        self.writer.writerow([
            'received_count',
            'message_id',
            'latency_ms',
            'lost_count',
            'receive_time'
        ])

    def listener_callback(self, msg):
        receive_time = time.time()

        try:
            parts = msg.data.split(',', 2)
            message_id = int(parts[0])
            send_time = float(parts[1])

            latency_ms = (receive_time - send_time) * 1000.0

            if self.last_counter is not None:
                expected = self.last_counter + 1
                if message_id > expected:
                    self.lost_count += message_id - expected

            self.last_counter = message_id
            self.received_count += 1

            self.writer.writerow([
                self.received_count,
                message_id,
                latency_ms,
                self.lost_count,
                receive_time
            ])
            self.csv_file.flush()

            self.get_logger().info(
                f"ID={message_id} latency={latency_ms:.3f} ms lost={self.lost_count}"
            )

        except Exception as e:
            self.get_logger().error(f"Error parsing message: {e}")

    def destroy_node(self):
        self.csv_file.close()
        super().destroy_node()


def main():
    rclpy.init()
    node = DDSSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
