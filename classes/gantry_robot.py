from classes import industrial_robot

class Gantry(industrial_robot.Industrial):
    """Initialize class attributes. 

    Args:
        indusrial_robot (class): Base class used to initialize some of the gantry robot parameters and methods.
    """
    
    def __init__(self, name: str, payload: float, application: list, small_rail_length: float, long_rail_length: float, small_rail_velocity: float, long_rail_velocity: float, company= 'NIST'):            
        """Initialize Gantry class parameters. 

        Args:
            name (str): Name of the robot. This attribute can only be accessed outside the class definition and cannot be set.
            payload (float): Payload for the robot’s arm(s). This attribute can be both accessed and set outside the class definition.
            application (list): List of applications the robot can perform. For instance, gantry_robot can do both kitting and assembly while ground_robot can only do kitting. This attribute can be both accessed and set outside the class definition.
            company (str, optional): Name of the robot’s vendor. By default this is set to "Nist". This attribute canonly be accessed outside the class definition and cannot be set. Defaults to 'NIST'.
            small_rail_length (float): Length of small rail.
            long_rail_length (float): Length of long rail.
            small_rail_velocity (float): Velocity of small rail.
            long_rail_velocity (float): Velocity of long rail.
        """

        super().__init__(name, payload, application, company=company)
        self._small_rail_length = small_rail_length
        self._long_rail_length = long_rail_length
        self._small_rail_velocity = small_rail_velocity
        self._long_rail_velocity = long_rail_velocity

    def __str__(self):
        
        return f'Name: {self._name}, Payload: {self._payload}, Application: {self._application}, Small Rail Length: {self._small_rail_length}, Ling Rail Length: {self._long_rail_length}, Small Rail Velocity: {self._small_rail_velocity}, Long Rail Velocity: {self._long_rail_velocity}, Company: {self._company}'

    @property
    def small_rail_length(self):
        return self._small_rail_length

    @property
    def long_rail_length(self):
        return self._long_rail_length

    @property
    def small_rail_velocity(self):
        return self._small_rail_velocity

    @property
    def long_rail_velocity(self):
        return self._long_rail_velocity

    @small_rail_length.setter
    def small_rail_length(self, small_rail_length):
        self._small_rail_length = small_rail_length

    @long_rail_length.setter
    def long_rail_length(self, long_rail_length):
        self._long_rail_length = long_rail_length

    @small_rail_velocity.setter
    def small_rail_velocity(self, small_rail_velocity):
        self._small_rail_velocity = small_rail_velocity

    @long_rail_velocity.setter
    def long_rail_velocity(self, long_rail_velocity):
        self._long_rail_velocity = long_rail_velocity

    def activate_camera(self):
        """Print the gantry robot activates the camera.
        """
        
        print(f'{self._name} activates camera')

    def flip_part(self, parttype: str):
        """Print the gantry robot flips the provided part.

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
        """
        
        print(f'{self._name} flips {parttype}')
    
    def pick_up(self, parttype: str, bin: str):
        """Gantry robot picks up part then activates its camera, calls the base class pick_up method, then flips the part. 

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self._name}  picks up {parttype} from bin {bin}')
        self.activate_camera()
        super().pick_up(parttype, bin)
        self.flip_part(parttype)

if __name__ == '__main__':
    # robot = indusrial_robot('Shon', 1.2, ['s', 'd'])
    # robot.pick_up('red battery', 'bin 1')
    # robot.put_down('red battery', 'bin 1')
    # robot.attach_gripper('three_finger')
    # robot.detach_gripper('three_finger')
    # robot.move_to_bin('bin 1')
    # robot.move_to_agv('agv 1')
    # robot.move_from_bin('bin 1')
    # robot.move_from_agv('agv 1')
    # robot.move_to_gripper_station('gripper changing station')
    # robot.move_from_gripper_station('gripper changing station')

    g_robot = Gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')
    print(g_robot)
    g_robot.pick_up('red battery', 'bin 2')
