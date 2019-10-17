import json
from pypinyin import pinyin, lazy_pinyin, Style


class Entity(object):
    name = ""
    tel1 = ""
    tel2 = ""
    mobile = ""
    gongwei = ""
    chushi = ""
    bumen = ""
    pinyin = ""
    suoxie = ""
    company = ""
    leader = False

    def __init__(self, bumen, chushi, name, tel, mobile, gongwei, leader, company):
        if bumen is not None and isinstance(bumen,str):
            self.bumen = bumen.replace('\n', '')
        if chushi is not None and isinstance(chushi,str):
            self.chushi = chushi.replace('\n', '')
        if name is not None and isinstance(name,str):
            self.name = name.replace('\n', '')
        if tel is not None and isinstance(tel,str):
            self.tel1 = tel.replace('\n', '')
        if mobile is not None and isinstance(mobile,str):
            self.mobile = mobile.replace('\n', '')
        if gongwei is not None and isinstance(gongwei,str):
            self.gongwei = gongwei.replace('\n', '')
        if company is not None and isinstance(company,str):
            self.company = company.replace('\n', '')

        #self.bumen = bumen
        #self.chushi = chushi
        #self.name = name
        #self.tel1 = tel
        #self.mobile = mobile
        #self.gongwei = gongwei
        #self.leader = leader
        #self.company = company
        self.pinyin = ''.join(lazy_pinyin(self.name))
        self.suoxie = ''.join(lazy_pinyin(self.name, style=Style.FIRST_LETTER))

    def default(self, obj):

        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)

    def clear(self):
        if self.bumen is not None and isinstance(self.bumen,str):
            self.bumen = self.bumen.replace('\n', '')
        if self.chushi is not None and isinstance(self.chushi,str):
            self.chushi = self.chushi.replace('\n', '')
        if self.name is not None and isinstance(self.name,str):
            self.name = self.name.replace('\n', '')
        if self.tel1 is not None and isinstance(self.tel1,str):
            self.tel1 = self.tel1.replace('\n', '')
        if self.tel2 is not None and isinstance(self.tel2,str):
            self.tel2 = self.tel2.replace('\n', '')
        if self.mobile is not None and isinstance(self.mobile,str):
            self.mobile = self.mobile.replace('\n', '')
        if self.gongwei is not None and isinstance(self.gongwei,str):
            self.gongwei = self.gongwei.replace('\n', '')


