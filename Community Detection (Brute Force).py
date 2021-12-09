#!/usr/bin/env python
# coding: utf-8

# # Brute Force Method

# In[1]:


import networkx as nx
import itertools
from time import perf_counter


# ## Function Definition

# In[2]:


def communities_using_brute(G):
  nodes = G.nodes()
  n = G.number_of_nodes()
  first_community = []
    
  for i in range(1, n//2 + 1):
    c = [list(a) for a in itertools.combinations(nodes, i)]
    first_community.extend(c)
  
  second_community = []
  
  for i in range(len(first_community)):
    b = list(set(nodes)-set(first_community[i]))
    second_community.append(b)
  
  # Which division is best...
  intra_edges1 = []
  intra_edges2 = []
  inter_edges = []
      
  # ratio of number of intra/number of inter
  # community edges
  ratio = []  
  
  for i in range(len(first_community)):
    intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())
  
  for i in range(len(second_community)):
    intra_edges2.append(G.subgraph(second_community[i]).number_of_edges())
  
  e = G.number_of_edges()
  
  for i in range(len(first_community)):
    inter_edges.append(e-intra_edges1[i]-intra_edges2[i])
  
  # Calculate the Ratio
  
  for i in range(len(first_community)):
    ratio.append((float(intra_edges1[i]+intra_edges2[i]))/inter_edges[i])
  
  maxV=max(ratio)
  mindex=ratio.index(maxV)
  
  print('[', first_community[mindex], '] , [', second_community[mindex], ']')


# ## Visualising the input Graph

# In[3]:


G = nx.barbell_graph(5, 0)
nx.draw_networkx(G)


# ## Output 

# In[4]:


start = perf_counter()
communities_using_brute(G)
end = perf_counter()
execution_time = (end - start)
execution_time


# ## Visualising Zachary's Karate Club Graph

# In[5]:


G1 = nx.karate_club_graph()
nx.draw_networkx(G1)


# In[ ]:


start = perf_counter()
communities_using_brute(G1)
end = perf_counter()
execution_time = (end - start)
execution_time


# In[ ]:




