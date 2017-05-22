cmake_minimum_required(VERSION 2.8.3)
project(spincopter_gazebo)

find_package(catkin REQUIRED COMPONENTS
	cmake_modules
	roscpp
	std_msgs
	geometry_msgs
	genmsg
	sensor_msgs
	message_generation
	gazebo_ros
	gazebo_msgs)


if (FALSE)#${gazebo_VERSION_MAJOR} LESS 6
  include (FindPkgConfig)
  if (PKG_CONFIG_FOUND)
    pkg_check_modules(XML libxml-2.0)
    pkg_check_modules(OGRE OGRE)
    pkg_check_modules(OGRE-Terrain OGRE-Terrain)
  else()
    message(FATAL_ERROR "pkg-config is required; please install it")
  endif()

  
  find_package(Boost REQUIRED COMPONENTS thread)

  execute_process(COMMAND
    pkg-config --variable=plugindir OGRE
    OUTPUT_VARIABLE OGRE_PLUGIN_PATH
    OUTPUT_STRIP_TRAILING_WHITESPACE
  )
endif()
find_package(gazebo REQUIRED)
find_package(Eigen REQUIRED)

catkin_package(
INCLUDE_DIRS include launch plugins worlds ${Eigen_INCLUDE_DIRS}
	LIBRARIES SPINCOPTER_gazebo
	CATKIN_DEPENDS geometry_msgs roscpp std_msgs message_runtime sensor_msgs
	DEPENDS system_lib gazebo_ros eigen
	)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

include_directories(${Eigen_INCLUDE_DIRS})



link_directories(${GAZEBO_LIBRARY_DIRS})# ${OGRE_LIBRARY_DIRS})
include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})# ${Boost_INCLUDE_DIR}  ${OGRE_INCLUDE_DIRS} ${OGRE-Terrain_INCLUDE_DIRS})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")



install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY worlds
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
