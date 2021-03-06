#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for data API"""

import tempfile
import unittest
from urllib.error import URLError
import warnings

from sknetwork.data.toy_graphs import *
from sknetwork.data.load import *
from sknetwork.utils import Bunch


class TestDataAPI(unittest.TestCase):

    def test_toy_graphs(self):
        toy_graphs = [karate_club, painters, bow_tie, house, miserables]
        for toy_graph in toy_graphs:
            self.assertEqual(type(toy_graph()), sparse.csr_matrix)
            self.assertEqual(type(toy_graph(metadata=True)), Bunch)

    def test_load(self):
        tmp_data_dir = tempfile.gettempdir() + '/stub'
        clear_data_home(tmp_data_dir)
        try:
            graph = load_netset('stub', tmp_data_dir)
            self.assertEqual(type(graph), Bunch)
        except URLError:
            warnings.warn('Could not reach Telecom Graphs. Corresponding test has not been performed.', RuntimeWarning)
            return
