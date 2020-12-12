from package_to_ukraine.pages.parcel_search import SearchParcel
from package_to_ukraine.pages.parcel_delivery import ParcelDelivery, Sender

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


    def test_send_first_available_delivery_method(self, setup):
        self.driver.get("https://paczkadoukrainy.pl/")
        search_parcel_page = SearchParcel(self.driver)
        search_parcel_page.search_parcel_by_weight("10")
        delivery_page = ParcelDelivery(self.driver)
        first_available_delivery_method = delivery_page.fetch_available_deliveries()[0]
        delivery_page.choose_delivery_method(first_available_delivery_method)
        delivery_page.choose_first_available_delivery_point()
        sender = Sender( sender_name  =  "Mobisense Monika Mazurek",
                         sender_city  =  "Kielce",
                         sender_postal_code  =  "25-663",
                         sender_house_number  =  "1",
                         sender_flat_number  =  "1",
                         sender_phone  =  "664540929",
                         sender_email   =  "monika@monika.nl")
        delivery_page.set_sender_info(sender)



