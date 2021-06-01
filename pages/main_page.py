from .base_page import BasePage


class MainPage(BasePage):
    # вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)