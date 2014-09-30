#!/usr/local/bin/python2.7
'''
@Author: Jilesh Lakhani
@Date: 30th Sept 2014
'''

import os
import sys
import csv
import copy
from collections import OrderedDict

YEAR = 'Year'
MONTH = 'Month'
PRICE = 'Price'

class ComputeSharePrice(object):
    def __init__(self):
        self.max_company_share_price = OrderedDict()
        super(ComputeSharePrice, self).__init__()
    
    def __call__(self, absolute_file_name):       
        try:
            rows = csv.DictReader(open(absolute_file_name), dialect='excel')
            header = copy.deepcopy(rows.fieldnames)
            try:
                header.remove(YEAR)
            except Exception, e:
                raise Exception('Expecting Header with Colum Name "%s", Note Header is case senstive' % YEAR)

            try:
                header.remove(MONTH)
            except Exception, e:
                raise Exception('Expecting Header with Colum Name "%s", Note Header is case senstive' % MONTH)

            companies = header

            for row in rows:
                for company in companies:
                    if self.max_company_share_price.has_key(company):
                        if not row[company]:
                            continue
                        if int(self.max_company_share_price[company][0]) < int(row[company]):
                            self.max_company_share_price[company] = (row[company], row[MONTH], row[YEAR])
                    else:
                        self.max_company_share_price[company] = (row.get(company, 0), row[MONTH], row[YEAR])                        
            return self.max_company_share_price
        except IOError, e:
                raise Exception('Please Provide correct File name')

share_price = ComputeSharePrice()

if __name__ == '__main__':
    file_name = None
    if len(sys.argv) > 1:
        file_name = sys.argv[0]

    else:
        file_name = raw_input("File name: ")

    for key, value in share_price(file_name).iteritems():
        print 'Max Share Price of %s, is in Year %s & Month %s, with max price of %s' % (key, value[2], value[1], str(value[0]))

