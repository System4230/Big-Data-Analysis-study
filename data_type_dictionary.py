Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic = {'name':'Hong', 'phone':'01012345678', 'birth':'0814'}
>>> dic[1] = 'a'
>>> dic
{'name': 'Hong', 'phone': '01012345678', 'birth': '0814', 1: 'a'}
>>> dic['pet'] = 'dog'
>>> dic
{'name': 'Hong', 'phone': '01012345678', 'birth': '0814', 1: 'a', 'pet': 'dog'}
>>> 
>>> del dic[1]
>>> dic
{'name': 'Hong', 'phone': '01012345678', 'birth': '0814', 'pet': 'dog'}
>>> 
>>> # 원소의 value 구하기
>>> dic['pet']
'dog'
>>> dic['name']
'Hong'
>>> 
>>> # key 리스트 만들기
>>> dic.keys()
dict_keys(['name', 'phone', 'birth', 'pet'])
>>> list(dic.keys())
['name', 'phone', 'birth', 'pet']
>>> 
>>> # value 리스트 만들기
>>> dic.values()
dict_values(['Hong', '01012345678', '0814', 'dog'])
>>> list(dic.values())
['Hong', '01012345678', '0814', 'dog']
>>> 
>>> # key 와 value 쌍 구하기
>>> dic.items()
dict_items([('name', 'Hong'), ('phone', '01012345678'), ('birth', '0814'), ('pet', 'dog')])
>>> 
>>> # 삭제
>>> dic.clear()
>>> dic
{}
