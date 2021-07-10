

class Industrial_Robot():
    """Industrial Robot base class.
    Initialize with the robot name, payload, application, and company.
    """

    def __init__(self, name: str, payload: float, appl: list(), company="NIST"):
        """Initialize class attributes. 

        Args:
            name (str): Name of the robot. This attribute canonly be accessed outside the class definition and cannot be set.
            payload (float): Payload for the robot’s arm(s). This attribute can be both accessed and set outside the class definition.
            appl (list): List of applications the robot can perform. For instance,gantry_robot can do both kitting and assembly while ground_robot can only do kitting. This attribute can be both accessed and set outside the class definition.
            company (str, optional): Name of the robot’s vendor. By default this is set to "Nist". This attribute canonly be accessed outsidethe class definition and cannot be set.  Defaults to 'NIST'.
        """
        
        self.appl = appl
        self.payload = payload
        self._name = name
        self.company = company

    @property
    def name(self):
        return self._name


    def pick_up(parttype: str, bin: str):
        print(f"industrial robot picks up {parttype} from {bin}")


    def put_down(parttype: str, agv: str):
        print(f"industrial robot puts down {parttype} in {agv}")


    def attach_gripper(gripper: str):
        print(f"industrial robot attaching {gripper}")


    def detach_gripper(gripper: str):
        print(f"industrial robot detaching {gripper}")


    def move_to_bin(bin: str):
        print(f"moving to {bin}")

    def move_to_agv(agv: str):
        print(f"moving to {agv}")


    def move_to_gripper_station(station: str):
        print(f"moving to gripper station {station}")


    def move_from_bin(bin: str):
        print(f"moving from {bin}")


    def move_from_agv(agv: str):
        print(f"moving from {agv}")


    def move_from_gripper_station(station: str):
        print(f"moving from gripper station {station}")


if __name__ == '__main__':
    indus_robot_obj = industrial_Robot("robot1", 1.0, [])
    print(indus_robot_obj._name)
    print(indus_robot_obj.appl)
    print(indus_robot_obj.company)
    print(indus_robot_obj.payload)
    indus_robot_obj.move_from_agv("agv1")



