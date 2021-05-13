# Dependences
from demos.Agent_Based_Modeling.prey_predator_abm.model.parts.utils import *
from demos.Agent_Based_Modeling.prey_predator_abm.model.sys_params import initial_values


## Initial state object
genesis_states = {
    'agents': generate_agents(initial_values['world_size_n_dimension'],initial_values['world_size_m_dimension'], 
                              initial_values['initial_food_sites'],initial_values['initial_predator_count'], 
                              initial_values['initial_prey_count']),
    'sites': np.ones((initial_values['world_size_n_dimension'], initial_values['world_size_m_dimension'])) * initial_values['initial_food_sites']
}


