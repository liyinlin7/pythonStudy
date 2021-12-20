import unittest
import logging
from time import sleep


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('====setUp()====')

    def tearDown(self):
        logging.info('======tearDown=====')
        sleep(5)
