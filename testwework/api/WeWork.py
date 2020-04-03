import requests


class WeWork:
    corpid = "wwf7dccb7e27452163"
    secret = "6TRTJpcYXSJMGNYY4OtfiayLts1LYX5rsOkAFz52ats"
    access_token = None

    @classmethod
    def get_token(cls):
        if cls.access_token == None:
            url ="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r =requests.get(url, params={"corpid":cls.corpid, "corpsecret":cls.secret}).json()
            print(r)
            print("frist get token ")
            cls.access_token = r["access_token"]

        return WeWork.access_token