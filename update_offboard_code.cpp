void OffboardControl::publish_trajectory_setpoint()
{
    TrajectorySetpoint msg{};
    msg.position = {0.0, 0.0, -5.0};
    msg.yaw = -3.14; // [-PI:PI]
    msg.timestamp = this->get_clock()->now().nanoseconds() / 1000;
    trajectory_setpoint_publisher_->publish(msg);

    RCLCPP_INFO(this->get_logger(), "Published setpoint: position = [%f, %f, %f], yaw = %f",
                 msg.position[0], msg.position[1], msg.position[2], msg.yaw);
}
