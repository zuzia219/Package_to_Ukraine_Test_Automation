class ParcelLocators:
    parcel_weight_name = "parcelWeight"
    parcel_search_xpath = "//*[text()[contains(.,'Zobacz ceny')]]"
    parcel_send_locators = "//*[text()[contains(.,'Nadaj paczkę')]]"

class DeliveryMethodsLocators:
    delivery_methods_xpath = "//div[contains(@class,'ng-scope')]/div/div/div[contains(@class,'card-header')]"

class SenderLocators:
    sender_name_id = "senderName"
    sender_postal_code_id = "senderPostalCode"
    sender_city_id = "senderCity"
    sender_street_id = "senderStreet"
    sender_house_number_id = "senderHouseNumber"
    sender_flat_number_id = "senderFlatNumber"
    sender_phone_id = "senderPhone"
    sender_email_id = "senderEmail"


class ReceiverLocators:
    receiver_name_id = "receiverName"
    receiver_postal_code_id = "receiverPostalCode"
    receiver_city_id = "receiverCity"
    receiver_street_id = "receiverAddressStreet"
    receiver_house_number_id = "receiverHouseNumber"
    receiver_flat_number_id = "receiverFlatNumber"
    receiver_phone_id = "receiverPhone"
    receiver_email_id = "receiverEmail"

class DeliveryPointsLocators:
    delivery_point_checkbox_xpath = "//label[text()='Dostawa do punktu odbioru']"
    delivery_point_search_xpath = "//input[@placeholder='Wyszukaj punkt odbioru (miasto, ulica)']"

class CustomsDeclarationLocators:
    parcel_item_description_name = "parcelItemDescription"
    parcel_item_quantity_name = "parcelItemQuantity"
    parcel_item_weight_name = "parcelItemWeight"
    parcel_item_value_client_currency_name = "parcelItemValueClientCurrency"
    parcel_item_number_class = "duty-item__lp-value"
    next_item_xpath = "//button[text()='Dodaj kolejną pozycję']"

class StatementLocators:
        order_form_regulation_id = "orderFormRegulation"
        order_form_regulation_2_id = "orderFormRegulation2"
        order_form_regulation_3_id = "orderFormRegulation3"
        order_prohibited_goods_id  ="orderProhibitedGoods"


class PayLocators:
        next_step_xpath = "//button[text()='Następny krok']"


class InvalidMessageLocators:
    invalid_weight_xpath = "//p[text()='Łączna waga paczki nie może być niższa od deklarowanej wagi zawartości']"






