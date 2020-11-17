#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import preprocess

# Test case for data preprocess
class TestPreprocess(unittest.TestCase):

    def test_generate_rank_queries(self): 
        for i in range(100):
            rank_queries = preprocess.generate_rank_queries(1500)
            stat_queries = preprocess.generate_stat_queries(1500)
            info_queries = preprocess.generate_info_queries(1500)
        pass
	
if __name__ == '__main__':
    unittest.main()