#PROBLEM 3: COUNTING AND GROUPING  (15 points possible)
#A catering company has hired you to help with organizing 
#and preparing customer's orders. You are given a list of 
#each customer's desired items, and must write a program that 
#will count the number of each items needed for the chefs 
#to prepare. The items that a customer can order are: salad, 
#hamburger, and water.
#
#Write a function called item_order that takes as input a 
#string named order. The string contains only words for the
#items the customer can order separated by one space. The 
#function returns a string that counts the number of each 
#item and consolidates them in the following order: salad:
#    [# salad] hamburger:[# hambruger] water:[# water]
#
#If an order does not contain an item, then the count for 
#that item is 0. Notice that each item is formatted as 
#[name of the item][a colon symbol][count of the item] 
#and all item groups are separated by a space.

order = "salad water hamburger salad hamburger"

def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    for i in range(len(order)):
        if order[i:i+5] == 'salad':
            salad += 1
        if order[i:i+9] == 'hamburger':
            hamburger += 1
        if order[i:i+5] == 'water':
            water += 1
    order = "salad:"+str(salad)+" hamburger:"+str(hamburger)+" water:"+str(water)
    return order    

