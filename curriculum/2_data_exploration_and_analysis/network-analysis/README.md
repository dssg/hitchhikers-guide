# Networks

## Background and Motivation

Networks are a measurable representation of patterns of relationships connecting entities in an abstract or actual space.
The constituent parts of a network are nodes which are connected by ties. Networks have been used to model airplane 
traffic from airports, supply chains, friendship networks, and even amorphous materials like window glass, cells, and
proteins. The importance of networks analysis is that it captures the effect of where and how an individual actor 
is positioned among others.

In this tutorial, we are going to examine the friendship network of 34 students in a karate class. A political
rivalry arose in the class and divided the class into two factions, eventually leading to a fissure and two separate
karate classes. The club held periodic meetings to vote on policy decisions. When one of the faction heads, 
individuals 1 and 34, called a meeting, they would communicate the information only to members firmly in their 
faction, in order to ensure that the majority of members attending the meeting were in their faction, thereby
guaranteeing that their policies would pass. Meeting times were not publicly announced, but spread from friend to friend 
in the social network. In this tutorial we will explore graphical representations of this network, degree metrics, 
centrality metrics, how to calculate the shortest path between nodes, and community detection. We will be using the 
NetworkX Python Library developed at Los Alamos National Laboratory (LANL).

## Installation

To install the virtual environment and dependencies run the following command

```
./install_network_env.sh && source network-venv/bin/activate
```


