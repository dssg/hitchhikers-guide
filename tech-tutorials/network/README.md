# Networks

## Background and Motivation

Networks are a measurable representation of patterns of relationships connecting entities in an abstract or actual space.
The constituent parts of a network are nodes which are connected by ties. Networks have been used to model airplane 
traffic from airports, supply chains, friendship networks, amorphous materials like window glass, cells, and proteins. 
The importance of networks analysis is that it captures the affect of where and how an individual actor is positioned 
among others.

In this tutorial we are going to examine the friendship network of 34 individuals in a karate class. This is an
interesting dataset due to a political rivalry that arose in the class and divided the class into two factions,
eventually leading to a fissure and two separate karate classes. The club would periodically hold meetings called by two
leaders, 1 and 34, the heads of each faction. When one of the heads of the faction called a meeting they would 
communicate the information to members only firmly in their faction in order to attain a majority during the meeting
time so their polices could be passed. The information of when a meeting occured was passed from friend-to-friend in
the social network. In this tutorial we will explore representations of this network, degree metrics, centrality metrics,
how to calculate the shortest path between nodes, and community detection. We will be using the NetworkX Python Library
developed at Los Alamos National Laboratory (LANL) for the majority of this work.

## Installation

To install the virtual environment and dependencies run the following command
```
./install
```
./install_network_env.sh && source network-venv/bin/activate
```


