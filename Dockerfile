# Use the official ROS melodic image as the base image
FROM ros:melodic

# Install additional dependencies
RUN apt-get update && apt-get install -y \
    ros-melodic-turtlebot3 \
    ros-melodic-turtlebot3-msgs \
    ros-melodic-turtlebot3-simulations \
    && rm -rf /var/lib/apt/lists/*

# Set up the workspace
WORKDIR /catkin_ws

# Copy the TurtleBot3 simulation files into the workspace
COPY . /catkin_ws

# Build the workspace
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash && catkin_make"

# Set the entry point to launch the TurtleBot3 simulation
CMD /bin/bash -c "source /catkin_ws/devel/setup.bash && roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch"
