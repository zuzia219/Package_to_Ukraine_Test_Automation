from selenium.webdriver.common.keys import Keys

from package_to_ukraine.locators.locators import InvalidMessageLocators, DeliveryMethodsLocators, DeliveryPointsLocators, ParcelLocators, SenderLocators, CustomsDeclarationLocators
import logging


class ParcelDelivery:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def fetch_available_deliveries(self):
        delivery_element_list = self.driver.find_elements_by_xpath(DeliveryMethodsLocators.delivery_methods_xpath)
        delivery_method_list = []
        for delivery in delivery_element_list:
            delivery_method_list.append(delivery.text)
        delivery_method_list = [text.split("\n")[0] for text in delivery_method_list]
        return delivery_method_list

    def check_if_delivery_available(self, delivery_method):
        self.logger.info("Choosing parcel delivery {}".format(delivery_method))
        delivery_method_list = self.fetch_available_deliveries()
        self.logger.info("Available deliveries {}".format(delivery_method_list))
        delivery_available = False
        if any(delivery_method in s for s in delivery_method_list):
            delivery_available = True
        self.logger.info("Chosen delivery method is available: {}".format(delivery_available))
        return delivery_available

    def choose_delivery_method(self, delivery_method):
        delivery_methods = self.fetch_available_deliveries()
        delivery_method_index = delivery_methods.index(delivery_method)
        self.logger.info("Index {}".format(delivery_method_index))
        parcel_send_button_index = delivery_method_index + 1
        send_button_xpath = "(" + ParcelLocators.parcel_send_locators + ")" + "[" + str(parcel_send_button_index) + "]"
        self.driver.find_element_by_xpath(send_button_xpath).click()

    def choose_first_available_delivery_point(self):
        self.driver.find_element_by_xpath(DeliveryPointsLocators.delivery_point_checkbox_xpath).click()
        #self.driver.find_element_by_xpath(DeliveryPointsLocators.delivery_point_search_xpath).click()
        #self.driver.find_element_by_xpath(DeliveryPointsLocators.delivery_point_search_xpath).send_keys(Keys.ENTER)

    def set_sender_info(self, Sender):
        self.driver.find_element_by_id(SenderLocators.sender_name_id).send_keys(Sender.sender_name)
        self.driver.find_element_by_id(SenderLocators.sender_city_id).send_keys(Sender.sender_city)
        self.driver.find_element_by_id(SenderLocators.sender_postal_code_id).send_keys(Sender.sender_postal_code)
        self.driver.find_element_by_id(SenderLocators.sender_house_number_id).send_keys(Sender.sender_house_number)
        self.driver.find_element_by_id(SenderLocators.sender_flat_number_id).send_keys(Sender.sender_flat_number)
        self.driver.find_element_by_id(SenderLocators.sender_phone_id).send_keys(Sender.sender_phone)
        self.driver.find_element_by_id(SenderLocators.sender_email_id).send_keys(Sender.sender_email)

    def set_custom_declaration_row(self, ParcelItem):
        index_to_add = ParcelItem.parcel_item_number
        index_to_add = "-" + str(index_to_add - 1)
        self.driver.find_element_by_name(CustomsDeclarationLocators.parcel_item_description_name + index_to_add).send_keys(ParcelItem.parcel_item_description)
        self.driver.find_element_by_name(CustomsDeclarationLocators.parcel_item_quantity_name + index_to_add).send_keys(
            ParcelItem.parcel_item_quantity)
        self.driver.find_element_by_name(CustomsDeclarationLocators.parcel_item_weight_name + index_to_add).send_keys(
            ParcelItem.parcel_item_weight)
        self.driver.find_element_by_name(CustomsDeclarationLocators.parcel_item_value_client_currency_name + index_to_add).send_keys(
            ParcelItem.parcel_item_value_client_currency)

    def add_next_custom_declaration_row(self):
        self.driver.find_element_by_xpath(CustomsDeclarationLocators.next_item_xpath).click()

    def check_if_invalid_weight_message_is_visable(self):
        return self.driver.find_element_by_xpath(InvalidMessageLocators.invalid_weight_xpath).is_displayed()


class ParcelItem:
    def __init__(self, parcel_item_number, parcel_item_description = '', parcel_item_quantity = '', parcel_item_weight = '',
    parcel_item_value_client_currency = ''):
        self.parcel_item_description = parcel_item_description
        self.parcel_item_quantity = parcel_item_quantity
        self.parcel_item_weight = parcel_item_weight
        self.parcel_item_value_client_currency = parcel_item_value_client_currency
        self.parcel_item_number = parcel_item_number


class Sender:

    def __init__(self, sender_name = '', sender_postal_code = '', sender_city = '',
                 sender_house_number = '', sender_flat_number = '', sender_phone = '', sender_email = ''):

        self.sender_name = sender_name
        self.sender_city = sender_city
        self.sender_postal_code = sender_postal_code
        self.sender_house_number = sender_house_number
        self.sender_flat_number = sender_flat_number
        self.sender_phone = sender_phone
        self.sender_email = sender_email



