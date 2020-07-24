import json

from tenAd.auth_token import TencentAD


def get_user_auth_code():
    qq_no = "*********"  # input("请输入QQ号:")
    qq_pwd = "*********"  # input("请输入QQ密码:")

    ad = TencentAD()

    ad.click_qq_login(qq_no=qq_no, qq_pwd=qq_pwd)
    ad.close()

    ad.get_access_token()
    # ad.get_action_set_id()

    with open("./auth_code.json", "a") as f1:
        f1.write(json.dumps(ad.account_id_auth_code_dict) + "\n")
    with open("./access_token.json", "a") as f2:
        f2.write(json.dumps(ad.tencent_ad_access_token_dict) + "\n")
    with open("./action_set_id.json", "a") as f3:
        f3.write(json.dumps(ad.tencent_ad_action_set_id) + "\n")
    with open("./account_set_id.json", "a") as f3:
        f3.write(json.dumps(ad.account_set_id_dict) + "\n")
    with open("./account_access_token.json", "a") as f3:
        f3.write(json.dumps(ad.account_access_token_dict) + "\n")
    with open("./account_refresh_token.json", "a") as f3:
        f3.write(json.dumps(ad.account_refresh_token_dict) + "\n")


if __name__ == '__main__':
    get_user_auth_code()
