ENPM809E - Python Applications for Robotics

Group 1: Souvik Pramanik, Brenda Scheufele, Shon Cortes

July 12, 2021

RWA2 - Task-level Planning with PDDL

# task_level_planning_group_1
This assignment revolves around robot automated kit building which consists of picking up parts stored in bins with a gantry robot and placing them into trays located on automated guided vehicles (AGVs). We simulate kitting using Python and PDDL.
  
To run this program you must have python3 installed as well as be able to run the planning program tool PDDL.  

Both *.ppdl files in 'planning' folder should be placed in the same folder as the popf3-clp execution file on your computer before running this program.  Modules that need to be imported are:

import subprocess

The main file to run the program is ‘execution.py’.

User Inputs: 

You must enter positive integer values (separated by a ‘space’ if required) for the following requested amounts: 

-Number of red batteries/blue batteries/blue sensors/green regulators (must be 5 or less)
-Bin number for each part (program will request one at a time, you must pick from list given)
-AGV to use for kitting (choose one from 1,2,3,4)

You must enter the AGV location and station to deliver parts to exactly from the given list (actual list will depend on AGV choice):
-AGV location [as1, as2, ks ]
-Station to deliver parts [as1, as2]

You must enter positive integer values (separated by a ‘space’) for the following requested amounts: 
-Number of red battery/blue battery/blue sensor/green regulator in kit (must be 5 or less)


If you make an error you will be asked to re-enter until it is a valid input.

The program will take the user inputs, create a plan for execution, and output robot actions to assemble the desired kit.


