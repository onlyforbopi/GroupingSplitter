#!/usr/bin/python

import time

#items = [ 1, 2, 3, 4, 5 ]
items = [ 4500, 61000, 32000, 5100, 1700, 18000, 52000, 43000, 1000, 10, 100000, 300, 800, 9999, 99999, 50, 3000, 2000, 93000 ]




def powerset(items):
	res = [[]]
	for item in items:
		newset = [r+[item] for r in res]
		res.extend(newset)
	return res
	
	
# for j in powerset(items):
    # print(j)
    
    
    
# BRUTE KNAPSACK - NO WEIGHTS, JUST VALUES
# GETS INPUT a list of items (values) and returns the
# combination with the highest possible value, that's 
# smaller than max_weight    
def brute_knapsack(items, max_weight):
    knapsack = []
    best_weight = 0
    best_value = 0
    for item_set in powerset(items):
        set_weight = sum(item_set)
        
        
        
        if set_weight < max_weight and set_weight > best_weight:
            best_weight = set_weight
            knapsack = item_set
    
    return knapsack, best_weight
    
    
    
    
#print(brute_knapsack(items, 76000*0.6))




# items: [(id, weight, value)]
def knapsack_greedy(items, max_weight):
	knapsack = []
	knapsack_weight = 0
    #knapsack_value = 0
	items_sorted = sorted(items)
	while len(items_sorted) > 0:
		item = items_sorted.pop()
		if item + knapsack_weight <= max_weight:
			knapsack.append(item)
			knapsack_weight += item
			#knapsack_value += value(knapsack[-1])
		else:
			break
	return knapsack, knapsack_weight
    
#print(knapsack_greedy(items, 76000))
   

#maxi = sum(items) * 0.5
maxi = sum(items) * 0.60
#maxi = sum(items) * 0.60
# maxi = sum(items) * 0.65
print(maxi)   
    
out_list = []
while len(items) > 0:
    
    #choice = brute_knapsack(items, maxi)
    choice = knapsack_greedy(items, maxi)
    print(choice)
    out_list.append(choice[0])
    
    #time.sleep(5)
    print(len(items))
    for j in choice[0]:
        if j in items:
            #print("Removing: " + str(j))
            items.remove(j)
            #print(items)
            
            
    
print(out_list)

# def knapsack(items, max_weight):

    # in_list = items
    
    # out_list = []
    
    # while len(in_list) > 0:
        # out_list.append(knapsack_greedy(in_list, max_weight)[0])
        # print(out_list)
        # print(len(in_list))
    
# print(knapsack(items, 70000))

   
    