from .parts.seir_model import *
from cadCAD.configuration.utils import rename_utils



utils = {
    "p_exposed_growth": p_exposed_growth,
    "p_infected_growth": p_infected_growth,
    "p_recovered_growth": p_recovered_growth,
    "s_susceptible_population": s_susceptible_population,
    "s_exposed_population": s_exposed_population,
    "s_infected_population": s_infected_population,
    "s_recovered_population": s_recovered_population
}

genesis_states = {
    'susceptible': 990,
    'exposed': 10,
    'infected': 0,
    'recovered': 0,
    'utils': rename_utils(utils)
}
