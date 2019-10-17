import json
from entity import Entity


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        elif isinstance(obj, Entity):
            return { 'bumen':obj.bumen, 'chushi':obj.chushi, 'name':obj.name, 'tel1':obj.tel1, 'tel2':obj.tel2,
                     'mobile':obj.mobile, 'gongwei':obj.gongwei, 'pinyin':obj.pinyin, 'suoxie':obj.suoxie,
                     'leader': obj.leader, 'company': obj.company}

        return json.JSONEncoder.default(self, obj)
