from utilities.parent_class import ParentClass
from page_object.home import HomePage
from test_data.home_page_data import HomePageData

import pytest


class TestHomePage(ParentClass):
    @pytest.fixture(params=HomePageData.test_home_page_data_tuple)
    def home_data_tuple(self, request):
        """
        This uses tuple data as params
        """
        return request.param

    @pytest.fixture(params=HomePageData.get_data_excel('test5'))
    def home_data(self, request):
        """
        This uses dictionary as data
        """
        return request.param

    def test_home_form_submission(self, home_data):
        hp = HomePage(self.driver)

        hp.input_name(home_data['firstname'])
        hp.input_email(home_data['email'])
        hp.tick_ice_cream_box()
        hp.select_gender(home_data['gender'])
        hp.click_submit()

        self.driver.refresh()
