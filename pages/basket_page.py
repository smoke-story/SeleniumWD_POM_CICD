from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    languages_all = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "en-gb": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty."
    }

    def should_not_be_items_in_basket(self):
        basket_items = self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        assert basket_items, "Basket is not empty..."
    
    def should_be_empty_basket_message(self):
        current_language = self.current_language()
        message_basket = self.driver.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert self.languages_all[str(current_language)] in message_basket, "wqtqwtqwt"
