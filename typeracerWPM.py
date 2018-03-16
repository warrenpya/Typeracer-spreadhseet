import requests
import bs4
import openpyxl
import time

print("""
INSTRUCTIONS:

1. Create a spreadhseet file in the cwd. The type of file must be
                                    .xlsx, .xlsm, .xltx, or .xltm
2. Enter your username and file name

""")


#scrape website to figure out total number of races 
username = input('Enter username: ')
user_file = input('Enter filename: ')

res = requests.get('http://data.typeracer.com/pit/race_history?user='+username)

try:
    res.raise_for_status()
except Exception as exc:
    print('ERROR: %s' % (exc))

html = bs4.BeautifulSoup(res.text, 'html.parser')
elems = html.select('.scoresTable td')


races_num = elems[0].getText().strip()



#change url to include all races based on races_num, the total amount of races 
res = requests.get('http://data.typeracer.com/pit/race_history?user=warrenpya&n='+races_num+'&startDate=')



#scrape website again
try:
    res.raise_for_status()
except Exception as exc:
    print('ERROR: %s' % (exc))

html = bs4.BeautifulSoup(res.text, 'html.parser')
elems = html.select('.scoresTable td')




for i, value in enumerate(elems):
    elems[i] = value.getText().strip()




#setup spreadsheet
wb = openpyxl.load_workbook(user_file)
sheet = wb.active
sheet['A1'], sheet['B1'], sheet['C1'], sheet['D1'], sheet['E1'], sheet['F1'] = \
             'Race #', 'Speed', 'Accuracy', 'Points', 'Place', 'Date'



#add data
columns = ['A','B','C','D','E','F']

iterate = 0
row_count = 2
for x in elems:
    if iterate == 0:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 1:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 2:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 3:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 4:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 5:
        sheet[columns[iterate]+str(row_count)] = x
    elif iterate == 6:
        row_count += 1
        iterate = 0
        continue
    iterate += 1
        

wb.save('type_test.xlsx')

print('transfer complete!')
time.sleep(3)
quit()


