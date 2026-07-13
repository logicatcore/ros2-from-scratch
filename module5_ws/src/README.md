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

* To publish a topic directly from the terminal (only helpful for simple interfaces though). `ros2 topic pub -r <frequency> <topic_name> <interface> <message_in_json>`.
  * ros2 topic pub -r 2.0 /number example_interfaces/msg/Int64 "{data: 7}"
  * here 2.0 corresponds to frequency i.e. 2 Hertz (every 05 seconds)

* To record and play ros2 bags
  * Record: `ros2 bag record /number -o bag1`
  * Play: `ros2 bag play ~/bag1`

* To rename a node or a topic
  * Node renaming: You can change a node name at runtime by adding `--ros-args -r __node:=<new_name>` after the ros2 run command.
  * Topic renaming: you can also change a topic name at runtime. To do that, add another -r, followed by `<topic_name>:=<new_topic_name>`
  * Examples:
    * `ros2 run my_py_pkg number_publisher --ros-args -r number:=my_number`
    * `ros2 run my_py_pkg number_counter --ros-args -r number:=my_number`
    * `ros2 run my_py_pkg number_publisher --ros-args -r __node:=number_publisher_2 -r number:=my_number`