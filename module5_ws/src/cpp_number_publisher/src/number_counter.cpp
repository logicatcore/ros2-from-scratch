#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int32.hpp"

class NumberCounter: public rclcpp::Node
{
public:
    NumberCounter(): Node("number_counter"), sum(0)
    {
        subscription = this->create_subscription<example_interfaces::msg::Int32>(
            "number",
            10,
            std::bind(&NumberCounter::add_values, this, std::placeholders::_1)
        );
    }

    void add_values(example_interfaces::msg::Int32::SharedPtr msg)
    {
        sum += msg->data;
        RCLCPP_INFO(this->get_logger(), "Received: %d, Sum: %d", msg->data, sum);
    }

private:
    int sum;
    rclcpp::Subscription<example_interfaces::msg::Int32>::SharedPtr subscription;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberCounter>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}