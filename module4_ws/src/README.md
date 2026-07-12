# Commands used in Module 4

* Commands used to create packages in *module4_ws* folder
  * `ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy`
  * `ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp`

* To build the executables/packages
  * `colcon build`
  * `colcon build --packages-select my_cpp_pkg`

* To source the executables into the terminal
  * `source ./install/setup.bash`

* To run the executables
  * `ros2 run my_py_pkg test_node` 
  * `ros2 run my_cpp_pkg test_node` 