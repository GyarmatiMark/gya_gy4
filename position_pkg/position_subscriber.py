#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import math

class PositionSubscriber(Node):
    def __init__(self):
        super().__init__('position_subscriber')
        self.subscription = self.create_subscription(
            Point, '/position', self.listener_callback, 10)

    def listener_callback(self, msg: Point):
        distance = math.hypot(msg.x, msg.y)
        self.get_logger().info(
            f'Megkapott pozíció: x={msg.x:.2f}, y={msg.y:.2f} | Távolság: {distance:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = PositionSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
