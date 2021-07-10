import execution.taskplanning as task
import planning.fileio as fileio
import planning.pythonshell as shell
import execution.execution as execute

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

    task.user_inputs()
    fileio.generate(input_file_path, output_file_path)
    ground_robot_obj = execute.Ground('Shon', 1, 2)
    gantry_robot_obj = []