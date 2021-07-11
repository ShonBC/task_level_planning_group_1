ENPM809E - Python Applications for Robotics

Group 1: Souvik Pramanik, Brenda Scheufele, Shon Cortes

July 12, 2021


# task_level_planning_group_1
RWA2 - Task-level Planning with PDDL.  This assignment revolves around robot automated kit building which consists of picking up parts stored in bins with a gantry robot and placing them into trays located on automated guided vehicles (AGVs). We simulate kitting using Python and PDDL.
  
To run this program you must have python3 installed as well as be able to run the planning program tool PDDL.  

Both *.ppdl files in 'planning' folder should be placed in the same folder as the popf3-clp execution file on your computer before running this program.  

Modules that need to be imported are:   import subprocess

To run the program from your computer, go to the 'main.py' and modify the variables input_file_path, output_file_path, and planner_folder as in the example below:

Absolute path to the PDDL problem file:

input_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"

Absolute path to the updated PDDL file:

output_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"

Root directory of the planner:

planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'


Once the file paths are correct, run the program from 'main.py'. You will be asked for user inputs.


User Inputs: 

You must enter positive integer values (separated by a ‘space’ if required) for the following requested amounts: 

-Number of red batteries (program will request one at a time, you must pick from list given)
-AGV to use for kitting (choose one from 1,2,3,4)

You must enter the AGV location and station to deliver parts to exactly from the given list (actual list will depend on AGV choice):
-AGV location [as1, as2, ks ]
-Station to deliver parts [as1, as2]

You must enter positive integer values (separated by a ‘space’) for the following requested amounts: 
-Number of red battery/blue battery/blue sensor/green regulator in kit (must be 5 or less)


If you make an error you will be asked to re-enter until you give a valid input.

The program will take the user inputs, create a plan for execution, and output robot actions to assemble the desired kit.


