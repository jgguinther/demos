from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from demos.Agent_Based_Modeling.prey_predator_abm.model.state_variables import genesis_states
from demos.Agent_Based_Modeling.prey_predator_abm.model.partial_state_update_block import partial_state_update_block
from demos.Agent_Based_Modeling.prey_predator_abm.model.sys_params import sys_params

sim_config = config_sim (
    {
        'N': 3, # number of monte carlo runs
        # 'T': range(300), # number of timesteps
        'T': range(10), # number of timesteps
        'M': sys_params, # simulation parameters
    }
)

exp = Experiment()
exp.append_model(
    model_id='sys_model',
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)
