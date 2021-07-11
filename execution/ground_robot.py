# from industrial_robot import Industrial
# import industrial_robot
import industrial_robot

class Ground(industrial_robot.Industrial):

    def __init__(self, name: str, payload: float, application: list, linear_rail_length: float, company = 'NIST'):
        """Initialize class attributes. 

        Args:
            name (str): Name of the robot. This attribute canonly be accessed outside the class definition and cannot be set.
            payload (float): Payload for the robot’s arm(s). This attribute can be both accessed and set outside the class definition.
            application (list): List of applications the robot can perform. For instance,gantry_robot can do both kitting and assembly while ground_robot can only do kitting. This attribute can be both accessed and set outside the class definition.
            linear_rail_length (float): Length of linear rail. 
            company (str, optional): Name of the robot’s vendor. By default this is set to "Nist". This attribute canonly be accessed outsidethe class definition and cannot be set. Defaults to 'NIST'.
        """

        super().__init__(name, payload, application, company=company)
        self._linear_rail_length = linear_rail_length

    def __str__(self):
        return f'Name: {self._name}, Payload: {self._payload}, Application: {self._application}, Linear Rail Length: {self._linear_rail_length}, Company: {self._company}'

    @property
    def linear_rail_length(self):
        return self._linear_rail_length

    @linear_rail_length.setter
    def linear_rail_length(self, linear_rail_length):
        self._linear_rail_length = linear_rail_length

    def discard_part(self, parttype: str):
        """Print the robot name and the part being discarded

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
        """

        print(f'{self._name} discards {parttype}')

if __name__ == '__main__':

    gnd = Ground('Shon', 2.0, ['s', 'a'], 1.0, 'NIST')
    print(gnd)