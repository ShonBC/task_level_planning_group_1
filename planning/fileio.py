"""
This module creates a new PDDL file from the original.

 - Open the original PDDL problem file
 - Store its content in a list
 - Update this list from user inputs
 - Iterate over this updated list and write the list content in a new file
"""
import execution.taskplanning as task

# system_tracker = {"bins": {"red battery": {"parts": "3", "location": "1"}, "blue battery": {"parts": "2", "location": "2"},
#                           "blue sensor": {"parts": "1", "location": "3"}, "green regulator": {"parts": "5", "location": "4"}},
#                  "agv": {"selected": "agv2", "current station": 'as1', "remaining stations": ('agv1', 'agv3', 'agv4')},
#                  "kit":  {"red battery": "2", "blue battery": "2", "blue sensor": "1", "green regulator": "1"},
#                  "kit total": "6"}

def write_new_problem_file(path):
    """
    Read a list and write its content into a new file
    :param path: Absolute path for the output file
    :type path: str
    :return: None
    :rtype: None
    """
    with open(path, 'w') as writer:
        for item in output_list:
            # The indentation in the file needs some work but this is fine
            writer.write(item)


def read_file(path):
    """
    Open a file and store its content in a list
    :param path: Absolute path for the file to open
    :type path: str
    :return: List of each line of the file
    :rtype: List
    """

    with open(path, 'r') as opened_file:
        state_list = []
        lines = opened_file.readlines()

        for line in lines:
            state_list.append(line)
            # print(line)

        return state_list


def update_problem_states(user_inputs_file):
    """
    Read a list and update some of its contents from user inputs
    :return: None
    :rtype: None
    """
    agv_is_at_ks_counter = 0

    # ----------------------------
    # start data from user inputs
    # We assume the following information comes from user inputs
    initial_red_battery_quantity = system_tracker["bins"]["red battery"]["parts"]
    # print(initial_red_battery_quantity)
    initial_blue_battery_quantity = system_tracker["bins"]["blue battery"]["parts"]
    initial_blue_sensor_quantity = system_tracker["bins"]["blue sensor"]["parts"]
    initial_green_regulator_quantity = system_tracker["bins"]["green regulator"]["parts"]

    # bin and part type information
    red_battery_bin = system_tracker["bins"]["red battery"]["location"]
    blue_battery_bin = system_tracker["bins"]["blue battery"]["location"]
    blue_sensor_bin = system_tracker["bins"]["blue sensor"]["location"]
    green_regulator_bin = system_tracker["bins"]["green regulator"]["location"]

    # agv information
    used_agv = system_tracker["agv"]["selected"]
    used_agv_station = system_tracker["agv"]["current station"]
    at_ks = system_tracker["agv"]["remaining agv's"]

    # required part quantity information
    required_red_battery_quantity = system_tracker["kit"]["red battery"]
    required_blue_battery_quantity = system_tracker["kit"]["blue battery"]
    required_blue_sensor_quantity = system_tracker["kit"]["blue sensor"]
    required_green_regulator_quantity = system_tracker["kit"]["green regulator"]

    kit_final_qty = system_tracker.get("kit total")

    # end data from user inputs

    # update predicates and attributes from user inputs
    for i in range(len(output_list)):
        print("output list", output_list)
        if 'agv-is-at-as' in output_list[i]:
            output_list[i] = "        (agv-is-at-as "+used_agv+" "+used_agv_station+")\n"
        if 'agv-is-not-at-ks' in output_list[i]:
            output_list[i] = "        (agv-is-not-at-ks " + used_agv + ")\n"
        if 'agv-is-at-ks' in output_list[i]:
            if agv_is_at_ks_counter == 0:
                output_list[i] = "        (agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            elif agv_is_at_ks_counter == 1:
                output_list[i] = "        (agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            elif agv_is_at_ks_counter == 2:
                output_list[i] = "        (agv-is-at-ks " + at_ks[agv_is_at_ks_counter]+")\n"
            agv_is_at_ks_counter += 1
        if 'bin-has-parttype' in output_list[i] and 'blue_sensor' in output_list[i]:
            output_list[i] = "        (bin-has-parttype bin" + blue_sensor_bin + " blue_sensor)\n"
        if 'bin-has-parttype' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '        (bin-has-parttype bin' + green_regulator_bin + ' green_regulator)\n'
        if 'bin-has-parttype' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '        (bin-has-parttype bin' + blue_battery_bin + ' blue_battery)\n'
        if 'bin-has-parttype' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '        (bin-has-parttype bin' + red_battery_bin + ' red_battery)\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin red_battery bin' + red_battery_bin + ')'\
                             + initial_red_battery_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin blue_battery bin' + blue_battery_bin + ')' \
                             + initial_blue_battery_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'blue_sensor' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin blue_sensor bin' + blue_sensor_bin + ')' \
                             + initial_blue_sensor_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin green_regulator bin' + green_regulator_bin + ')' \
                             + initial_green_regulator_quantity + ')\n'
        if 'required-parttype-qty-on-agv' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '(=(required-parttype-qty-on-agv red_battery ' + used_agv + ')'\
                             + required_red_battery_quantity + ')\n'
        if 'required-parttype-qty-on-agv' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '(=(required-parttype-qty-on-agv blue_battery ' + used_agv + ')'\
                             + required_blue_battery_quantity + ')\n'
        if 'required-parttype-qty-on-agv' in output_list[i] and 'blue_sensor' in output_list[i]:
            output_list[i] = '(=(required-parttype-qty-on-agv blue_sensor ' + used_agv + ')'\
                             + required_blue_sensor_quantity + ')\n'
        if 'required-parttype-qty-on-agv' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '(=(required-parttype-qty-on-agv green_regulator ' + used_agv + ')' \
                             + required_green_regulator_quantity + ')\n'
        if 'kit-final-part-qty' in output_list[i]:
            output_list[i] = '(=(kit-final-part-qty)' + kit_final_qty + ')\n'
        if 'problem rwa2-problem'in output_list[i]:
            output_list[i] = '(define (problem rwa2-updated-problem)\n'


if __name__ == '__main__':
    system_tracker = task.user_inputs()
    print(system_tracker)
    # absolute path to the PDDL problem file
    input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
    # input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
    # input_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"

    # absolute path to the new PDDL problem file
    output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
    # output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
    # output_file_path = "/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
    output_list = read_file(input_file_path)
    update_problem_states(system_tracker)
    write_new_problem_file(output_file_path)
