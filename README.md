# RoboticsGeoLocation
Robotics Geolocation Project

This is an mini project to demonstrate my ability to generate a Turtle Robot that can autonomously make it's way to a given location.


### Setup:
 - setup docker container for ros http://wiki.ros.org/docker/Tutorials/Docker
 - get turtle bot set up

 - ros to turtlesim guide mac os (docker): https://desertbot.io/blog/ros-turtlesim-beginners-guide-mac
 1. 
 
 

### Part 1: Create some code for turtle to be able to directly move to the a given location.
- Get initial tutle onto a map
- Get initial rotation, trajectory and distance abiliy from current location to coordinate location
- introduce mapping functionality? google maps api??

### Step 1: Spin up a new docker container
#### Spinning up a Docker container for core noetic build
- `docker pull ros`
- ~~`sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" --name roslocal -it ros:noetic-ros-core /bin/bash`~~
- `docker run -e DISPLAY=host.docker.internal:0 --name rosproject -it ros:noetic-ros-core
bash`

#### Accessing docker container
- `docker exec -it rosproject bash`   

#### Updating and installing turtlesim
```bash
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install build-essential libssl-dev
sudo apt-get install ros-noetic-ros
sudo apt-get install ros-noetic-turtlesim
```
- 
- note: added at the end of `~/.bashrc` -> `source ../opt/ros/noetic/setup.bash` this allows immediate access to ros tools
  -`echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc`
  
- to display all docker containers on a new terminal `docker ps -l`
```bash
(base) omro@Omars-MacBook-Pro-6 ~ % docker ps -l
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS     NAMES
1fc98c8ed6cc   ros:noetic-ros-core   "/ros_entrypoint.sh …"   10 minutes ago   Up 10 minutes             rosproject
```

enter the container of interest ie rosproject in this case
- `docker exec -it rosproject bash`


## SETTING UP PROJECT AND GETTING TURTLESIM UP AND RUNNING
- ENTER THE DESIRED WORKSPACE in my case new workspace 
```bash
mkdir project
cd project
```
Build the project files
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
rosrun turtlesim turtlesim_node
```

I cam across this error

```bash
libGL error: No matching fbConfigs or visuals found 
libGL error: failed to load driver: swrast
```
fixed with 
```bash
export LIBGL_ALWAYS_INDIRECT=1
sudo apt-get install -y mesa-utils libgl1-mesa-glx
```

#### Resources: 
- http://wiki.ros.org/docker/Tutorials/Docker
- https://www.reddit.com/r/ROS/comments/udxwcv/what_version_of_ros_should_i_download/
- https://wiki.ros.org/Distributions
- ros to turtlesim guide mac os (docker): https://desertbot.io/blog/ros-turtlesim-beginners-guide-mac


