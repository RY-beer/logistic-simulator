from models.data.world_stat import WorldState

class Simulation:
    def __init__(self):
        self.state = WorldState(
            nodes={},
            edges={},
            vehicles={},
            orders={}
        )

    def tick(self):
        self._move_vehicles()
        self._process_orders()
        self._apply_penalties()