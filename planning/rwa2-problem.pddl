(define (problem rwa2-problem)
    (:domain rwa2-domain)
    (:objects
        blue_sensor green_regulator red_battery blue_battery - PartType
        vacuum_gripper finger_gripper - Gripper
        ground_robot gantry_robot - Robot
        agv1 agv2 agv3 agv4 - AGV
        bin1 bin2 bin3 bin4 bin5 bin6 bin7 bin8 - Bin
        as1 as2 as3 as4 - AssemblyStation
        gripper_station - GripperStation
    )
    (:init
        ;static predicates
        (=(kit-current-part-qty)0)

        (robot-is-at-home gantry_robot)
        (robot-is-at-home ground_robot)

        (robot-has-no-gripper gantry_robot)
        (robot-has-no-gripper ground_robot)

        (robot-is-not-at-gripper-station gantry_robot)
        (robot-is-not-at-agv gantry_robot)
        (robot-is-not-at-bin gantry_robot)

        (robot-is-not-at-gripper-station ground_robot)
        (robot-is-not-at-agv ground_robot)
        (robot-is-not-at-bin ground_robot)

        (robot-can-reach-bin gantry_robot bin3)
        (robot-can-reach-bin gantry_robot bin4)
        (robot-can-reach-bin gantry_robot bin7)
        (robot-can-reach-bin gantry_robot bin8)

        (robot-can-reach-bin ground_robot bin1)
        (robot-can-reach-bin ground_robot bin2)
        (robot-can-reach-bin ground_robot bin5)
        (robot-can-reach-bin ground_robot bin6)

        (agv-can-go-to-as agv1 as1)
        (agv-can-go-to-as agv1 as2)
        (agv-can-go-to-as agv2 as1)
        (agv-can-go-to-as agv2 as2)
        (agv-can-go-to-as agv3 as3)
        (agv-can-go-to-as agv3 as4)
        (agv-can-go-to-as agv4 as3)
        (agv-can-go-to-as agv4 as4)

        (gripper-is-at-station vacuum_gripper gripper_station)
        (gripper-is-at-station finger_gripper gripper_station)
        (gripper-can-grasp-parttype vacuum_gripper red_battery)
        (gripper-can-grasp-parttype vacuum_gripper blue_battery)
        (gripper-can-grasp-parttype finger_gripper green_regulator)
        (gripper-can-grasp-parttype finger_gripper blue_sensor)
        (gripper-is-empty vacuum_gripper)
        (gripper-is-empty finger_gripper)


        ;dynamic predicates (from user inputs)
        (agv-is-at-as agv1 as1)
        (agv-is-not-at-ks agv1)

        (agv-is-at-ks agv2)
        (agv-is-at-ks agv3)
        (agv-is-at-ks agv4)

        (bin-has-parttype bin1 blue_sensor)
        (bin-has-parttype bin2 green_regulator)
        (bin-has-parttype bin3 red_battery)
        (bin-has-parttype bin4 blue_battery)

        ;dynamic functions (from user inputs)
        (=(kit-final-part-qty)6)

        (=(current-parttype-qty-on-agv blue_sensor agv1)0)
        (=(current-parttype-qty-on-agv green_regulator agv1)0)
        (=(current-parttype-qty-on-agv red_battery agv1)0)
        (=(current-parttype-qty-on-agv blue_battery agv1)0)

        (=(parttype-quantity-in-bin blue_sensor bin1)5)
        (=(parttype-quantity-in-bin green_regulator bin2)5)
        (=(parttype-quantity-in-bin red_battery bin3)5)
        (=(parttype-quantity-in-bin blue_battery bin4)5)

        (=(required-parttype-qty-on-agv blue_sensor agv1)2)
        (=(required-parttype-qty-on-agv green_regulator agv1)2)
        (=(required-parttype-qty-on-agv red_battery agv1)1)
        (=(required-parttype-qty-on-agv blue_battery agv1)1)
    )

    (:goal(and
            ;dynamic predicate (from user inputs)
            (agv-is-at-as agv1 as1)
            ;static predicates
            (kit-complete)
            (robot-is-at-home ground_robot)
            (robot-is-at-home gantry_robot)
        )
    )

)
