# Dependences
from .parts.utils import *
from .sys_params import initial_values
from cadCAD.configuration.utils import rename_utils

utils = {
    'calculate_increment': calculate_increment,
    'get_free_location': get_free_location,
    'nearby_agents': nearby_agents,
    'check_location': check_location,
    'is_neighbor': is_neighbor
}

## Initial state object
genesis_states = {
    'agents': generate_agents(initial_values['world_size_n_dimension'],initial_values['world_size_m_dimension'], 
                              initial_values['initial_food_sites'],initial_values['initial_predator_count'], 
                              initial_values['initial_prey_count']),
    'sites': np.ones((initial_values['world_size_n_dimension'], initial_values['world_size_m_dimension'])) * initial_values['initial_food_sites'],
    'utils': rename_utils(utils)
}


