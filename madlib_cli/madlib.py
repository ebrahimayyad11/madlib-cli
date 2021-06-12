import re

def welcome():
    print("""Hello, welcome to our game
    Insert an example of the language parts""")

data = ['Adjective','Adjective','A First Name','Past Tense Verb','A First Name','Adjective','Adjective',
'Plural Noun','Large Animal','Small Animal',"A Girl's Nam",'Adjective','Plural Noun','Adjective','Plural Noun',
'Number 1-50',"First Name's",'Number','Plural Noun','Number','Plural Noun']


newData = []

def insertData():
    for i in range(len(data)):
        newInput = input("Insert "+data[i]+"\n")
        newData.append(newInput)



# if __name__ == '__main__':
#     welcome()
#     # insertData()



def read_template(path):
    try:
        with open(path) as file:
          return file.read()
    except FileNotFoundError:
        print('error!')

readData = read_template("./assets/dark_and_stormy_night_template.txt")



def parse_template(data):
    modifiedData=re.sub('{[^}]+}','{}',data)
    removedData=re.findall('{(.*?)\}',data)
    return  modifiedData, removedData


parseData = parse_template(readData)
# parseData = parseData[0]



def merge(parseData,newData):
    return parseData.format(*newData)
    

def copy():
    with open('./assets/new_assets.txt', 'wb') as scriptWrite:
         return scriptWrite.write(bytes(merge(parseData,newData),'utf-8'))

# copy()




