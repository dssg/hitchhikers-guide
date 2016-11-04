#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This package implements community detection."""

from .community_louvain import *

__all__ = ["partition_at_level", "modularity", "best_partition",
           "generate_dendrogram", "generate_dendogram", "induced_graph",
           "load_binary"]
__author__ = """Thomas Aynaud (thomas.aynaud@lip6.fr)"""
#    Copyright (C) 2009 by
#    Thomas Aynaud <thomas.aynaud@lip6.fr>
#    All rights reserved.
#    BSD license.
