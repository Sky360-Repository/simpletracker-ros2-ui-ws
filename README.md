### This repository is designed to run alongside [simpletracker-ros2-ws](https://github.com/Sky360-Repository/simpletracker-ros2-ws)

#### To run the simpletracker-ros2-ws container, do the following:

1. Open terminal 
2. run `docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY sky360/simpletracker-ros2:1.0.1 bash`
3. run `./setup.sh`
4. run `nano ./src/simple_tracker_launch/launch/simple_tracker_launch.py`
5. Scroll down using the allows and comment out using # the entire visualiser node from the launch file.
```
  #Node(
  #    package='simple_tracker_visualisers',
  #    #namespace='sky360',
  #    executable='simple_visualiser',
  #    name='simple_visualiser',
  #    remappings=[
  #        ('sky360/visualiser/annotated_frame', 'sky360/frames/annotated/v1'),
  #        ('sky360/visualiser/original_camera_frame', 'sky360/camera/original/v1'),
  #        ('sky360/visualiser/original_frame', 'sky360/frames/original/v1'),
  #        ('sky360/visualiser/masked_frame', 'sky360/frames/masked/v1'),
  #        ('sky360/visualiser/grey_frame', 'sky360/frames/grey/v1'),
  #        ('sky360/visualiser/dense_optical_flow_frame', 'sky360/frames/dense_optical_flow/v1'),
  #        ('sky360/visualiser/masked_background_frame', 'sky360/frames/masked_background/v1'),
  #        ('sky360/visualiser/foreground_mask_frame', 'sky360/frames/foreground_mask/v1'),                
  #    ]
  #),
  ```
6. type `ctrl + x`
7.  `y`
8. run `./build.sh`

**NOTE** if you see the following error: `/usr/bin/python3.10: No module named rosidl_adapter` in red, then rerun the following commands: 

  1. `source /root/.bashrc` to source the ros2 install
  2. `./build.sh` to setup and run the simple tracker ros2

Finally, launch the application using:

9. run `./launch.sh`

The Simple Tracker ROS2 container should now be running without any UI

#### Run this simpletracker-ros2-ui-ws application

1. Open the **simpletracker-ros2-ui-ws** project folder using VS Code
2. Run this project using VS Code with the dev container extension installed as a dev container
3. From within the VS Code terminal type the following:
 - **NOTE:** If this is the first time you running the application since the container was built, type `./setup.sh`
 - Type `./build.sh`
 - Type `./launch.sh`
 - This should launch the visualiser
4. If you want to see additional windows uncomment the mappings in the simple_tracker_ui_launch.py file in the simple_tracker_ui_launch/launch folder

#### UI TODO:

Take a look at the image_visualiser.py file to see what topics are available for consumption

Add a new package/node from the `src` directory using the `ros2 pkg create....` command e.g. `ros2 pkg create --build-type ament_python simple_tracker_movie_player --dependencies rclpy image_transport cv_bridge sensor_msgs std_msgs python3-opencv`

Add your new project to the simple_tracker_launch.py file so that it will launch

run `./build.sh` to build the project
run `./launch.sh` to launch the project

That's it, best of luck!