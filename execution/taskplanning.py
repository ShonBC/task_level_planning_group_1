    """Takes user inputs to initialize planning environment
    """
    
import fileio
import industrial_robot
import ground
import gantry

system_tracker = {"bins": {"red battery": {"parts": 0, "location": 1}, "blue battery": {"parts": 0, "location": 1},
                           "blue sensor": {"parts": 0, "location": 1}, "green regulator": {"parts": 0, "location": 1}},
                  "agv": {"selected": "", "current station": "", "remaining stations": ()},
                  "kit":  {"red battery": 0, "blue battery": 0, "blue sensor": 0, "green regulator": 0},
                  "kit total": 0}


def iterate(bin_no: list, entry):
    for elt in bin_no:
        if elt == entry:
            return True


def modify_bin(bin_no: tuple, entry: int):
    bin_no = list(bin_no)
    bin_no.remove(entry)
    bin_no = tuple(bin_no)
    return bin_no


def try_again(*args):
    print("Please Try Again!")
    for arg in args:
        print(f'The only valid entries are {arg}', end='')
    print('\n')


def main():
    print("Initial System Tracker")
    print(system_tracker)
    # f = open("test.txt")  # open file in current directory
    part_entry = False
    while not part_entry:
        red_battery, blue_battery, blue_sensor, green_regulator = input("Q1. Number of red battery/blue battery/blue "
                                                                        "sensor/green regulator in bins [0-5]: ").split()
        if red_battery.isdigit() and blue_battery.isdigit() and blue_sensor.isdigit() and green_regulator.isdigit() and \
                (0 <= int(red_battery) < 6) and (0 <= int(blue_battery) < 6) and (0 <= int(blue_sensor) < 6) and \
                (0 <= int(green_regulator) < 6):
            part_entry = True
        else:
            try_again(0, 1, 2, 3, 4, 5)
        system_tracker["bins"]["red battery"]["parts"] = red_battery
        system_tracker["bins"]["blue battery"]["parts"] = blue_battery
        system_tracker["bins"]["blue sensor"]["parts"] = blue_sensor
        system_tracker["bins"]["green regulator"]["parts"] = green_regulator

    bin_no = (1, 2, 3, 4, 5, 6, 7, 8)
    if int(red_battery) > 0:
        proper_entry = False
        while not proper_entry:
            red_bat_bin = input(f"Q2. Bin for red batteries {bin_no}: ")
            if red_bat_bin.isdigit() and 1 <= int(red_bat_bin) < 9:
                proper_entry = True
                bin_no = modify_bin(bin_no, int(red_bat_bin))


            else:
                try_again(bin_no)

        system_tracker["bins"]["red battery"]["location"] = red_bat_bin

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
    agv_location = "agv"
    while not proper_entry:
        agv_no = input("Q6. AGV to use for kitting [1-4]: ")
        if agv_no.isdigit() and 1 <= int(agv_no) < 5:
            proper_entry = True
            agv_location += agv_no
        else:
            try_again(1, 2, 3, 4)

    agv_loc_no = "agv" + agv_no
    system_tracker["agv"]["selected"] = agv_loc_no
    stations = ["ks" + agv_no]
    if agv_no == "1" or agv_no == "2":
        stations.append("as1")
        stations.append("as2")
    else:
        stations.append("as3")
        stations.append("as4")

    proper_entry = False
    while not proper_entry:
        agv_location = input("Q7. Current location of {} {}: ".format(agv_loc_no, stations))
        proper_entry = iterate(stations, agv_location)
        if not proper_entry:
            try_again(tuple(agv_location))
        else:
            proper_entry = True
    system_tracker["agv"]["current station"] = agv_location

    ks = stations.pop(0)
    system_tracker["agv"]["remaining stations"] = tuple(stations)
    proper_entry = False
    while not proper_entry:
        as_sta = input(f"Q8. Station to deliver parts {stations}: ")
        proper_entry = iterate(stations, agv_location)
        if not proper_entry:
            try_again(tuple(stations))

    if int(red_battery) == 0 and int(blue_battery) == 0 and int(blue_sensor) == 0 and int(green_regulator) == 0:
        print("Kit has no parts ... exit")
        return None

    proper_entry = False
    while not proper_entry:
        red_bat_kit, blue_bat_kit, blue_sen_kit, green_reg_kit = input("Q9. Number of red battery/blue battery/blue "
                                                                       "sensor/green regulator in kit [0-5]: ").split()
        if red_bat_kit.isdigit() and blue_bat_kit.isdigit() and blue_sen_kit.isdigit() and green_reg_kit.isdigit():
            if 0 <= int(red_bat_kit) < 6 and 0 <= int(blue_bat_kit) < 6 and 0 <= int(blue_sen_kit) < 6 and 0 <= \
                    int(green_reg_kit) < 6:
                if int(red_bat_kit) < int(red_battery) and int(blue_bat_kit) < int(blue_battery) and \
                        int(blue_sen_kit) < int(blue_sensor) and int(green_reg_kit) < int(green_regulator):
                    proper_entry = True
                else:
                    print("Please Try Again. Number of parts entered exceeds number of available parts in bin.")

        if not proper_entry:
            try_again(0, 1, 2, 3, 4, 5)

    system_tracker["kit"]["red battery"] = red_bat_kit
    system_tracker["kit"]["blue battery"] = blue_bat_kit
    system_tracker["kit"]["blue sensor"] = blue_sen_kit
    system_tracker["kit"]["green regulator"] = green_reg_kit
    system_tracker["kit total"] = str(int(red_bat_kit) + int(blue_bat_kit) + int(blue_sen_kit) + int(green_reg_kit))


    # Add in the call to fileio.py to set user inputs from list into .pddl files.
    # gantry.main()
    # ground.main()
    # industrial_robot.main()
    print("After Updating System Tracker")
    print(system_tracker)
