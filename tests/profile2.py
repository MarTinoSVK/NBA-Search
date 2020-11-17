#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import preprocess

# Test case for data preprocess
class TestPreprocess(unittest.TestCase):
	
    def test_generate_queries(self): 
        for i in range(100):
            ranked_queries, stat_queries, info_queries = preprocess.generate_queries(1500)
        pass
		
if __name__ == '__main__':
    unittest.main()