'''
Industrial Robot base class.
'''

class Industrial():
    """Industrial Robot base class.
    Initialize with the robot name, payload, application, and company.
    """
   
    def __init__(self, name: str, payload: float, application: list, company = 'NIST'):
        """Initialize class attributes. 

        Args:
            name (str): Name of the robot. This attribute can only be accessed outside the class definition and cannot be set.
            payload (float): Payload for the robot’s arm(s). This attribute can be both accessed and set outside the class definition.
            application (list): List of applications the robot can perform. For instance, gantry_robot can do both kitting and assembly while ground_robot can only do kitting. This attribute can be both accessed and set outside the class definition.
            company (str, optional): Name of the robot’s vendor. By default this is set to "Nist". This attribute can only be accessed outside the class definition and cannot be set.  Defaults to 'NIST'.
        """
       
        self._name = name
        self._payload = payload
        self._application = application
        self._company = company

    def __str__(self):
        return f'Name: {self._name}, Payload: {self._payload}, Application: {self._application}, Company: {self._company}'

    @property
    def name(self):
        return self._name
    
    @property
    def payload(self):
        return self._payload

    @property
    def application(self):
        return self._application

    @property 
    def company(self):
        return self._company

    @payload.setter
    def payload(self, payload):
        self._payload = payload
    
    @application.setter
    def application(self, application):
        self.application = application
        
    def pick_up(self, parttype: str, bin: str):
        """Print the part type picked up and the bin it was obtained from.

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self.name} picks up {parttype} from bin {bin}')

    def put_down(self, parttype: str, bin: str):
        """Print the part type put down and the bin it was taken from.

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self.name} puts down {parttype} from bin {bin}')

    def attach_gripper(self, gripper: str):
        """Print the gripper the robot has attached.

        Args:
            gripper (str): Robots can use 2 grippers: A vacuum gripper (vacuum_gripper) and a 3-finger gripper (finger_gripper).
        """

        print(f'{self.name} attaches {gripper}')

    def detach_gripper(self, gripper: str):
        """Print the gripper the robot has detached.

        Args:
            gripper (str): Robots can use 2 grippers: A vacuum gripper (vacuum_gripper) and a 3-finger gripper (finger_gripper).
        """

        print(f'{self.name} detaches {gripper}')

    def move_to_bin(self, bin:str): 
        """Print the bin the robot has moved to.

        Args:
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self.name} moves to bin {bin}')

    def move_to_agv(self, agv: str): 
        """Print the AGV the robot has moved to.

        Args:
            agv (str): Automated Guided Vehicle used to transport parts to kitting station.
        """

        print(f'{self.name} moves to {agv}')

    def move_to_gripper_station(self, station: str): 
        """Print the robot has moved to the gripper station.

        Args:
            station (str): Gripper changing station. The robot must move here to change grippers.
        """

        print(f'{self.name} moves to {station}')

    def move_from_bin(self, bin: str): 
        """Print the bin the robot is moving from.

        Args:
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self.name} moves from bin {bin}')

    def move_from_agv(self, agv: str): 
        """Print the AGV the robot is moving from.

        Args:
            agv (str): Automated Guided Vehicle used to transport parts to kitting station.
        """

        print(f'{self.name} moves from {agv}')

    def move_from_gripper_station(self, station: str): 
        """Print the robot is moving from the gripper changing station.

        Args:
            station (str): Gripper changing station. The robot must move here to change grippers.
        """

        print(f'{self.name} moves from {station}')

if __name__ == '__main__':
    robot = Industrial('Shon', 1.2, ['s', 'd'])
    print(robot)
    robot.pick_up('red battery', 'bin 1')
    robot.put_down('red battery', 'bin 1')
    robot.attach_gripper('three_finger')
    robot.detach_gripper('three_finger')
    robot.move_to_bin('bin 1')
    robot.move_to_agv('agv 1')
    robot.move_from_bin('bin 1')
    robot.move_from_agv('agv 1')
    robot.move_to_gripper_station('gripper changing station')
    robot.move_from_gripper_station('gripper changing station')

    # g_robot = gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')
    # g_robot.pick_up('red battery', 'bin 2')
