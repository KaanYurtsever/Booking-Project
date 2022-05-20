import booking.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Booking:
    def __init__(self, driver=webdriver.Chrome(service=Service(ChromeDriverManager().install())), teardown=True):
        self.driver = driver
        self.teardown = teardown
        super(Booking, self).__init__()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.close()
            self.driver.quit()

    def open_home_page(self):
        self.driver.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.driver.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place(self, location):
        place_to_go = self.driver.find_element_by_id('ss')
        place_to_go.clear()
        place_to_go.send_keys(location)

        place_to_go_first_option = self.driver.find_element_by_css_selector('li[data-i="0"]')
        place_to_go_first_option.click()

    def check_in_and_check_out_date(self, check_in, check_out):
        check_in_date = self.driver.find_element_by_css_selector(f'td[data-date="{check_in}"]')
        check_in_date.click()
        check_out_date = self.driver.find_element_by_css_selector(f'td[data-date="{check_out}"]')
        check_out_date.click()

    def select_guest_count(self, count):
        select_guest_field = self.driver.find_element_by_class_name('xp__guests__count')
        select_guest_field.click()

        while True:
            adults_count_element = self.driver.find_element_by_id('group_adults')
            adults_count = int(adults_count_element.get_attribute('value'))
            decrease_number_of_adults = self.driver.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]')
            decrease_number_of_adults.click()

            if adults_count == 1:
                break

        increase_number_of_adults = self.driver.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]')

        for i in range(count - 1):
            increase_number_of_adults.click()

    def search_hotels(self):
        search_button = self.driver.find_element_by_css_selector('button[type="submit"]')
        search_button.click()
