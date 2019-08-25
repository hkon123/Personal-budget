from item import Item
from income import Income
from expence import Expence
from assets import Asset
import matplotlib.pyplot as plt
import numpy as np
import sys

class Budget(object):

    def __init__(self,project):
        self.items = []
        self.incomes = [Income("Base",0)]
        self.expences = []
        self.assets = []
        self.project = project
        self.read_files()

    def read_files(self):
        f = open(str(self.project) + "/items.dat",'r')
        for line in f:
            try:
                list = line.split(",")
                self.add_item(str(list[1]),float(list[2]),int(list[3]))
            except Exception as e:
                continue
        f.close()
        f = open(str(self.project) + "/expences.dat",'r')
        for line in f:
            try:
                list = line.split(",")
                self.add_expence(str(list[1]),float(list[2]))
            except Exception as e:
                continue
        f.close()
        f = open(str(self.project) + "/incomes.dat",'r')
        for line in f:
            try:
                list = line.split(",")
                self.add_income(str(list[1]),float(list[2]))
            except Exception as e:
                continue
        f.close()
        f = open(str(self.project) + "/assets.dat",'r')
        for line in f:
            try:
                list = line.split(",")
                self.add_asset(str(list[1]),float(list[2]))
            except Exception as e:
                continue
        f.close()

    def add_item(self,name,price,priority):
        self.items.append(Item(name,price,priority))

    def add_income(self,source,amount):
        self.incomes.append(Income(source,amount))

    def add_expence(self,source,amount):
        self.expences.append(Expence(source,amount))

    def add_asset(self,source,amount):
        self.assets.append(Asset(source,amount))

    def get_endOfMonth_bottomline(self):
        return self.incomes[0].total_income - self.expences[0].total_expence

    def get_end_of_month_one(self):
        return self.assets[0].total_assets + self.incomes[0].total_income - self.expences[0].total_expence

    def generate_projection(self,months):
        end_of_month = self.get_end_of_month_one()
        projection = [end_of_month]
        for i in range(months):
            end_of_month += self.get_endOfMonth_bottomline()
            projection.append(end_of_month)
        return projection

    def print_items(self):
        print(str(self.items[0].num_items) + "  items in budget \n\n")
        for item in self.items:
            print(str(item.priority) + ". " + str(item.name) + "  " +str(item.price) + "kr ")
        print("\n\n")
        print("Total value of budget: " + str(self.items[0].total_value))

    def plot_year_projection(self):
        assets = self.generate_projection(12)
        months = np.arange(len(assets))
        plt.plot(months,assets)
        plt.xlabel("Month")
        plt.ylabel("Assets")
        plt.title("1-year projection of income and expences")
        plt.show()
