# TurtleToLocation
Robotics Geolocation Project

This is an mini project to demonstrate my ability to generate a Turtle Robot that can autonomously make it's way to a given location.

### Part 1: Create some code for turtle to be able to directly move to the a given location.
- Get initial turtle onto a map
- Get initial rotation, trajectory and distance abiliy from current location to coordinate location


## SETUP

This assumes you have docker installed on your machine. https://docs.docker.com/get-docker/

### Step 1: Spin up a new docker container
#### Spinning up a Docker container for core noetic build
In your terminal set up a docker instance for the project. in this case the name of the project is `rosproject`
```bash
docker pull ros
docker run -e DISPLAY=host.docker.internal:0 --name rosproject -it ros:noetic-ros-core bash
```

#### Step 2: Accessing docker container
You are most likely already inside of the docker container if you're seeing something along the lines of 
```bash
root@db5ef5c82850:/# 
```

If not then enter the docker container from your terminal. (note: if you have named your project differently to `rosproject`, make sure to enter the appropriate name)
```
docker exec -it rosproject bash
```   
this will be important later on when you will need to open up multiple container windows

- note: if you're outside of your continer, to display the available docker containers on a new terminal run `docker ps -l`
```bash
(base) omro@Omars-MacBook-Pro-6 ~ % docker ps -l
CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS     NAMES
1fc98c8ed6cc   ros:noetic-ros-core   "/ros_entrypoint.sh …"   10 minutes ago   Up 10 minutes             rosproject
```

#### Step 3: Run the first time setup
Once you're inside the docker continer, run the `first-time-setup.sh` bash script to install all the relevant depancies  for the project.
```bash
./first-time-setup.sh
```

## Testing the Work
Before Proceeding, make sure you are inside of the correct directroy and for the sake of convenince, if you open up a new terminal tab accessing the container, made sure to make your way back to this directory, most likely  

run the command below to reach it if you aren't there yet.
```bash
cd /RoboticsGeoLocation
```

### 1- Testing
To ensure the envoronment is appropriately set up and the Position and Motion methods are appropriately working. Please run the Provided tests ensuring they all pass.

In a new terminal window that is (currently accessing the `rosproject` docker container) run the 2 provided tests.

**Position Tests**
```
pytest PositionTests.py
```
successful results look like   

<img width="544" alt="image" src="https://user-images.githubusercontent.com/49950899/188654917-8f849135-6b3c-4859-9b21-f1161985cde1.png">


**Motion Tests**
```
pytest MotionTests.py
```
successful results look like   

<img width="540" alt="image" src="https://user-images.githubusercontent.com/49950899/188654781-f1fb35c4-00fb-4ea5-8ea1-73469f3db9b1.png">


### 2- Running the move to goal script
Once you're happy the tests are running.
Open up 2 more terminal windows (total of 3 windows accessing the docker container).

#### 1st window: roscore
run roscore to ensure a master is running
```bash
roscore
```

#### 2nd window: turtlesim
run the turtlesim to visualise the motion
```bash
rosrun turtlesim turtlesim_node 
```

#### 3rd window: testing functionality
this will be where you will test the move to goal functionality
you should run the MoveTurtle.py script with 2 positional arguments which will make up a set of coordinates eg (8 9)
```bash
python3 MoveTurtle.py.py 8 9
```
you should see the turtle moving towards the provided coordiante location.
<img width="495" alt="image" src="https://user-images.githubusercontent.com/49950899/188760956-0365916c-1de8-42b3-ba85-2785bbcb2cf9.png">

### Next Parts of this project
I would start to incorporate some sort of Mapping/GPS API to identify a gps location of a given turtle. 
https://github.com/googlemaps/google-maps-services-python
this could solve a lot of the path planning issues associated by making use of pre-existing solutions to this particular problem.
  
Positionally, rather than using the Pose Data from the `turtle1/pose` node, I would instead look to identify the coordinate location using GPS. Along with the coordinate location of the turtle, I would do something similar for the coordinate location of the Desired location (Greenwhich?)
  
Initially, I would making use of the same methods generated in this project to move the turtle towards the location using the same motion. 
  
On success of this I would start thinking about the process of making use of waypoints built into that api. I would think about the checkpoints a person might need to make while `walking` this route, or a car `driving`, split it up into appropriate sections, and still using the same motion system, move towards to split checkpoint locations.

  
#### Resources: 
- http://wiki.ros.org/docker/Tutorials/Docker
- https://wiki.ros.org/Distributions
- ros to turtlesim guide mac os (docker) to get visualisation: https://desertbot.io/blog/ros-turtlesim-beginners-guide-mac


