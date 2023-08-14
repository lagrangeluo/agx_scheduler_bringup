#!/bin/bash
source /home/agilex/ff_ros2_ws/src/agx_scheduler_bringup/agx_scheduler_bringup/start/shell &&
   
source /opt/ros/galactic/setup.bash &&
   
source /home/agilex/rmf_ws/install/setup.bash &&
   
source /home/agilex/ff_ros2_ws/install/setup.bash &&

ros2 launch agx_scheduler_bringup navis_rmf_all.launch.xml
