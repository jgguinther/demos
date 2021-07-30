MONTE_CARLO_RUNS = 1 # N monte carlo runs

from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from demos.System_Dynamics.Compartment_Models.seird.model.state_variables import genesis_states
from demos.System_Dynamics.Compartment_Models.seird.model.partial_state_update_block import partial_state_update_block
from demos.System_Dynamics.Compartment_Models.seird.model.sys_params import sys_params
from demos.System_Dynamics.Compartment_Models.seird.sim_params import SIMULATION_TIME_STEPS


sim_config = config_sim (
    {
        'N': MONTE_CARLO_RUNS,
        'T': range(SIMULATION_TIME_STEPS), # number of timesteps
        'M': sys_params,
    }
)

exp = Experiment()

exp.append_model(
    model_id="sys_model_1",
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)

exp.append_model(
    model_id="sys_model_2",
    sim_configs=sim_config,
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_block
)
