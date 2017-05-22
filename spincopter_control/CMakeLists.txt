cmake_minimum_required(VERSION 2.8.3)
project(spincopter_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  rosgraph_msgs
  genmsg
  geometry_msgs
  mav_msgs
  nav_msgs
  roscpp
  sensor_msgs
  cmake_modules
)


find_package(cmake_modules REQUIRED)
find_package(Eigen REQUIRED)
find_package(catkin REQUIRED)

catkin_package(
)
catkin_package(
  CATKIN_DEPENDS rospy std_msgs rosgraph_msgs genmsg geometry_msgs mav_msgs nav_msgs roscpp sensor_msgs
  DEPENDS Eigen
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${Eigen_INCLUDE_DIRS}
)

install(DIRECTORY config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})



