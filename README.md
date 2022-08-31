# RoboticsGeoLocation
Robotics Geolocation Project

This is an mini project to demonstrate my ability to generate a Turtle Robot that can autonomously make it's way to a given location from anywhere on earth. Initial goal location is the Greenwhich Observatory.

**important things to remember:**
- this is about reboustness and structure of code rather than the actual number of features introduced.
- code cleanliness and readability is important


## Step 1: Create a realistic plan

### Setup:
 - setup docker container for ros http://wiki.ros.org/docker/Tutorials/Docker
 - get turtle bot set up
 
 

### Part 1: Create some code for turtle to be able to directly move to the a given location.
- Get initial tutle onto a map
- Get initial rotation, trajectory and distance abiliy from current location to coordinate location
- introduce mapping functionality? google maps api??




### Part 2: Introduce some ability to move across walking platforms???? google map api???? 
Idea 1: - Get path from google maps, implement PID to follow the line.


## Step 2: Create general methods


## Step 3: Create tests for given methods??????????????????????????????????
- checkout pytest and pyunit


#### Spinning up a Docker container for core noetic build
- `docker pull ros`
- `sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --name roslocal -it ros:noetic-ros-core /bin/bash`

#### Accessing docker container
- `docker exec -it roslocal bash`
note: added at the end of `.bashrc` -> `source ../opt/ros/noetic/setup.bash`

#### Updating and installing turtlesim
- `apt-get update`
- `sudo apt-get install ros-noetic-turtlesim`

#### Resources: 
- http://wiki.ros.org/docker/Tutorials/Docker
- https://www.reddit.com/r/ROS/comments/udxwcv/what_version_of_ros_should_i_download/
- https://wiki.ros.org/Distributions


