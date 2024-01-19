import string
import random
from pathlib import Path
import json

class Students:
    data = []
    database = './projects/stud.json'
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(err)
    
    @classmethod
    def update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @classmethod
    def randomid(cls):
        alp = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        sp = random.choices('!@#$%^&*', k=2)
        id = alp + num + sp
        random.shuffle(id)
        return ''.join(id)
    
    @classmethod
    def register(cls):
        stud = {
            'id': cls.randomid(),
            'name': input('Name: '),
            'email': input('Email: '),
            'password': input('Password: '),
            'skill': input('Skill: ')
        }
        cls.data.append(stud)
        cls.update()
    
    @classmethod
    def readSingle(cls):
        id = input('ID: ')
        password = input('Password: ')
        student = [i for i in cls.data if i['id']==id and i['password']==password]
        if len(student) == 0:
            print('Invalid Credentials')
        else:
            for j in student[0]:
                print(f'{j} : {student[0][j]}')
        
    @classmethod
    def updateData(cls):
        id = input('ID: ')
        password = input('Password: ')
        student = [i for i in cls.data if i['id']==id and i['password']==password]
        if len(student) == 0:
            print('Invalid Credentials')
        else:
            print('Enter to skip')
            stud = {
                'name': input('Name: '),
                'email': input('Email: '),
                'password': input('Password: '),
                'skill': input('Skill: '),
            }
        
        if stud['name'] == '':
            stud['name'] = student[0]['name']
        if stud['email'] == '':
            stud['email'] = student[0]['email']
        if stud['password'] == '':
            stud['password'] = student[0]['password']
        if stud['skill'] == '':
            stud['skill'] = student[0]['skill']
            
            
        for i in stud.keys():
            if stud[i] == student[0][i]:
                continue
            else:
                student[0][i] = stud[i]
        cls.update()
        
    @classmethod
    def access(cls):
        studdata = cls.data
        for stud in studdata:
            print()
            for j in stud:
                print(f'{j} : {stud[j]}')
        
    @classmethod
    def delete(cls):
        id = input('ID: ')
        password = input('Password: ')
        student = [i for i in cls.data if i['id']==id and i['password']==password]
        if len(student) == 0:
            print('Invalid Credentials')
        else:
            check = input('Y/N: ')
            if check == 'Y':
                studind = cls.data.index(student[0])
                cls.data.pop(studind)
                cls.updateData()
            elif check == 'N':
                pass
            else:
                print('Wrong response')
                
while(True):           
    print('''
        1. Register
        2. Login
        3. Access
        4. Update
        5. Delete
        0. Exit
        ''')
    n = int(input('Response: '))

    if n == 0:
        exit(0)
    if n == 1:
        Students.register()
    if n == 2:
        Students.readSingle()
    if n == 3:
        Students.access()
    if n == 4:
        Students.updateData
    if n == 5:
        Students.delete()