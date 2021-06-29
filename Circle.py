
import logging
from math import pi
import timeit
import sys
from os import path
sys.path.append(path.abspath('../test2'))
import unit_testing

class Circle:

    #method for find circle area
    def circle_area(self,r):
        txt = "{:.2f}"
        result=float(txt.format(pi*(r**2)))
        return result



    # method for find diameter
    def circle_diameter(self,r):
        txt = "{:.2f}"
        result = float(txt.format(2*r))
        return result


    # method for find circumference
    def circle_circumference(self,r):
        txt = "{:.2f}"
        result = float(txt.format(2*pi*r))
        return result



     #method the return boolean
    def true_false(self,r):
        if(r>0):
            return True
        else:
            return False
#

if __name__ == '__main__':


    # logging to show information and warning
    LOG_FILENAME = "logfile.log"
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
    logging.info('Info:Began to log')
    logging.warning('Warning:It is Unit testing program ')
    logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s', level=logging.DEBUG)

    print('Mandeep Kaur 800291')

    # start execution time
    start_time = timeit.default_timer()


    #calling run_test method
    unit_testing.UnitTest_Quiz().run_test()


    # execution time print in logfile and console
    print("start", start_time)
    logging.info('starting Time: {}'.format(start_time))
    executionTime=timeit.default_timer() - start_time
    print("Execution Time:", executionTime, "seconds")
    logging.info('Execution Time: {}'.format(executionTime))




