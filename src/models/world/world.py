

import math

import game_config
from models.data.world_stat import WorldState


class World:
    def __init__(self):
        self.state = WorldState(
            tick=0,
            nodes={},
            vehicles={},
            orders={},
            current_size_index=0
        )

    def generate_world(self, size_index: int):
        self.state.current_size_index = size_index

    def add_nodes(self):
        level = self.company.get_level()
        node_count = int(math.sqrt(self.get_world_size()) * game_config.NODE_DENSITY_FACTOR)
        ## calculate the number of node with some method
        factory_count = int(node_count * game_config.FACTORY_RATIO)
        store_count = int(node_count * game_config.STORE_RATIO)
        resource_count = int(node_count * game_config.RESOURCE_RATIO)

        ## randomly put nodes on the map

    def add_roads(self):
        pass

    def ticking(self):
        pass

    def get_nodes(self):
        return self.state.nodes
    
    def get_vehicles(self):
        return self.state.vehicles
    
    def get_orders(self):
        return self.state.orders
    
    def get_world_size(self):
        return game_config.WORLD_SIZES[self.company.get_level()/3]
    
    def get_nodes_by_id(self, node_id: int):
        return self.state.nodes.get(node_id)
    
    def get_vehicles_by_id(self, vehicle_id: int):
        return self.state.vehicles.get(vehicle_id)
    
    def get_orders_by_id(self, order_id: int):
        return self.state.orders.get(order_id)