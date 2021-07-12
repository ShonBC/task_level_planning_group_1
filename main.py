from execution import taskplanning as task
from planning import fileio as fileio
from planning import pythonshell as shell
from execution import execution as execute
from classes import gantry_robot as gantry
from classes import ground_robot as ground

# absolute path to the PDDL problem file
# input_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
# input_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"

# absolute path to the new PDDL problem file
# output_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
#output_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"

# root directory of the planner
# planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'
planner_folder = '/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf'
#planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'



if __name__ == '__main__':

    # Instantiate ground and gantry robots
    ground_robot_obj = ground.Ground('ground robot', 1.0, ['action 1', 'action 2'], 1.0, 'NIST')
    gantry_robot_obj = gantry.Gantry('gantry robot', 1.0, ['action 1', 'action 2'], 1.0, 2.0, 10, 11, 'NIST')

    # Take user inputs, generates system tracker
    system_tracker = task.user_inputs()

    # Generate new problem pddl file
    fileio.generate(input_file_path, output_file_path, system_tracker)

    # Run the pddl planner with the updated problem file
    moves = shell.plan(planner_folder)
    # print(moves)
    print('Begin execution: ')
    execute.execute_plan(moves, ground_robot_obj, gantry_robot_obj, system_tracker)
