# from task_level_planning_group_1.execution 
import taskplanning as task
import planning.fileio
import classes.industrial_robot as Industrial
import classes.ground_robot as Ground
import classes.gantry_robot as Gantry


def execute_plan(plan, ind_robot, gnd_robot, gnt_robot, system_tracker):

    for command in plan:
        
        agv = system_tracker["agv"]["selected"]

        #Check robot type
        if 'gantry' in command:
            robot = gnt_robot 

        elif 'ground' in command:
            robot = gnd_robot 

        elif 'industrial' in command:
            robot = gnd_robot

        # Check for part type and bin number
        if 'red' in command:
            part_type = 'red battery'
            bin_num = system_tracker["bins"]["red battery"]["location"]

        elif 'blue battery' in command:
            part_type = 'blue battery'
            bin_num = system_tracker["bins"]["blue battery"]["location"]

        elif 'blue sensor' in command:
            part_type = 'blue sensor'
            bin_num = system_tracker["bins"]["blue sensor"]["location"]

        elif 'green' in command:
            part_type = 'green regulator'
            bin_num = system_tracker["bins"]["green regulator"]["location"]

        if 'finger' in command:
            gripper = 'finger gripper'
        elif ' vacuum' in command:
            gripper = 'vacuum gripper'

        # Check for robot action
        if 'pick' in command:
            
            robot.pick_up(part_type, bin_num)

        elif 'put' in command:
            
            robot.put_down(part_type, bin_num)

        elif 'attach' in command:
            
            robot.attach_gripper(gripper)

        elif 'detach' in command:

            robot.detach_gripper(gripper)

        elif 'to bin' in command:

            robot.move_to_bin(bin_num)
        
        elif 'to agv' in command:
            robot.move_to_agv(system_tracker["agv"]["selected"]) 

        elif 'to gripper' in command:
            

        elif 'from agv' in command:
            robot.move_from_agv(system_tracker["agv"]["selected"])



    # print('kit complete')


task.main()

execute_plan()




