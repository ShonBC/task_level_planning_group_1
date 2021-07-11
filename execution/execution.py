import gantry_robot as gantry
import ground_robot as ground

def execute_plan(moves, gnd_robot, gnt_robot, system_tracker):
    """[summary]

    Args:
        plan ([type]): [description]
        gnd_robot ([type]): [description]
        gnt_robot ([type]): [description]
        system_tracker ([type]): [description]
    """

    for command in moves:
        
        agv = system_tracker["agv"]["selected"]

        #Check robot type
        if 'gantry' in command:
            robot = gnt_robot 

        elif 'ground' in command:
            robot = gnd_robot 
        if 'bin1' in command:
            bin_num = 'bin 1'
        elif 'bin2' in command:
            bin_num = 'bin 2'
        elif 'bin3' in command:
            bin_num = 'bin 3'
        elif 'bin4' in command:
            bin_num = 'bin 4'
        elif 'bin5' in command:
            bin_num = 'bin 5'
        elif 'bin6' in command:
            bin_num = 'bin 6'
        elif 'bin7' in command:
            bin_num = 'bin 7'
        elif 'bin8' in command:
            bin_num = 'bin 8'

        # Check for part type and bin number
        if 'red' in command:
            part_type = 'red battery'
            bin_num = system_tracker["bins"]["red battery"]["location"]

        elif 'blue_battery' in command:
            part_type = 'blue battery'
            bin_num = system_tracker["bins"]["blue battery"]["location"]

        elif 'blue_sensor' in command:
            part_type = 'blue sensor'
            bin_num = system_tracker["bins"]["blue sensor"]["location"]

        elif 'green' in command:
            part_type = 'green regulator'
            bin_num = system_tracker["bins"]["green regulator"]["location"]

        if 'finger' in command:
            gripper = 'finger gripper'
        elif 'vacuum' in command:
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

        elif 'to_bin' in command:

            robot.move_to_bin(bin_num)
        
        elif 'to_agv' in command:
            robot.move_to_agv(agv) 

        elif 'move_to_gripper_station' in command:
            robot.move_to_gripper_station('gripper station')

        elif 'from_bin' in command:

            robot.move_from_bin(bin_num)

        elif 'from_agv' in command:
            robot.move_from_agv(agv)

        elif 'from_gripper' in command:
            robot.move_from_gripper_station('gripper station')

        elif 'discard' in command:
            robot.discard_part(part_type)

    print('kit complete')

if __name__ == '__main__':

    ground_robot_obj = ground.Ground('ground robot', 1.0, ['action 1', 'action 2'], 1.0, 'NIST')
    gantry_robot_obj = gantry.Gantry('gantry robot', 1.0, ['action 1', 'action 2'], 1.0, 2.0, 10, 11, 'NIST')

    moves = ['move_to_gripper_station gantry_robot gripper_station', 'move_to_gripper_station ground_robot gripper_station', 'drive_to_ks agv1 as1', 'attach_gripper gantry_robot vacuum_gripper gripper_station', 'attach_gripper ground_robot finger_gripper gripper_station', 'move_from_gripper_station gantry_robot vacuum_gripper gripper_station', 'move_from_gripper_station ground_robot finger_gripper gripper_station', 'move_to_bin gantry_robot bin4', 'move_to_bin ground_robot bin1', 'pick_up gantry_robot vacuum_gripper blue_battery bin4', 'pick_up ground_robot finger_gripper blue_sensor bin1', 'move_from_bin gantry_robot bin4 vacuum_gripper blue_battery', 'move_from_bin ground_robot bin1 finger_gripper blue_sensor', 'move_to_agv gantry_robot agv1 vacuum_gripper blue_battery', 'move_to_agv ground_robot agv1 finger_gripper blue_sensor', 'put_down gantry_robot blue_battery vacuum_gripper agv1', 'move_from_agv gantry_robot agv1', 'move_to_bin gantry_robot bin3', 'pick_up gantry_robot vacuum_gripper red_battery bin3', 'move_from_bin gantry_robot bin3 vacuum_gripper red_battery', 'move_to_agv gantry_robot agv1 vacuum_gripper red_battery', 'put_down gantry_robot red_battery vacuum_gripper agv1', 'move_from_agv gantry_robot agv1', 'put_down ground_robot blue_sensor finger_gripper agv1', 'move_from_agv ground_robot agv1', 'move_to_bin ground_robot bin2', 'pick_up ground_robot finger_gripper green_regulator bin2', 'move_from_bin ground_robot bin2 finger_gripper green_regulator', 'move_to_agv ground_robot agv1 finger_gripper green_regulator', 'put_down ground_robot green_regulator finger_gripper agv1', 'move_from_agv ground_robot agv1', 'move_to_bin ground_robot bin2', 'pick_up ground_robot finger_gripper green_regulator bin2', 'move_from_bin ground_robot bin2 finger_gripper green_regulator', 'move_to_agv ground_robot agv1 finger_gripper green_regulator', 'put_down ground_robot green_regulator finger_gripper agv1', 'move_from_agv ground_robot agv1', 'move_to_bin ground_robot bin1', 'pick_up ground_robot finger_gripper blue_sensor bin1', 'move_from_bin ground_robot bin1 finger_gripper blue_sensor', 'move_to_agv ground_robot agv1 finger_gripper blue_sensor', 'put_down ground_robot blue_sensor finger_gripper agv1', 'move_from_agv ground_robot agv1', 'set_kit_complete', 'drive_to_as agv1 as1']
    system_tracker = {"bins": {"red battery": {"parts": "3", "location": "1"}, "blue battery": {"parts": "2", "location": "2"},
                            "blue sensor": {"parts": "1", "location": "3"}, "green regulator": {"parts": "5", "location": "4"}},
                    "agv": {"selected": "agv2", "current station": 'as1', "remaining stations": ('agv1', 'agv3', 'agv4')},
                    "kit":  {"red battery": "2", "blue battery": "2", "blue sensor": "1", "green regulator": "1"},
                    "kit total": "6"}

    execute_plan(moves, ground_robot_obj, gantry_robot_obj, system_tracker)


