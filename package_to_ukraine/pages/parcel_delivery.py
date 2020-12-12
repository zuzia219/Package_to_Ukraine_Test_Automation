
from package_to_ukraine.locators.locators import InvalidMessageLocators, StatementLocators, DeliveryMethodsLocators, DeliveryPointsLocators, ParcelLocators, ReceiverLocators, SenderLocators, CustomsDeclarationLocators
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
        parcel_send_button_index = delivery_method_index + 1
        send_button_xpath = "(" + ParcelLocators.parcel_send_locators + ")" + "[" + str(parcel_send_button_index) + "]"
        self.driver.find_element_by_xpath(send_button_xpath).click()

    def choose_first_available_delivery_point(self):
        self.driver.find_element_by_xpath(DeliveryPointsLocators.delivery_point_checkbox_xpath).click()

    def set_sender_info(self, Sender):
        self.driver.find_element_by_id(SenderLocators.sender_name_id).send_keys(Sender.sender_name)
        self.driver.find_element_by_id(SenderLocators.sender_city_id).send_keys(Sender.sender_city)
        self.driver.find_element_by_id(SenderLocators.sender_street_id).send_keys(Sender.sender_street)
        self.driver.find_element_by_id(SenderLocators.sender_postal_code_id).send_keys(Sender.sender_postal_code)
        self.driver.find_element_by_id(SenderLocators.sender_house_number_id).send_keys(Sender.sender_house_number)
        self.driver.find_element_by_id(SenderLocators.sender_flat_number_id).send_keys(Sender.sender_flat_number)
        self.driver.find_element_by_id(SenderLocators.sender_phone_id).send_keys(Sender.sender_phone)
        self.driver.find_element_by_id(SenderLocators.sender_email_id).send_keys(Sender.sender_email)
        
    def set_receiver_info(self, Receiver):
        self.driver.find_element_by_id(ReceiverLocators.receiver_name_id).send_keys(Receiver.receiver_name)
        self.driver.find_element_by_id(ReceiverLocators.receiver_phone_id).send_keys(Receiver.receiver_phone)

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


    def accept_order_form_regulation(self):
        self.driver.find_element_by_id(StatementLocators.order_form_regulation_id).click()

    def accept_order_form_regulation2(self):
        self.driver.find_element_by_id(StatementLocators.order_form_regulation_2_id).click()

    def accept_order_form_regulation3(self):
        self.driver.find_element_by_id(StatementLocators.order_form_regulation_3_id).click()

    def accept_order_prohibited_goods_id(self):
        self.driver.find_element_by_id(StatementLocators.order_prohibited_goods_id).click()


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
                 sender_house_number = '', sender_flat_number = '', sender_phone = '', sender_email = '', sender_street =''):

        self.sender_name = sender_name
        self.sender_city = sender_city
        self.sender_street = sender_street
        self.sender_postal_code = sender_postal_code
        self.sender_house_number = sender_house_number
        self.sender_flat_number = sender_flat_number
        self.sender_phone = sender_phone
        self.sender_email = sender_email
        
class Receiver:

    def __init__(self, receiver_name = '', receiver_postal_code = '', receiver_city = '',
                 receiver_house_number = '', receiver_flat_number = '', receiver_phone = '', receiver_email = ''):

        self.receiver_name = receiver_name
        self.receiver_city = receiver_city
        self.receiver_postal_code = receiver_postal_code
        self.receiver_house_number = receiver_house_number
        self.receiver_flat_number = receiver_flat_number
        self.receiver_phone = receiver_phone
        self.receiver_email = receiver_email



