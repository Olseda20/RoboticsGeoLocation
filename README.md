# RoboticsGeoLocation
Robotics Geolocation Project

This is an mini project to demonstrate my ability to generate a Turtle Robot that can autonomously make it's way to a given location.


### SETUP
### Part 1: Create some code for turtle to be able to directly move to the a given location.
- Get initial tutle onto a map
- Get initial rotation, trajectory and distance abiliy from current location to coordinate location
- introduce mapping functionality? google maps api??

### Step 1: Spin up a new docker container
#### Spinning up a Docker container for core noetic build
In your terminal set up a docker instance for the project. in this case the name of the project is `rosproject`
```bash
docker pull ros
docker run -e DISPLAY=host.docker.internal:0 --name rosproject -it ros:noetic-ros-core bash
```

#### Accessing docker container
```
docker exec -it rosproject bash
```   
- note: if you're outside of your continer, to display the available docker containers on a new terminal run `docker ps -l`
```bash
(base) omro@Omars-MacBook-Pro-6 ~ % docker ps -l
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS     NAMES
1fc98c8ed6cc   ros:noetic-ros-core   "/ros_entrypoint.sh …"   10 minutes ago   Up 10 minutes             rosproject
```

#### Run the first time setup
Once you're inside the docker continer, run the `first-time-setup.sh` bash script to install all the relevant depancies  for the project.
```bash
./first-time-setup.sh
```

### Testing the Work
1- To ensure the envoronment is appropriately set up and the Position and Motion methdos are appropriately working. Please run the Provided tests ensuring they all pass.

In a new terminal window that is (currently accessing the `rosproject` docker container) run the 2 provided tests.
Position Tests
```
pytest PositionTests.py
```
Motion Tests
```
pytest MotionTests.py
```

Once you're happy the tests are running.
Open up 2 more terminal windows (total of 3 windows accessing the docker container).
1st window:
run roscore to ensure a master is running
```bash
roscore
``

2nd window:
run the turtlesim to visualise the motion
```bash
rosrun turtlesim turtlesim_node 
```

3rd window:
this will be where you will test the move to goal functionality
you should run the run.py script with 2 potional arguments which will make up a set of coordinates (6 7)
```bash
python3 run.py 6 7
```
you should see the turtle moving towards the provided coordiante location.

I would encourage you to test several locations.



#### Resources: 
- http://wiki.ros.org/docker/Tutorials/Docker
- https://www.reddit.com/r/ROS/comments/udxwcv/what_version_of_ros_should_i_download/
- https://wiki.ros.org/Distributions
- ros to turtlesim guide mac os (docker): https://desertbot.io/blog/ros-turtlesim-beginners-guide-mac


