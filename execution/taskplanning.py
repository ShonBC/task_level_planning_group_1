"""Takes user inputs to initialize planning environment and store them into a dictionary structure.

"""

# system_tracker: stores the user inputs into a dict structure. Contains the bins for each part, current agv's and their
# respective assembly stations
system_tracker = {
    "bins": {"red battery": {"parts": "0", "location": "1"}, "blue battery": {"parts": "0", "location": "1"},
             "blue sensor": {"parts": "0", "location": "1"}, "green regulator": {"parts": "0", "location": "1"}},
    "agv": {"selected": "", "current station": "", "remaining agv's": ("0", "0", "0")},
    "kit": {"red battery": "0", "blue battery": "0", "blue sensor": "0", "green regulator": "0"},
    "kit total": "0"}


def iterate(bin_no: list, entry):
    """ Will iterate through list and return whether the entry entered is in the list.

    Args:
        bin_no (list): list being compared
        entry ([type]): user input (string)

    Returns:
        Boolean: return true if entry is in bin_no list.
    """

    for elt in bin_no:
        if elt == entry:
            return True


def modify_bin(bin_no: tuple, entry: int):
    """ Modify the bin in the bin_no tuple and return it.

    Args:
        bin_no (tuple): tuple containing selected bin numbers. Used for display purposes.
        entry (int): selected bin entry

    Returns:
        tuple: modified tuple bin_no
    """

    bin_no = list(bin_no)
    bin_no.remove(entry)
    bin_no = tuple(bin_no)
    return bin_no


def try_again(*args):
    """
    Will print message reminding user about the proper entries.
    """

    print("Please Try Again!")
    for arg in args:
        print(f'The only valid entries are {arg}', end='')
    print('\n')


def user_inputs():
    """ Program that will ask for user input starts here. Will be used for further processing.

    Returns:
        system_tracker: updated dict data structure which will perform actions based on dictionary.
    """

    # part_entry: Flags whether number of parts entered is proper as required in the specifications.
    # If flag is true, the input entry is correct. Otherwise, try again.
    part_entry = False
    while not part_entry:
        # Four entries are required. User must try again otherwise.
        try:
            red_battery, blue_battery, blue_sensor, green_regulator = input(
                "Q1. Number of red battery/blue battery/blue "
                "sensor/green regulator in bins [0-5]: ").split()
        except ValueError:
            print('Enter 4 integers.')
            continue

        # Will check if user enters integer between 0 and 5 and will flag True if all conditions are met.
        if red_battery.isdigit() and blue_battery.isdigit() and blue_sensor.isdigit() and green_regulator.isdigit() and \
                (0 <= int(red_battery) < 6) and (0 <= int(blue_battery) < 6) and (0 <= int(blue_sensor) < 6) and \
                (0 <= int(green_regulator) < 6):
            part_entry = True

            # Check if number of parts in all of the bins is 0. If so program terminates.
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

    # bin_no used to check which bins to use for each part. Tuple used for display purposes shown below. Will be
    # updated from Q2-Q5.
    bin_no = (1, 2, 3, 4, 5, 6, 7, 8)
    if int(red_battery) > 0:  # Question will only be asked if number of red batteries is greater than 0.
        proper_entry = False  # proper_entry is similar to parts_entry.
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
    agv_location = "agv"  # Used to concatenate with the agv number mentioned in Q6.
    while not proper_entry:
        agv_no = input("Q6. AGV to use for kitting [1-4]: ")
        if agv_no.isdigit() and 1 <= int(agv_no) < 5:
            proper_entry = True
            agv_location += agv_no  # Will append to agv_no which was asked in Q6.
        else:
            try_again((1, 2, 3, 4))

    # Store Selected agv location in selected key of system tracker
    system_tracker["agv"]["selected"] = agv_location
    agv = ["agv1", "agv2", "agv3", "agv4"]  # agv creates list of agv locations.
    # Which will be used to store the remaining agv locations.
    for i in agv:
        if i == agv_location:
            agv.remove(i)

    system_tracker["agv"]["remaining agv's"] = tuple(agv)  # in the remaining agv's key of agv key in system_tracker.
    # Stations for selected agv are created. First element stores the associated kitting station for the selected agv.
    # Next two elements store the two assembly stations for the associated agv.
    # as1 and as2 are used for agv1 and agv2. as3 and as4 are used for agv3 and agv4.
    stations = ["ks" + agv_no]
    if agv_no == "1" or agv_no == "2":
        stations.append("as1")
        stations.append("as2")
    else:
        stations.append("as3")
        stations.append("as4")
    # Stations uses a List structure for display purposes as shown in the next question.
    proper_entry = False
    while not proper_entry:
        agv_location = input("Q7. Current location of {} {}: ".format(agv_location, stations))
        proper_entry = iterate(stations, agv_location)
        if not proper_entry:
            try_again(tuple(stations))
        else:
            proper_entry = True

    # Current agv location is stored in the current station key of agv key in system tracker.
    system_tracker["agv"]["current station"] = agv_location

    stations.pop(0)  # Remove associated kitting station for next question.
    proper_entry = False
    while not proper_entry:
        as_sta = input(f"Q8. Station to deliver parts {stations}: ")
        proper_entry = iterate(stations, as_sta)
        if not proper_entry:
            try_again(tuple(stations))

    # Note: Two flags were set. Default is False
    proper_entry = False        # Check if input entered is integer between 0 and 5.
    correct_entry = False       # Check if integer of parts in kit is greater than parts in bin.
    while not proper_entry or not correct_entry:
        # Ask for number of parts currently in kit. Like Q1, user must make four entries.
        try:
            red_bat_kit, blue_bat_kit, blue_sen_kit, green_reg_kit = input(
                "Q9. Number of red battery/blue battery/blue "
                "sensor/green regulator in kit [0-5]: ").split()
        except ValueError:
            print('Enter 4 integers.')
            continue
        # Will scan if all four numbers are integers between 1 and 5. If True, proceed to next step.
        # Otherwise, try again.
        if red_bat_kit.isdigit() and blue_bat_kit.isdigit() and blue_sen_kit.isdigit() and green_reg_kit.isdigit() \
        and 0 <= int(red_bat_kit) < 6 and 0 <= int(blue_bat_kit) < 6 and 0 <= int(blue_sen_kit) < 6 and \
        0 <= int(green_reg_kit) < 6:
            proper_entry = True
            # If the user mentioned that there will be no parts in the kit, program terminates with Kit completed message.
            if int(red_bat_kit) == 0 and int(blue_bat_kit) == 0 and int(blue_sen_kit) == 0 and int(
                    green_reg_kit) == 0:
                print("Kit completed... exit")
                exit()
            # If the number of parts the user entered for any part exceeds the number of available parts in the bin,
            # try again.
            # Note: Since the inputs entered are integers from 0 to 5, a different message is printed.
            if int(red_bat_kit) > int(red_battery) or int(blue_bat_kit) > int(blue_battery) or \
                    int(blue_sen_kit) > int(blue_sensor) or int(green_reg_kit) > int(green_regulator):
                print("Please Try Again. Number of parts entered exceeds number of available parts in bin.")
            else:
                correct_entry = True
        else:
            proper_entry = False

        # Will call try again function if user input enters anything but the required integers.
        if not proper_entry:
            try_again((0, 1, 2, 3, 4, 5))

            # Stores the number of parts in the kit to the respective location in system_tracker.
    system_tracker["kit"]["red battery"] = red_bat_kit
    system_tracker["kit"]["blue battery"] = blue_bat_kit
    system_tracker["kit"]["blue sensor"] = blue_sen_kit
    system_tracker["kit"]["green regulator"] = green_reg_kit
    # In addition system_tracker will store the sum total of parts in the kit
    system_tracker["kit total"] = str(int(red_bat_kit) + int(blue_bat_kit) + int(blue_sen_kit) + int(green_reg_kit))


    return system_tracker
