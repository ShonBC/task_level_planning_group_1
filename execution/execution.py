# from task_level_planning_group_1.execution 
import taskplanning as task

def read_plan():

    with open('filename') as file:
        
        # Place each line as an element in the plan list. Use ".rstrip" to remove white space.
        plan = [line.strip() for line in file]

    return plan

def execute_plan(plan):

    for command in plan:
        pass


task.main()

execute_plan(read_plan())




