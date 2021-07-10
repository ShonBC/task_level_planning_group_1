from industrial_robot import Industrial_Robot


class Gantry(Industrial_Robot):
    def __init__(self, name: str, payload: float, appl: list(), company: str, 
                 small_rail_length: float, long_rail_length: float, 
                 small_rail_velocity: float, long_rail_velocity: float):
        super().__init__(name, payload, appl, company)
        self.small_rail_length = small_rail_length
        self.long_rail_length = long_rail_length
        self.small_rail_velocity = small_rail_velocity
        self.long_rail_velocity = long_rail_velocity

    def flip_part(self, parttype: str):
        print(f"flip part {parttype}")

    def place_part_on_tray(self, parttype: str):
        print(f"place {parttype} on tray")

    def activate_camera(self):
        return True

    def pick_up(self, name: str, parttype: str, bin: str):
        print(f"{name} picks up {parttype} from {bin}")
        self.activate_camera()
        super().pick_up(parttype, bin)
        self.flip_part(parttype)


if __name__ == '__main__':
    gantry_robot_obj = Gantry("robot1", 0.0, [], "NIST",  0.0, 0.0, 0.0, 0.0)
    print(gantry_robot_obj._name)
    print(gantry_robot_obj.appl)
    print(gantry_robot_obj.company)
    print(gantry_robot_obj.payload)
    print(gantry_robot_obj.long_rail_length)
    print(gantry_robot_obj.small_rail_velocity)
    print(gantry_robot_obj.small_rail_velocity)
    print(gantry_robot_obj.small_rail_length)
    gantry_robot_obj.place_part_on_tray("red_battery")


