



cows = {
            'A': 5,
            'B': 10,
            'C': 11,
            'D': 7,
            'E': 2,
            'Z': 4,
            'F': 3,
            'G': 29,
            'J': 29,
            'H': 1   }




total = 0
for j in cows.keys():
    total += cows[j]


print("Total: " + str(total))



def greedy_cow_transport(mycows, limit=50):

    # Copy the dictionary to work on duplicate
    copy_cows = dict(mycows)
    # Initialize an output list
    outlist = []
    
    
    # def keywithmaxvalfit(d, total, limit):
        # if len(d) != 0:
            # v=list(d.values())
            # k=list(d.keys())
            
            
    
    
    
    def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     if len(d) != 0:
        v=list(d.values())
        k=list(d.keys())
        return k[v.index(max(v))]
     else:
        return 0
     
    # sort copy_cows by value
    
    
    def greedy_grab(mydict):
        result = []
        total = 0
        
        mydictin = dict(mydict)
        
        # print keywithmaxval(mydict)
        
                  
        while total <= limit and len(mydict) != 0:
            maxkey=keywithmaxval(mydict)
            #
            # For other version
            if total + mydict[maxkey] > limit:
                # move to next key - HOW??
                break
            else:
                result.append(maxkey)
                total += mydict[maxkey]
                del copy_cows[maxkey]
            # print total
            # print result
        
        # for keys in mydict:
            # if total + mydict[keys] <= limit:
                # result.append(keys)
                # total += mydict[keys]
        # print copy_cows        
        return result

    # def update_dict(mydict, mylist):
        # for i in mylist:
            # del mydict[i]
        # return mydict        
        
    # print (greedy_grab(copy_cows))
    # print (update_dict(copy_cows, greedy_grab(copy_cows)))
    
    while len(copy_cows) > 0:
        outlist.append(greedy_grab(copy_cows))        
         
    
    return outlist
    
    
print (greedy_cow_transport(cows, limit=total*0.6))

