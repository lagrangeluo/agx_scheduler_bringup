#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Joep Tool

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    spawn_file_dir = os.path.join(get_package_share_directory('auto_fleet'), 'launch')
    
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')

    x_pose_2 = LaunchConfiguration('x_pose_2', default='-2.5')
    y_pose_2 = LaunchConfiguration('y_pose_2', default='0.0')
    
    x_pose_3 = LaunchConfiguration('x_pose_3', default='-3.0')
    y_pose_3 = LaunchConfiguration('y_pose_3', default='1.0')
    
    turtlebot3_1 = LaunchConfiguration('turtlebot3_1', default='burger_1')
    turtlebot3_2 = LaunchConfiguration('turtlebot3_2', default='burger_2')
    turtlebot3_3 = LaunchConfiguration('turtlebot3_3', default='burger_3')

    tf_prefix_1 = LaunchConfiguration('tf_prefix_1', default='burger_1/')
    tf_prefix_2 = LaunchConfiguration('tf_prefix_2', default='burger_2/')
    tf_prefix_3 = LaunchConfiguration('tf_prefix_3', default='burger_3/')
    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'empty_world.world'
    )

    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )

    robot_state_publisher_cmd_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time,
   		  	   'tf_prefix': tf_prefix_1
        }.items()
    )

    robot_state_publisher_cmd_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time,
                    	   'tf_prefix': tf_prefix_2
        }.items()
    )

    robot_state_publisher_cmd_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'robot_state_publisher.launch.py')
        ),
        launch_arguments={'use_sim_time': use_sim_time,
                    	   'tf_prefix': tf_prefix_3
        }.items()
    )
    
    spawn_turtlebot_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose,
            'y_pose': y_pose,
            'TURTLEBOT3_MODEL': turtlebot3_1
        }.items()
    )
    
    spawn_turtlebot_2_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose_2,
            'y_pose': y_pose_2,
            'TURTLEBOT3_MODEL': turtlebot3_2
        }.items()
    )

    spawn_turtlebot_3_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(spawn_file_dir, 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments={
            'x_pose': x_pose_3,
            'y_pose': y_pose_3,
            'TURTLEBOT3_MODEL': turtlebot3_3
        }.items()
    )
    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(robot_state_publisher_cmd_1)
    #ld.add_action(robot_state_publisher_cmd_2)
    #ld.add_action(robot_state_publisher_cmd_3)
    ld.add_action(spawn_turtlebot_cmd)
    #ld.add_action(spawn_turtlebot_2_cmd)
    #ld.add_action(spawn_turtlebot_3_cmd)

    return ld
