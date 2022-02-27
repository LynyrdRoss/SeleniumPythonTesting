from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import pytest
import logging
import inspect


@pytest.mark.usefixtures('setup')
class ParentClass:
    @staticmethod
    def logger():
        log_name = inspect.stack()[1][3]
        log = logging.getLogger(log_name)

        file_handler = logging.FileHandler('log.log')
        log_format = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')

        file_handler.setFormatter(log_format)

        log.addHandler(file_handler)
        log.setLevel(logging.DEBUG)

        return log

    def verify_link_presence(self, by_selector, string_value):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((
                by_selector, string_value
            ))
        )
