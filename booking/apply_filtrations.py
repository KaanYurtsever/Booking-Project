from .bookings import Booking
from selenium.webdriver.common.by import By


class ApplyFiltration(Booking):
    PAGE_TITLE = (By.XPATH, '//*[@id="right"]/div[1]/div/div/div/h1')

    def star_rating(self, star):
        try:
            star_value = self.driver.find_element_by_xpath(
                f'//*[@id="left_col_wrapper"]/div[2]/div/div/div[1]/div[6]/div[{star + 1}]')
            star_value.click()
        except:
            star_value = self.driver.find_element_by_xpath(
                f'//*[@id="searchboxInc"]/div[1]/div/div/div[1]/div[6]/div[{star + 1}]')
            star_value.click()

    def sort_price_lowest_to_highest(self):
        ele = self.driver.find_element_by_css_selector('li[data-id="price"]')
        ele.click()

    def page_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text

    def close_browser(self):
        self.driver.close()
        self.driver.quit()
