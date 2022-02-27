from selenium.webdriver.common.by import By

from utilities.parent_class import ParentClass
from page_object.home import HomePage

import time


class TestMain(ParentClass):
    def test_main_function(self):
        log = ParentClass.logger()

        home_page = HomePage(self.driver)

        checkout = home_page.click_shop()

        log.info('Fetching card titles')

        cards = checkout.get_product_title()

        for card in cards:
            card_title = card.text

            log.info(card_title)

            if card_title == 'Blackberry':
                checkout.click_blackberry_button()

        checkout.click_checkout_btn()

        confirm = checkout.proceed_to_checkout()

        log.info("Inputting country name with ind")

        confirm.input_in_country('ind')
        time.sleep(5)

        self.verify_link_presence(By.LINK_TEXT, 'India')

        confirm.click_link('India')

        confirm.tick_checkbox()

        confirm.click_purchase()

        confirm.test_alert_text()
