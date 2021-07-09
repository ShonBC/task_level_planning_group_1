"""
This module creates a new PDDL file from the original.

 - Open the original PDDL problem file
 - Store its content in a list
 - Update this list from user inputs
 - Iterate over this updated list and write the list content in a new file
"""

user_inputs_file = ['5', '5', '5', '5', 'bin1', 'bin2', 'bin3', 'bin4', 'agv2',
                    'as2', ('agv1', 'agv3', 'agv4'), '2', '2', '1', '1', '6']


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
    initial_red_battery_quantity = user_inputs_file[0]
    initial_blue_battery_quantity = user_inputs_file[1]
    initial_blue_sensor_quantity = user_inputs_file[2]
    initial_green_regulator_quantity = user_inputs_file[3]

    # bin and part type information
    red_battery_bin = user_inputs_file[4]
    blue_battery_bin = user_inputs_file[5]
    blue_sensor_bin = user_inputs_file[6]
    green_regulator_bin = user_inputs_file[7]

    # agv information
    used_agv = user_inputs_file[8]
    used_agv_station = user_inputs_file[9]
    at_ks = user_inputs_file[10]

    # required part quantity information
    required_red_battery_quantity = user_inputs_file[11]
    required_blue_battery_quantity = user_inputs_file[12]
    required_blue_sensor_quantity = user_inputs_file[13]
    required_green_regulator_quantity = user_inputs_file[14]

    kit_final_qty = user_inputs_file[15]

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
            output_list[i] = "        (bin-has-parttype " + blue_sensor_bin + " blue_sensor)\n"
        if 'bin-has-parttype' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '        (bin-has-parttype ' + green_regulator_bin + ' green_regulator)\n'
        if 'bin-has-parttype' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '        (bin-has-parttype ' + blue_battery_bin + ' blue_battery)\n'
        if 'bin-has-parttype' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '        (bin-has-parttype ' + red_battery_bin + ' red_battery)\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'red_battery' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin red_battery ' + red_battery_bin + ')'\
                             + initial_red_battery_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'blue_battery' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin blue_battery ' + blue_battery_bin + ')' \
                             + initial_blue_battery_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'blue_sensor' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin blue_sensor ' + blue_sensor_bin + ')' \
                             + initial_blue_sensor_quantity + ')\n'
        if 'parttype-quantity-in-bin' in output_list[i] and 'green_regulator' in output_list[i]:
            output_list[i] = '(=(parttype-quantity-in-bin green_regulator ' + green_regulator_bin + ')' \
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
    # absolute path to the PDDL problem file
    input_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-problem.pddl"
    # absolute path to the new PDDL problem file
    output_file_path = "/home/brenda/Desktop/popf-tif-clp/planner/debug/popf/rwa2-updated-problem.pddl"
    output_list = read_file(input_file_path)
    update_problem_states(user_inputs_file)
    write_new_problem_file(output_file_path)
