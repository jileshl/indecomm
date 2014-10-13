#!/usr/local/bin/python2.7
'''
@Author: Jilesh Lakhani
@Date: 30th Sept 2014
'''

import unittest

from collections import OrderedDict
from compute_share_price import ComputeSharePrice

class TestComputeSharePrice(unittest.TestCase):
    def setUp(self):
        self.test_klass = ComputeSharePrice()
        
    def test_invalid_year(self):
        #import pdb; pdb.set_trace()
        with self.assertRaises(Exception) as ex:
            self.test_klass('tests/sample_data/invalid_header_year.csv')

        exception = ex.exception
        self.assertEqual(exception.message, 'Expecting Header with Colum Name "Year", Note Header is case senstive')

    def test_invalid_month(self):
        with self.assertRaises(Exception) as ex:
            self.test_klass('tests/sample_data/invalid_header_month.csv')

        exception = ex.exception
        self.assertEqual(exception.message,'Expecting Header with Colum Name "Month", Note Header is case senstive')

    def test_invalid_path(self):
        with self.assertRaises(Exception) as ex:
            self.test_klass('invalid/path/test.csv')

        exception = ex.exception
        self.assertEqual(exception.message, 'Please Provide correct File name')
            
    def test_valid_multiple_company(self):
        expected_result = OrderedDict([('Company-A', ('751', 'Jan', '1990')), ('Company-B', ('880', 'Dec', '2013')), ('Company-C', ('856', 'Dec', '2013')), ('Company-D', ('865', 'Dec', '2013'))])
        return_val = self.test_klass('tests/sample_data/shares_data_valid.csv')
        self.assertEqual(expected_result, return_val)      
        self.assertEqual(len(expected_result.keys()), 4)

    def test_valid_multiple_company_2(self):
        expected_result = OrderedDict([('Company-A', ('751', 'Jan', '1990')), ('Company-B', ('880', 'Dec', '2013')), ('Company-C', ('856', 'Dec', '2013')), ('Company-D', ('865', 'Dec', '2013')), ('CompanyE', ('561', 'Dec', '2013'))])
        return_val = self.test_klass('tests/sample_data/shares_data_valid_2.csv')
        self.assertEqual(expected_result, return_val)      
        self.assertEqual(len(expected_result.keys()), 5)

    def test_valid_multiple_company_3(self):
        expected_result = OrderedDict([('Company-A', ('751', 'Jan', '1990')), ('Company-B', ('880', 'Dec', '2013')), ('Company-C', ('856', 'Dec', '2013')), ('Company-D', ('865', 'Dec', '2013')), ('Company-E', ('561', 'Dec', '2013'))])
        return_val = self.test_klass('tests/sample_data/shares_data_valid_3.csv')
        self.assertEqual(expected_result, return_val)
        
if __name__ == '__main__':
    unittest.main()
