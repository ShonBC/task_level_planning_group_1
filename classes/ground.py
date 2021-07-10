from industrial_robot import Industrial_Robot


class Ground(Industrial_Robot):
    def __init__(self,  name: str, payload: float, appl: list(), company: str, lin_rail_len: float):
        super().__init__(name, payload, appl, company)
        self.lin_rail_len = lin_rail_len

    def discard_part(self, parttype: str):
        print("Discarding {}".format(parttype))


if __name__ == '__main__':
    ground_robot_obj = Ground("robot1", 0.0, [], "NIST", 0.0)
    print(ground_robot_obj._name)
    print(ground_robot_obj.appl)
    print(ground_robot_obj.company)
    print(ground_robot_obj.payload)
    print(ground_robot_obj.lin_rail_len)
    ground_robot_obj.discard_part("red_battery")



