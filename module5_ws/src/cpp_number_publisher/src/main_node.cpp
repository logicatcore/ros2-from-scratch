#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int32.hpp"

class NumberPublisher : public rclcpp::Node
{
public:
    NumberPublisher() : Node("number_publisher"), counter_(0)
    {
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&NumberPublisher::number_publisher, this));
        publisher_ = this->create_publisher<example_interfaces::msg::Int32>("number", 10);
        RCLCPP_INFO(this->get_logger(), "Number publisher node has been started.");
    }
    void number_publisher()
    {
        auto msg = example_interfaces::msg::Int32();
        msg.data = counter_;
        publisher_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Publishing: %d", msg.data);
        counter_++;
    }
private:
    int counter_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<example_interfaces::msg::Int32>::SharedPtr publisher_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}