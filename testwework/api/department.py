import requests


from testwework.api.WeWork import WeWork
from testwework.api.baseapi import BaseApi


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    def list(self,id):
        r =requests.get(self.list_url,params={"access_token":WeWork.get_token(),"ID": id}).json()
        self.verbose(r)
        return r

    def creat(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
