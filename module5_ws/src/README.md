# Commands used in Module 5

* Commands used to create packages
  * `ros2 pkg create number_publisher --build-type ament_python --dependencies rclpy example_interfaces`
  * `ros2 pkg create cpp_number_publisher --build-type ament_cmake --dependencies rclcpp example_interfaces`

* Sourcing the setup.bash script
  * `source install/setup.bash`

* To run the nodes
  * `ros2 run number_publisher number_publisher`
  * `ros2 run cpp_number_publisher number_publisher`

* To check the currently published topics
  * `ros2 topic list`

* To create an impromptu subscriber 
  * `ros2 topic echo /number`


