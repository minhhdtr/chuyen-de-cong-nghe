from bs4 import BeautifulSoup 
import requests
import json


url = 'https://xskt.com.vn/xsmb/100-ngay'
result = requests.get(url=url)

content = result.text
soup = BeautifulSoup(content)
kqmbs = soup.find_all('table',class_='result')


data = []
for kqmb in kqmbs:
    # print('============================================================')
    kq = {}
    kq['time'] = kqmb.find('i',class_='dockq')['title']
    kq['db'] = kqmb.find('td', title='Giải ĐB').find_next('em').text
    kq['g1'] = kqmb.find('td', title='Giải nhất').find_next('p').text
    kq['g2'] = kqmb.find('td', title='Giải nhì').find_next('p').text.split(' ')
    g3 = list(kqmb.find('td', title='Giải ba').find_next('p').stripped_strings)
    kq['g3'] = g3[0].split(' ') + g3[1].split(' ')
    kq['g4'] = kqmb.find('td', title='Giải tư').find_next('p').text.split(' ')
    g5 = list(kqmb.find('td', title='Giải năm').find_next('p').stripped_strings)
    kq['g5'] = g5[0].split(' ') + g3[1].split(' ')
    kq['g6'] = kqmb.find('td', title='Giải tư').find_next('p').text.split(' ')
    kq['g7'] = kqmb.find('td', title='Giải tư').find_next('p').text.split(' ')
    data.append(kq)
    # print('============================================================')
print(len(data))
json_data = json.dumps(data, ensure_ascii=False, indent=4)

# Ghi chuỗi JSON vào file
with open('data.json', 'w') as file:
    file.write(json_data)
    
print("File JSON đã được tạo thành công.")

