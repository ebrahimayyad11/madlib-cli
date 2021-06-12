import re

def welcome_print():
    print(""" 
    Welcome to madlib game!
    all you need is to think of an example of the below vocabs 
    """)

data=['Adjective','Adjective','A First Name','Past Tense Verb','A First Name','Adjective','Adjective',
'Plural Noun','Large Animal','Small Animal',"A Girl's Nam",'Adjective','Plural Noun','Adjective','Plural Noun',
'Number 1-50',"First Name's",'Number','Plural Noun','Number','Plural Noun']

new_data=[]

def input_vocabs():
    for i in range (len(data)):
        input_val=input('>> Enter %s  '%(data[i]))
        new_data.append(input_val)


if __name__== '__main__':
    welcome_print()
    input_vocabs() 


def read_template(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError :
        raise FileNotFoundError('The file not found')
   

def parse_template(read_script):
    modified_script=re.sub('{[^}]+}','{}',read_script)
    removed_str_parts=tuple(re.findall("{(.*?)}",read_script))
    return  modified_script, removed_str_parts


def merge(parsed_script,user_input):
    return parsed_script.format(*user_input)



def script_copy(merged_script):
    with open('./assets/new_assets.txt','wb') as script_write:
         return script_write.write(bytes(merged_script,'utf-8'))