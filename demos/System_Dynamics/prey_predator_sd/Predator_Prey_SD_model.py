#!/usr/bin/env python
# coding: utf-8

# ## Predator Prey Systems Dynamics modelling
# 
# ### Dynamical System: Lotka-Volterra
# 
# This is the standard introductory model for Prey-Predator interactions and dynamical systems in general. It is based on the following equations:
# 
# \begin{aligned}{\frac {d}{dt}Prey}&=\alpha * Prey-\beta * Prey * Predators,\\{\frac {d}{dt}Predators}&=\delta * Prey * Predators-\gamma * Predators,\end{aligned}
# 
# Where $\alpha$ and $\gamma$  are the prey growth rate and predator elimination rate, and $\delta$ and $\gamma$ are interaction factors between preys and predators.
# 
# The most prominent feature of it is the existence, depending on the choice of parameters, of a repeteable cycle around a fixed point which creates a dynamical equilibrium between the number of preys and predators on a system.
# 
# In this simulation, we don't have any variability, we are running it with no monte carlo runs. We are running with 1,000 timesteps.

# In[1]:


# Dependences
import pandas as pd
import numpy as np

# Experiments
from model import run
pd.options.display.float_format = '{:.2f}'.format

# get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib inline

# run the simulation
df = run.run()


# In[ ]:


# observe the dataset


# In[2]:


df.head()


# In[ ]:


# plot the data


# In[3]:


df.plot(x='timestep',y=['prey_population','predator_population'],title='Predator Prey populations over time',
       figsize =(15,10))


# We can see that when prey increases, predators increase shortly after, and after prey decreases, prey decreases, illustrating the cyclical nature of the predator prey dynamical system. 
