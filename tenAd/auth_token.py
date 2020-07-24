import time

from qqt.chrome import Chrome
from qqt.tencent_sdk import TencentSDK

auth_code_url = "https://developers.e.qq.com/oauth/authorize?client_id=1110673276&redirect_uri=https://m.risecenter.com/guangdiantong/UserActions.php&account_type=ACCOUNT_TYPE_QQ"


class TencentAD(Chrome):
    def __init__(self):
        super().__init__()
        self.qq_login_button = []
        self.qq_login_a_link = []
        self.u_input = []
        self.p_input = []
        self.login_button2 = []
        self.select_account_button = []
        self.col_checkbox = []
        self.account_id_sort_no = 0
        self.auth_code_url = ''
        self.auth_code = ''
        self.account_id_auth_code_dict = dict()
        self.tencent_sdk = TencentSDK()
        self.tencent_ad_access_token_dict = dict()
        self.account_access_token_dict = dict()
        self.tencent_ad_action_set_id = dict()
        self.account_set_id_dict = dict()
        self.account_refresh_token_dict = dict()

    def click_qq_login(self, qq_no, qq_pwd):
        self.open_tab(auth_code_url)

        time.sleep(2)

        self.qq_login_button = self.driver.find_element_by_class_name("tc-btn")
        self.qq_login_button.click()

        time.sleep(2)

        self.driver.switch_to_frame("ptlogin_iframe")
        self.qq_login_a_link = self.driver.find_element_by_id("switcher_plogin")
        self.qq_login_a_link.click()

        time.sleep(2)

        self.u_input = self.driver.find_element_by_id("u")
        self.u_input.send_keys(qq_no)

        time.sleep(2)

        self.p_input = self.driver.find_element_by_id("p")
        self.p_input.send_keys(qq_pwd)

        time.sleep(2)

        self.login_button2 = self.driver.find_element_by_class_name("login_button")
        self.login_button2.click()

        time.sleep(3)

        self.driver.switch_to_default_content()

        time.sleep(2)

        # 点击展示下拉account列表
        self.select_account_button = self.driver.find_element_by_css_selector(".meta-select")
        self.select_account_button.click()

        time.sleep(2)

        # 点击选中account
        self.col_checkbox = self.driver.find_elements_by_class_name("spaui-table-tr-data")

        account_id_auth_code_dict = dict()

        for i in range(len(self.col_checkbox)):
            account_id = self.col_checkbox[i].find_element_by_class_name("col-id").find_element_by_class_name(
                "spaui-table-td-inner").text

            self.col_checkbox[i].click()

            time.sleep(2)

            # 点击页面空白处
            self.driver.find_element_by_class_name("meta-select").click()

            time.sleep(2)

            # 点击获取认证code
            self.driver.find_element_by_class_name("tc-btn").click()

            # 等待页面跳转
            time.sleep(5)

            self.auth_code_url = self.driver.current_url

            self.auth_code = self.auth_code_url.split('?')[1].split('&')[0].split('=')[1]

            account_id_auth_code_dict[account_id] = self.auth_code

            # 返回页面
            self.driver.back()

            time.sleep(3)

            self.select_account_button = self.driver.find_element_by_css_selector(".meta-select")
            self.select_account_button.click()

            time.sleep(2)

            # 点击选中account
            self.col_checkbox = self.driver.find_elements_by_class_name("spaui-table-tr-data")

        self.account_id_auth_code_dict = account_id_auth_code_dict

    def get_access_token(self):
        for key, value in self.account_id_auth_code_dict.items():
            result = self.tencent_sdk.oauth_token(value)
            self.tencent_ad_access_token_dict[key] = result
            self.account_access_token_dict[key] = result["data"]["access_token"]
            self.account_refresh_token_dict[key] = result["data"]["refresh_token"]

    def get_action_set_id(self):
        for key, value in self.tencent_ad_access_token_dict.items():
            access_token = value["data"]["access_token"]
            result = self.tencent_sdk.user_action_sets_add(key, access_token)
            self.tencent_ad_action_set_id[key] = result
            self.account_set_id_dict[key] = result["data"]["user_action_set_id"]
