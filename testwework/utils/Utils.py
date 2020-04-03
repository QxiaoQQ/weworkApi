import json


class Utils:
    @classmethod
    def format(cls,json_object):
        # 加上@classmethod 方法就可以在调用的时候少写个实例化 Utils()--》 直接写成 Utils
        # 转为json格式，并缩进2个字符
        return json.dumps(json_object, indent=2)
