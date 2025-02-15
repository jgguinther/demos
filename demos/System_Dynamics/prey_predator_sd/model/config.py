from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from .state_variables import genesis_states
from .partial_state_update_block import partial_state_update_block
from .sys_params import sys_params 

sim_config = config_sim (
    {
        'N': 1, # number of monte carlo runs
        'T': range(1000), # number of timesteps
        'M': sys_params, # simulation parameters
    }
)

exp = Experiment()

exp.append_configs(
    model_id='sys_model2',
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)
