import os
import fileinput
import sys

class Edit(object):

    def __init__(self,project):
        self.project = project
        test = self.test_project()

    def add_item(self):
        name = str(input("Name of Item: "))
        price = float(input("Price of item: "))
        priority = int(input("purchase priority: "))
        index = self.get_index("items")
        f = open(str(self.project) + "/items.dat", 'a')
        f.write("\n")
        f.write("{")
        f.write("index:[" + str(index)+ "],")
        f.write(name+",")
        f.write(str(price)+",")
        f.write(str(priority)+",")
        f.write("}")
        f.close()

    def add_other(self,type):
        name = str(input("Name of "+str(type)+": "))
        price = float(input("Size of "+str(type)+": "))
        index = self.get_index(str(type)+"s")
        f = open(str(self.project) + "/"+str(type)+"s.dat", 'a')
        f.write("\n")
        f.write("{")
        f.write("index:[" + str(index)+ "],")
        f.write(name+",")
        f.write(str(price)+",")
        f.write("}")
        f.close()

    def test_project(self):
        try:
            f = open(str(self.project) + "/project.ignore",'r')
            for line in f:
                if line == "True":
                    return True
        except Exception as e:
            print("This project does not exist, check spelling or create a project.")
            sys.exit()

    def print_stock(self,type):
        f = open(str(self.project) + "/"+str(type)+"s.dat", 'r')
        for line in f:
            print(line)

    def create_new_project(self,name):
        os.system("mkdir " + str(name))
        f = open(str(name) + "/items.dat",'w')
        f.close()
        f = open(str(name) + "/incomes.dat",'w')
        f.close()
        f = open(str(name) + "/expences.dat",'w')
        f.close()
        f = open(str(name) + "/assets.dat",'w')
        f.close()
        f = open(str(name) + "/project.ignore",'w')
        f.write("True")
        f.close()

    def get_index(self,file):
        f = open(str(self.project) + "/" + str(file) + ".dat", 'r')
        index = 0
        for line in f:
            try:
                index_temp = line.split("[")[1]
                index = int(index_temp.split("]")[0])

            except Exception as e:
                continue
        return index+1

    def remove_index(self,file,index):
        for line in fileinput.input(str(self.project) + "/" + str(file) + "s.dat", inplace=1):
            if ("["+str(index)+"]") in line:
                line = ""
            sys.stdout.write(line)

def create_new_project(name):
    os.system("mkdir " + str(name))
    f = open(str(name) + "/items.dat",'w')
    f.close()
    f = open(str(name) + "/incomes.dat",'w')
    f.close()
    f = open(str(name) + "/expences.dat",'w')
    f.close()
    f = open(str(name) + "/assets.dat",'w')
    f.close()
    f = open(str(name) + "/project.ignore",'w')
    f.write("True\n")
    f.close()

class Edit_Ui(object):

    def load():
        os.system('cls')
        if str(input("open current project(Y), or create new project(n)?")) == "Y":
            os.system('cls')
            project = str(input("Name of project?"))
            os.system('cls')
            current_edit = Edit(project)
            if str(input("do you want to make edits to your project?(Y,n)")) == "Y":
                while True:
                    if str(input("add(Y) or remove(n)")) == "Y":
                        os.system('cls')
                        type = str(input("what type of entry do you want to add? (item,expence,income,asset)"))
                        os.system('cls')
                        if type == "item":
                            current_edit.add_item()
                        else:
                            try:
                                current_edit.add_other(type)
                            except Exception as e:
                                print("cannot add this entry, check spelling")
                                continue
                    else:
                        type = str(input("what type of entry do you want to remove? (item,expence,income,asset)"))
                        os.system('cls')
                        current_edit.print_stock(type)
                        try:
                            current_edit.remove_index(type,int(input("index of entry you want to remove: ")))
                            os.system('cls')
                        except Exception as e:
                            print("could not remove this item, try again and check spelling")
                            continue
                    if str(input("Want to make more edits?(Y,n)")) == "n":
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                return project
            else:
                return project
        else:
            create_new_project(str(input("Name of new project?\n")))
            print("Project succsesfully created")
