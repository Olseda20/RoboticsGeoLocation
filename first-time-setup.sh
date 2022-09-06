echo "Heyyo, this is the first time setup of my rosproject. This will install all the relevant dependancies to get an appropriate ros container set up."

# getting ros set up
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install pip
sudo apt-get install build-essential libssl-dev
export LIBGL_ALWAYS_INDIRECT=1
sudo apt-get install -y mesa-utils libgl1-mesa-glx
sudo apt-get install ros-noetic-ros
sudo apt-get install ros-noetic-turtlesim
pip install pytest
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# creating the project file
DIR=$(pwd)
mkdir /project
cd project
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
cd $DIR
