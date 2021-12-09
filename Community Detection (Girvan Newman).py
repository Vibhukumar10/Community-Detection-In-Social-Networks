#!/usr/bin/env python
# coding: utf-8

# # Girvan Newman Algorithm

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
from time import perf_counter

get_ipython().run_line_magic('matplotlib', 'inline')


# ## Function Definition

# In[2]:


def edge_to_remove(graph):
  G_dict = nx.edge_betweenness_centrality(graph)
  edge = ()

  # extract the edge with highest edge betweenness centrality score
  for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break

  return edge


# In[3]:


def girvan_newman(graph):
    # find number of connected components
    sg = nx.connected_components(graph)
    sg_count = nx.number_connected_components(graph)

    while(sg_count == 1):
        graph.remove_edge(edge_to_remove(graph)[0], edge_to_remove(graph)[1])
        sg = nx.connected_components(graph)
        sg_count = nx.number_connected_components(graph)

    return sg


# ## Visualising the input Graph

# In[4]:


G1 = nx.barbell_graph(5, 0)
nx.draw_networkx(G1)


# ## Ouput

# In[5]:


start = perf_counter()
c1 = girvan_newman(G1.copy())
end = perf_counter()
execution_time = (end - start)
execution_time


# In[6]:


# find the nodes forming the communities
node_groups1 = []

for i in c1:
  node_groups1.append(list(i))


# In[7]:


node_groups1


# ## Visualising the ouput

# In[8]:


color_map1 = []
for node in G1:
    if node in node_groups1[0]:
        color_map1.append('blue')
    else: 
        color_map1.append('green')  

nx.draw(G1, node_color=color_map1, with_labels=True)
plt.show()


# ## Visualising Zachary's Karate Club Graph

# In[9]:


# load the graph
G = nx.karate_club_graph()

# visualize the graph
nx.draw(G, with_labels = True)


# In[10]:


len(G.nodes), len(G.edges)


# In[11]:


start = perf_counter()
c = girvan_newman(G.copy())
end = perf_counter()
execution_time = (end - start)
execution_time


# In[12]:


# find the nodes forming the communities
node_groups = []

for i in c:
  node_groups.append(list(i))


# ## Ouput

# In[13]:


node_groups


# ## Visualising the ouput

# In[14]:


color_map = []
for node in G:
    if node in node_groups[0]:
        color_map.append('blue')
    else: 
        color_map.append('green')  

nx.draw(G, node_color=color_map, with_labels=True)
plt.show()


# In[ ]:




