#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random

class PositionPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')
        self.publisher_ = self.create_publisher(Point, '/position', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Point()
        msg.x = random.uniform(-5.0, 5.0)
        msg.y = random.uniform(-5.0, 5.0)
        msg.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pozíció publikálva: x={msg.x:.2f}, y={msg.y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = PositionPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
