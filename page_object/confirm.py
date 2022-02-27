from selenium.webdriver.common.by import By

from utilities.parent_class import ParentClass


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    def input_in_country(self, country):
        return self.driver.find_element(
            By.ID, 'country'
        ).send_keys(country)

    def click_link(self, country):
        return self.driver.find_element(
            By.LINK_TEXT, country
        ).click()

    def tick_checkbox(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "label[for='checkbox2']"
        ).click()

    def click_purchase(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "[type='submit']"
        ).click()

    def test_alert_text(self):
        alert_text = self.driver.find_element(
            By.CSS_SELECTOR,
            "[class*='alert-success']"
        ).text

        log = ParentClass.logger()
        log.info('Text received from alert is ' + alert_text)

        assert 'Success' in alert_text
