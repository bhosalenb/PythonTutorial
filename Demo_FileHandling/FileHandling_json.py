import json
class Employee:
    def read(self):
        with open('FH.json','r') as fr:
            for data in fr:
                temp= json.loads(data)
                print(data)

if __name__ == '__main__':
    e1 = Employee()
    e1.read()


