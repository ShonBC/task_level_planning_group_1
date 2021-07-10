import execution.taskplanning as task
import planning.fileio as fileio
import planning.pythonshell as shell
import execution.execution as execute
import classes.gantry_robot as gantry
import classes.ground_robot as ground

# absolute path to the PDDL problem file
# input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
# input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
input_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"

# absolute path to the new PDDL problem file
# output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
# output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
output_file_path = "/home/luna/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"

# root directory of the planner
# planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'
planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'
# planner_folder = '/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf'



if __name__ == '__main__':

    # Instantiate ground and gantry robots
    ground_robot_obj = ground.Ground('ground robot', 2.0, ['s', 'a'], 1.0, 'NIST')
    gantry_robot_obj = gantry.Gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')

    # Take user inputs
    task.user_inputs()

    # Generate new problem pddl file
    fileio.generate(input_file_path, output_file_path)

    # Run the pddl planner with the updated problem file
    plan = shell.plan(planner_folder)
    
    execute.execute_plan(plan, ground_robot_obj, gantry_robot_obj, task.system_tracker)