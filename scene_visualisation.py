# BSD 3-Clause License
#
# Copyright (C) 2024, LAAS-CNRS.
# Copyright note valid unless otherwise stated in individual files.
# All rights reserved.

from param_parser import ParamParser
from visualizer import create_viewer, add_sphere_to_viewer
from wrapper_panda import PandaWrapper

# Creating the robot
robot_wrapper = PandaWrapper(capsule=True)
rmodel, cmodel, vmodel = robot_wrapper.create_robot()

pp = ParamParser("scenes.yaml", 1)

cmodel = pp.add_collisions(rmodel, cmodel)
vis = create_viewer(rmodel, cmodel, cmodel)

vis.display(pp.get_initial_config())
