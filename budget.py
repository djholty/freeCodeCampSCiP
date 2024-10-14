from typing import List
import math

class Category:
    def __init__(self, categoryname:str):
        self.ledger = []
        self.balance = 0
        self.categoryname = categoryname
  
    def deposit(self, amount=0, description=''):
        """Deposits money into the budget"""
        self.ledger.append({"amount": amount, "description":description})
        self.balance += amount

    
    def check_funds(self, amt):
        if amt > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount, description=''):
        """Withdraws funds if there is sufficient cash"""
        x = self.check_funds(amount) #checks to see if withdrawal amount is smaller than balance.  If funds available return True
        if x is False:
            print('Insufficient Funds')
            return False #withdrawal did not take place so False
        else:
            self.ledger.append({'amount': -amount, 'description':description})
            self.balance -= amount
            return True # withdrawal took place so True

    def transfer(self, amount:float, transfercateg:object) -> bool:
        """ 
        Transfer money from one budget object to another as long as there is enough funds.  It will
        return false if not enough funds and true if there are and the transfer goes through 
        """
        x = self.check_funds(amount)
        if x is False:
            print('Insufficient Funds, transfer did not occur')
            return False #transfer did not take place so False
        else:
            self.ledger.append({'amount': -amount, 'description':f'Transfer to {transfercateg.categoryname}'})
            self.balance -= amount
            transfercateg.ledger.append({'amount':amount, 'description':f'Transfer from {self.categoryname}'})
            transfercateg.balance += amount
            return True # withdrawal took place so True

    
    def get_balance(self):
        return self.balance

    def __str__(self):
        """ Outputs a list of transactions for the budget object"""
        output = ''
        output += f'{self.categoryname:*^30}\n'
        for item in self.ledger:
            output += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
        output += f'Total: {self.get_balance()}'
        return output
        

def percent_spends_dots(category_list)-> str:
    """
    Calculates the percent spending for each category, rounds it to the nearest 10, and turns 
    each 10% into a 'o' character with appropriate padding for the height of the column printout
    """
    total_spend = get_total_spending(category_list) #gets total spending in all categories
    percent_spends = []
    for category in category_list:
        percent_withdrawal = (round(get_withdrawals(category)*100//total_spend, ))/10 + 1  # use round function to round up to nearest 10
        dots = 'o'*int(percent_withdrawal)
        dots = dots.rjust(11, ' ') #padded to the height of the column in spend chart b/c it starts from 0
        percent_spends.append(dots)
    return percent_spends

    
def get_withdrawals(categ: object)-> float:
    """ Calculates the total withdrawals for a budget object"""
    withdrawal_categ = 0
    for dic in categ.ledger:
        if dic['amount'] < 0: 
            withdrawal_categ += dic['amount']
    return -withdrawal_categ #returns a positive value b/c it multiplies by -1 after adding up all negative withdrawals

def get_total_spending(category_list)->float:
    """ 
    Iterates through a list of budgets, finds spending for each budget object, adds it up
    and returns total spending for all of them together
    """
    total_spending = 0
    for category in category_list:
        total_spending += get_withdrawals(category)
    return total_spending

def create_spend_chart(category_list)->str:
    """Gathers together percent spending and prints out a graph of the spending by category"""
    output = ''
    output += f'Percentage spent by category' 
    dots = percent_spends_dots(category_list) #gets the spending 'o's for each category 
    sidenumbers = list(range(100,-1,-10)) #gets the y axis values from 100 to 0
    zipped_dots = zip(sidenumbers,*dots)  #zips up all the lists together
    #print(list(zipped_dots))
    for tup in zipped_dots:
        output += '\n'  
        number, a, b, c = tup
        output += f'{number:3}| {a}  {b}  {c}  '
    output += '\n'
    output += f'    ----------'  
    category_names = [category.categoryname for category in category_list] #get a list of category names
    longeststrlength = len(max(category_names, key = len)) #get the length of longest string
    categ_names_padded = [i.ljust(longeststrlength) for i in category_names] #use length to pad names when zipping
    zipped = zip(*categ_names_padded)
    
    for tup in zipped:
        output += '\n'
        a,b,c = tup
        output += f'     {a}  {b}  {c}  '
    
        
    return output
    
