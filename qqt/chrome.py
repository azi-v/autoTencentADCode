from selenium import webdriver


# Chrome 单例类
class Chrome(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_tab(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
