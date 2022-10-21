# Original work Copyright (c) 2022 Sky360
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    return LaunchDescription([
        Node(            
            package='simple_tracker_ui_test',
            #namespace='sky360',
            executable='ui_test',
            name='simple_tracker_ui_test',
            remappings=[
                ('sky360/visualiser/annotated_frame', 'sky360/frames/annotated/v1'),
                #('sky360/visualiser/original_camera_frame', 'sky360/camera/original/v1'),
                #('sky360/visualiser/original_frame', 'sky360/frames/original/v1'),
                #('sky360/visualiser/masked_frame', 'sky360/frames/masked/v1'),
                #('sky360/visualiser/grey_frame', 'sky360/frames/grey/v1'),
                #('sky360/visualiser/dense_optical_flow_frame', 'sky360/frames/dense_optical_flow/v1'),
                #('sky360/visualiser/masked_background_frame', 'sky360/frames/masked_background/v1'),
                #('sky360/visualiser/foreground_mask_frame', 'sky360/frames/foreground_mask/v1'),                
            ]
        ),        
    ])
