from .parts.agents import *
from .parts.environment import *
from app.demos.labs_utils import rename_psubs

partial_state_update_block = rename_psubs([
    {
        # environment.py
        'policies': {
            'grow_food': grow_food
        },
        'states': {
            'sites': update_food
        }
    },
    {
        # agents.py
        'policies': {
            'increase_agent_age': digest_and_olden
        },
        'states': {
            'agents': agent_food_age

        }
    },
    {
        # agents.py
        'policies': {
            'move_agent': move_agents
        },
        'states': {
            'agents': agent_location

        }
    },
    {
        # agents.py
        'policies': {
            'reproduce_agents': reproduce_agents

        },
        'states': {
            'agents': agent_create

        }
    },
    {
        # agents.py
        'policies': {
            'feed_prey': feed_prey
        },
        'states': {
            'agents': agent_food,
            'sites': site_food
        }
    },
    {
        # agents.py
        'policies': {
            'hunt_prey': hunt_prey
        },
        'states': {
            'agents': agent_food
        }
    },
    {
        # agents.py
        'policies': {
            'natural_death': natural_death
        },
        'states': {
            'agents': agent_remove
        }
    }
])
