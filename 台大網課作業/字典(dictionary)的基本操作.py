movie1={'name':'Jackson',
       'year':1998,
       'director':'Sam'}
movie2=dict(name='qwee',
            year=2048,
            director='gol')
movie3={'name':'hil',
        'year':1985,
        'director':'jiol'}
print(movie1['name'])
print(movie2['year'])
print(movie3['director'])
print(movie1.get('gio'))    #輸入一個不存在的key的話，程式會回傳錯誤的訊息，如果使用get method來存取值，此時就算key並不存在，程式會回傳None而不是錯誤訊息
print(movie1.get('hjbi','not found'))   #not found的使用在於之後會回傳的不是None而是not found

#新增key-value
movie1['star']='bjkll'
print('新增一個資料:',movie1)

#新增多個key-value
temp_dict={'writer':'hio',
           'stars':['gboui','fuyhiu','fyfugu'],
           'Oscar':['ufiui','guykui','guyiui','hilhjo']}
movie1.update(temp_dict)
print('新增多個資料:',movie1)

#刪除資料
del movie1['star']
print('刪除一個資料:',movie1)
writer=movie1.pop('writer')
print('刪除的資料回傳:',writer)

#呼叫全部key、value、items
print('呼叫key:',movie1.keys())
print('呼叫value:',movie1.values())
print('呼叫整個字典:',movie1.items())


