from package_to_ukraine.pages.parcel_search import SearchParcel
from package_to_ukraine.pages.parcel_delivery import ParcelDelivery, Sender, ParcelItem

import pytest

from package_to_ukraine.tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")

class TestParcelSend(BaseTest):

    @pytest.mark.xfail
    def test_send_parcel_w_punkcie_ruchu(self, setup):
        self.driver.get("https://paczkadoukrainy.pl/")
        search_parcel_page = SearchParcel(self.driver)
        search_parcel_page.search_parcel_by_weight("10")
        delivery_page = ParcelDelivery(self.driver)
        assert delivery_page.check_if_delivery_available("W punkcie RUCHU")


    def test_invalid_weight_message(self, setup):
        self.driver.get("https://paczkadoukrainy.pl/")
        search_parcel_page = SearchParcel(self.driver)
        search_parcel_page.search_parcel_by_weight("10")
        delivery_page = ParcelDelivery(self.driver)
        first_available_delivery_method = delivery_page.fetch_available_deliveries()[0]
        delivery_page.choose_delivery_method(first_available_delivery_method)
        delivery_page.choose_first_available_delivery_point()

        sender = Sender( sender_name= "Mobisense Monika Mazurek",
                         sender_city  =  "Kielce",
                         sender_postal_code  =  "25-663",
                         sender_house_number  =  "1",
                         sender_flat_number  =  "1",
                         sender_phone  =  "664540929",
                         sender_email   =  "monika@monika.nl")

        item1 = ParcelItem(parcel_item_description = "Czekoladki",
                           parcel_item_quantity = "2",
                           parcel_item_weight = "10",
                           parcel_item_value_client_currency = "20",
                           parcel_item_number = 1)

        item2 = ParcelItem(parcel_item_description = "Kubek",
                           parcel_item_quantity = "1",
                           parcel_item_weight = "2",
                           parcel_item_value_client_currency = "5",
                           parcel_item_number = 2
        )
        delivery_page.set_sender_info(sender)
        delivery_page.set_custom_declaration_row(item1)
        delivery_page.add_next_custom_declaration_row()
        delivery_page.set_custom_declaration_row(item2)
        assert delivery_page.check_if_invalid_weight_message_is_visable()



