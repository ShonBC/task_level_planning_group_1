"""Takes user inputs to initialize planning environment and store them into a dictionary structure.
"""

system_tracker = {
    "bins": {"red battery": {"parts": "0", "location": "1"}, "blue battery": {"parts": "0", "location": "1"},
             "blue sensor": {"parts": "0", "location": "1"}, "green regulator": {"parts": "0", "location": "1"}},
    "agv": {"selected": "", "current station": "", "remaining agv's": ("0", "0", "0")},
    "kit": {"red battery": "0", "blue battery": "0", "blue sensor": "0", "green regulator": "0"},
    "kit total": "0"}


# Will iterate through list and return whether the entry entered is in the list
def iterate(bin_no: list, entry):
    """[summary]

    Args:
        bin_no (list): [description]
        entry ([type]): [description]

    Returns:
        [type]: [description]
    """

    for elt in bin_no:
        if elt == entry:
            return True


# Will modify the bin in the bin_no tuple and return it.
def modify_bin(bin_no: tuple, entry: int):
    """[summary]

    Args:
        bin_no (tuple): [description]
        entry (int): [description]

    Returns:
        [type]: [description]
    """

    bin_no = list(bin_no)
    bin_no.remove(entry)
    bin_no = tuple(bin_no)
    return bin_no


# Will print message reminding user about the proper entries.
def try_again(*args):
    """[summary]
    """

    print("Please Try Again!")
    for arg in args:
        print(f'The only valid entries are {arg}', end='')
    print('\n')


# Program that will ask for user input starts here.
def user_inputs():
    """[summary]

    Returns:
        [type]: [description]
    """
    # print("Initial System Tracker")
    # print(system_tracker)
    # part_entry: Flags whether number of parts entered is proper as required in the specifications.
    # If flag is true, the input entry is correct. Otherwise, try again.
    part_entry = False
    while not part_entry:
        try:
            red_battery, blue_battery, blue_sensor, green_regulator = input(
                "Q1. Number of red battery/blue battery/blue "
                "sensor/green regulator in bins [0-5]: ").split()
        except ValueError:
            print('Enter 4 integers.')
            continue
        print(red_battery.isdigit())
        print(blue_battery.isdigit())
        print(blue_sensor.isdigit())
        print(green_regulator.isdigit())

        # Will check if user enters integer between 0 and 5 and will proceed as follows.
        if red_battery.isdigit() and blue_battery.isdigit() and blue_sensor.isdigit() and green_regulator.isdigit() and \
                (0 <= int(red_battery) < 6) and (0 <= int(blue_battery) < 6) and (0 <= int(blue_sensor) < 6) and \
                (0 <= int(green_regulator) < 6):
            part_entry = True
            if int(red_battery) == 0 and int(blue_battery) == 0 and int(blue_sensor) == 0 and int(green_regulator) == 0:
                print("Kit has no parts ... exit")
                exit()
        else:
            try_again((0, 1, 2, 3, 4, 5))

        # Store number of parts in bins in the bins key of system_tracker.
        system_tracker["bins"]["red battery"]["parts"] = red_battery
        system_tracker["bins"]["blue battery"]["parts"] = blue_battery
        system_tracker["bins"]["blue sensor"]["parts"] = blue_sensor
        system_tracker["bins"]["green regulator"]["parts"] = green_regulator

    bin_no = (1, 2, 3, 4, 5, 6, 7, 8)  # Tuple created for display purposes shown below.
    if int(red_battery) > 0:  # Question will only be asked if number of red batteries is greater than 0.
        proper_entry = False
        while not proper_entry:
            red_bat_bin = input(f"Q2. Bin for red batteries {bin_no}: ")
            if red_bat_bin.isdigit() and 1 <= int(red_bat_bin) < 9:
                proper_entry = True
                bin_no = modify_bin(bin_no, int(red_bat_bin))  # Will remove the user input entered from the tuple.


            else:
                try_again(bin_no)

        system_tracker["bins"]["red battery"][
            "location"] = red_bat_bin  # Stores bin_no entry in bins red battery location key.

    # Prompts the same questions for blue battery, blue sensor and green regulators.
    if int(blue_battery) > 0:
        proper_entry = False
        while not proper_entry:
            blue_bat_bin = input(f"Q3. Bin for blue batteries {bin_no}: ")
            if blue_bat_bin.isdigit():
                proper_entry = iterate(bin_no, int(blue_bat_bin))

            if not proper_entry:
                try_again(bin_no)

        bin_no = modify_bin(bin_no, int(blue_bat_bin))
        system_tracker["bins"]["blue battery"]["location"] = blue_bat_bin

    if int(blue_sensor) > 0:
        proper_entry = False
        while not proper_entry:
            blue_sen_bin = input(f"Q4. Bin for blue sensors {bin_no}: ")
            if blue_sen_bin.isdigit():
                proper_entry = iterate(bin_no, int(blue_sen_bin))

            if not proper_entry:
                try_again(bin_no)

        bin_no = modify_bin(bin_no, int(blue_sen_bin))
        system_tracker["bins"]["blue sensor"]["location"] = blue_sen_bin

    if int(green_regulator) > 0:
        proper_entry = False
        while not proper_entry:
            green_reg_bin = input(f"Q5. Bin for green regulators {bin_no}: ")
            if green_reg_bin.isdigit():
                proper_entry = iterate(bin_no, int(green_reg_bin))

            if not proper_entry:
                try_again(bin_no)

        bin_no = modify_bin(bin_no, int(green_reg_bin))
        system_tracker["bins"]["green regulator"]["location"] = green_reg_bin

    proper_entry = False
    agv_location = "agv"  # Used to concatenate with the agv number mentioned in the
    while not proper_entry:
        agv_no = input("Q6. AGV to use for kitting [1-4]: ")
        if agv_no.isdigit() and 1 <= int(agv_no) < 5:
            proper_entry = True
            agv_location += agv_no
        else:
            try_again((1, 2, 3, 4))

    system_tracker["agv"]["selected"] = agv_location
    agv = ["agv1", "agv2", "agv3", "agv4"]
    for i in agv:
        if i == agv_location:
            agv.remove(i)

    system_tracker["agv"]["remaining agv's"] = tuple(agv)
    stations = ["ks" + agv_no]
    if agv_no == "1" or agv_no == "2":
        stations.append("as1")
        stations.append("as2")
    else:
        stations.append("as3")
        stations.append("as4")

    proper_entry = False
    while not proper_entry:
        agv_location = input("Q7. Current location of {} {}: ".format(agv_location, stations))
        proper_entry = iterate(stations, agv_location)
        if not proper_entry:
            try_again(tuple(stations))
        else:
            proper_entry = True
    system_tracker["agv"]["current station"] = agv_location

    ks = stations.pop(0)
    proper_entry = False
    while not proper_entry:
        as_sta = input(f"Q8. Station to deliver parts {stations}: ")
        proper_entry = iterate(stations, as_sta)
        if not proper_entry:
            try_again(tuple(stations))

    proper_entry = False
    while not proper_entry:
        try:
            red_bat_kit, blue_bat_kit, blue_sen_kit, green_reg_kit = input(
                "Q9. Number of red battery/blue battery/blue "
                "sensor/green regulator in kit [0-5]: ").split()
        except ValueError:
            print('Enter 4 integers.')
            continue

        if red_bat_kit.isdigit() and blue_bat_kit.isdigit() and blue_sen_kit.isdigit() and green_reg_kit.isdigit():
            if 0 <= int(red_bat_kit) < 6 and 0 <= int(blue_bat_kit) < 6 and 0 <= int(blue_sen_kit) < 6 and 0 <= \
                    int(green_reg_kit) < 6:
                proper_entry = True
                if int(red_bat_kit) == 0 and int(blue_bat_kit) == 0 and int(blue_sen_kit) == 0 and int(
                        green_reg_kit) == 0:
                    print("Kit completed... exit")
                    exit()
                if int(red_bat_kit) <= int(red_battery) and int(blue_bat_kit) <= int(blue_battery) and \
                        int(blue_sen_kit) <= int(blue_sensor) and int(green_reg_kit) <= int(green_regulator):
                    pass
                else:
                    print("Please Try Again. Number of parts entered exceeds number of available parts in bin.")
                    proper_entry = False

        else:
            try_again((0, 1, 2, 3, 4, 5))

    system_tracker["kit"]["red battery"] = red_bat_kit
    system_tracker["kit"]["blue battery"] = blue_bat_kit
    system_tracker["kit"]["blue sensor"] = blue_sen_kit
    system_tracker["kit"]["green regulator"] = green_reg_kit
    system_tracker["kit total"] = str(int(red_bat_kit) + int(blue_bat_kit) + int(blue_sen_kit) + int(green_reg_kit))

    # Add in the call to fileio.py to set user inputs from list into .pddl files.
    # gantry.main()
    # ground.main()
    # industrial_robot.main()
    # print("After Updating System Tracker")
    # print(system_tracker)
    return system_tracker
