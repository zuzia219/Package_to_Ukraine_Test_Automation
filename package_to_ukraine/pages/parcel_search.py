from package_to_ukraine.locators.locators import ParcelLocators
import logging


class SearchParcel:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def search_parcel_by_weight(self, weight):
        self.logger.info("Setting weight in Kg {}".format(weight))
        self.driver.find_element_by_name(ParcelLocators.parcel_weight_name).send_keys(weight)
        self.driver.find_element_by_xpath(ParcelLocators.parcel_search_xpath).click()



