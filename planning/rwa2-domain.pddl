(define (domain rwa2-domain)
	(:requirements :strips :typing :fluents)
	(:types 
		Robot
		AGV
		Part
		Gripper
		Bin
		AssemblyStation
		PartType
		GripperStation
	)
	
	(:predicates
		(robot-is-at-bin ?robot - Robot ?bin - Bin);robot location is at bin
		(robot-is-at-home ?robot - Robot);robot is at home
		(robot-is-not-at-home ?robot - Robot);robot is not at home
		(robot-is-at-agv ?robot - Robot ?agv - AGV)
		(robot-is-at-gripper-station ?robot - Robot ?gripper_station - GripperStation)
		(robot-has-gripper ?robot - Robot ?gripper - Gripper)	
		(robot-can-reach-bin ?robot - Robot ?bin - Bin)
		(robot-is-not-at-bin ?robot - Robot)
 	    (robot-is-not-at-agv ?robot - Robot)
		(robot-is-not-at-gripper-station ?robot - Robot)

(agv-is-at-as ?agv - AGV ?station - AssemblyStation)
		(agv-is-at-ks ?agv - AGV)
		(agv-is-not-at-ks ?agv - AGV)
		(agv-can-go-to-as ?agv - AGV ?as - AssemblyStation)
		;Gripper
		(gripper-is-on-robot ?gripper - Gripper ?robot - Robot)
		(gripper-is-at-station ?gripper - Gripper ?station - GripperStation)
		(gripper-can-grasp-parttype ?gripper - Gripper ?parttype - PartType)
		(gripper-is-empty ?gripper - Gripper)
		(gripper-holds-parttype ?gripper - Gripper ?parttype - PartType)
		;Bin
		(bin-has-parttype ?bin - Bin ?parttype - PartType)
		(kit-complete)
		(robot-has-no-gripper ?robot - Robot)

	)

	(:functions
		(parttype-quantity-in-bin ?parttype - PartType ?bin - Bin)
		(current-parttype-qty-on-agv ?parttype - PartType ?agv - AGV)
		(required-parttype-qty-on-agv ?parttype - PartType ?agv - AGV)
		(kit-current-part-qty)
		(kit-final-part-qty)
	)

	(:action PICK_UP
		:parameters(
			?robot - Robot 
			?gripper - Gripper 
			?parttype - PartType
			?bin - Bin)
		:precondition(and
			(>(parttype-quantity-in-bin ?parttype ?bin)0)
			(robot-is-at-bin ?robot ?bin)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
			(gripper-can-grasp-parttype ?gripper ?parttype)
			(gripper-is-empty ?gripper)
			(bin-has-parttype ?bin ?parttype)

		)
		:effect(and
			(decrease(parttype-quantity-in-bin ?parttype ?bin)1)
			(not(gripper-is-empty ?gripper))
			(gripper-holds-parttype ?gripper ?parttype)
		)
	)

	



	(:action PUT_DOWN
		:parameters(
			?robot - Robot
			?parttype - PartType
			?gripper - Gripper
			?agv - AGV)
		:precondition(and
			(agv-is-at-ks ?agv)
			(robot-is-at-agv ?robot ?agv)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
			(gripper-holds-parttype ?gripper ?parttype)
			
			)
		:effect(and
			(increase(current-parttype-qty-on-agv ?parttype  ?agv)1)
			(not(gripper-holds-parttype ?gripper ?parttype))
			(gripper-is-empty ?gripper)
			(increase(kit-current-part-qty)1)
			)
	)
	(:action ATTACH_GRIPPER
		:parameters(
			?robot - Robot
			?gripper - Gripper
			?gripper_station - GripperStation)
		:precondition(and
			(robot-has-no-gripper ?robot)
			(gripper-is-empty ?gripper)	
			(robot-is-at-gripper-station ?robot ?gripper_station)
			(gripper-is-at-station ?gripper ?gripper_station)		
		)
		:effect(and
			(not(gripper-is-at-station ?gripper ?gripper_station))
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
			(not(robot-has-no-gripper ?robot))
		)
	)
	(:action DETACH_GRIPPER
		:parameters(
			?robot - Robot
			?gripper - Gripper
			?gripper_station - GripperStation)
		:precondition(and
			(robot-is-at-gripper-station ?robot ?gripper_station)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)	
			(gripper-is-empty ?gripper)
		)
		:effect(and
			(gripper-is-at-station ?gripper ?gripper_station)
			(not(robot-has-gripper ?robot ?gripper))
			(not(gripper-is-on-robot ?gripper ?robot))
			(robot-has-no-gripper ?robot)
		)
	)
	(:action MOVE_TO_BIN
		:parameters(
			?robot - Robot
			?bin - Bin)
		:precondition(and
			(robot-can-reach-bin ?robot ?bin)
			(robot-is-at-home ?robot)
			(robot-is-not-at-bin ?robot)
			
		)
		:effect(and
			(robot-is-not-at-gripper-station ?robot)
			(robot-is-not-at-agv ?robot)
			(robot-is-not-at-home ?robot)
			(not(robot-is-at-home ?robot))
			(robot-is-at-bin ?robot ?bin)
			(not(robot-is-not-at-bin ?robot))

		)
	)

	(:action MOVE_TO_AGV
		:parameters(
			?robot - Robot
			?agv - AGV
			?gripper - Gripper
			?parttype - PartType)
		:precondition(and
			(robot-is-at-home ?robot)	
			(agv-is-at-ks ?agv)
			(robot-is-not-at-agv ?robot)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
			(gripper-holds-parttype ?gripper ?parttype)
			(<(current-parttype-qty-on-agv ?parttype ?agv)(required-parttype-qty-on-agv ?parttype ?agv))
		)
		:effect(and
			(not(robot-is-at-home ?robot))
			(robot-is-at-agv ?robot ?agv)
			(robot-is-not-at-gripper-station ?robot)
			(robot-is-not-at-bin ?robot)
			(robot-is-not-at-home ?robot)	
			(not(robot-is-not-at-agv ?robot))
		)
	)

	(:action MOVE_TO_GRIPPER_STATION
		:parameters(
			?robot - Robot
			?gripper_station - GripperStation
		)
		:precondition(and
			(robot-is-at-home ?robot)
			(robot-is-not-at-gripper-station ?robot)
			(robot-is-not-at-bin ?robot)
 	    (robot-is-not-at-agv ?robot)	
		)
		:effect(and
			(robot-is-not-at-home ?robot)
			(robot-is-not-at-agv ?robot)
			(robot-is-not-at-bin ?robot)
			(robot-is-at-gripper-station ?robot ?gripper_station)
			(not(robot-is-at-home ?robot))
			(not(robot-is-not-at-gripper-station ?robot))
		)
	)


	(:action MOVE_FROM_BIN
		:parameters (?robot - Robot ?bin - bin ?gripper - Gripper ?parttype - PartType)
		:precondition (and 
			(robot-is-at-bin ?robot ?bin)
			(robot-is-not-at-home ?robot)
			(robot-is-not-at-gripper-station ?robot)
			(robot-is-not-at-agv ?robot)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
			(gripper-holds-parttype ?gripper ?parttype)
		)
		:effect (and 
			(not(robot-is-at-bin ?robot ?bin))
			(not(robot-is-not-at-home ?robot))
			(robot-is-at-home ?robot)
		)
	)

	(:action MOVE_FROM_AGV
		:parameters (?robot - Robot ?agv - AGV)
		:precondition (and 
			(robot-is-at-agv ?robot ?agv)
			(robot-is-not-at-home ?robot)
			(robot-is-not-at-gripper-station ?robot)
			(robot-is-not-at-bin ?robot)
		)
		:effect (and 
			(not(robot-is-at-agv ?robot ?agv))
			(not(robot-is-not-at-home ?robot))
			(robot-is-at-home ?robot)
		)
	)

	(:action MOVE_FROM_GRIPPER_STATION
		:parameters (?robot - Robot ?gripper - Gripper ?gripper_station - GripperStation)
		:precondition (and 
			(robot-is-at-gripper-station ?robot ?gripper_station)
			(robot-is-not-at-home ?robot)
			(robot-is-not-at-agv ?robot)
			(robot-is-not-at-bin ?robot)
			(robot-has-gripper ?robot ?gripper)
			(gripper-is-on-robot ?gripper ?robot)
		)
		:effect (and 
			(not(robot-is-at-gripper-station ?robot ?gripper_station))
			(not(robot-is-not-at-home ?robot))
			(robot-is-at-home ?robot)
		)
	)

	

		(:action SET_KIT_COMPLETE
			:parameters(

			)
			:precondition(and
				(=(kit-current-part-qty)(kit-final-part-qty))
			)
			:effect(and
				(kit-complete)
			)
		)
				
		(:action DRIVE_TO_KS
			:parameters(
				?agv - AGV
				?as - AssemblyStation
			)
			:precondition(and
				(agv-is-not-at-ks ?agv)
				(agv-is-at-as ?agv ?as)	
			)
			:effect(and
				(not(agv-is-not-at-ks ?agv))
				(not(agv-is-at-as ?agv ?as))
				(agv-is-at-ks ?agv)
			)
		)

		(:action DRIVE_TO_AS
			:parameters(
				?agv - AGV
				?as - AssemblyStation
			)
			:precondition(and
				(agv-can-go-to-as ?agv ?as)
				(agv-is-at-ks ?agv)
				(kit-complete)	
			)
			:effect(and
				(agv-is-at-as ?agv ?as)
				(not(agv-is-at-ks ?agv))
				(agv-is-not-at-ks ?agv)
			)
		)
)
