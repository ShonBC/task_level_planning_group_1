import execution.taskplanning as task
import planning.fileio as fileio
import planning.pythonshell as shell
import execution.execution as execute

if __name__ == '__main__':

    ground_robot_obj = execute.Ground('Shon', 1, 2)
    gantry_robot_obj = []