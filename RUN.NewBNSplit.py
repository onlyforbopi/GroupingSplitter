#!/usr/bin/python





# ##########################################################################
# Necessary Modules
import sys
import os
import time


try:
    import collections
except:
    print("Failed to load module: Collections")
    sys.exit(1)
else:
    print("Module: collections loaded succesfully")

try:
    import argparse
except:
    print("Failed to load argparse. Terminating")
    sys.exit(2)


# ##########################################################################
# Initiate Parser
# MODIFY: CENTRAL HELP TEXT
parser = argparse.ArgumentParser(
        prog="BNSplitcalc", 
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        #description="calculate X to the power of Y",
        description='''\
#        
#       BNSplit v.2
#       --------------------------------
#       Author: p.doulgeridis
#       Description: Splits a text file into a number
#       of files that have size = lines_in provided, 
#       keeping the groupings intact.
#
#       Caution: Certain files may exceed limit due to grouping.
#
#        ''',
        epilog="Additional info")


#######
# Initiate mutually exclusive group. 
# SET BY DEFAULT FOR VERBOSE/QUIET
# IF YOU NEED MORE EXCLUSIVE OPTIONS, ADD A DIFFERENT GROUP.
#
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0)
group.add_argument("-q", "--quiet", action="store_true")        


######
# Positional Arguments (Necessary)
# POSSIBLE KINDS (actions, types)
#
parser.add_argument("file", type=str, help="Provide the file")
# parser.add_argument("start", type=int, help="Provide the beginning of substring - notepad++ column")
# parser.add_argument("end", type=int, help="Provide the end of the substring - notepad++ column")


###### 
# Parse arguments
args = parser.parse_args()


######
# Assign arguments
# NUM_OF_LINES=args.lines




# ##################################################################
# Declare functions and wrappers


# Reporting func
def reporting(lines_in):
    print("Operation Finished. Read: " + str(lines_in) + " lines.")

    

# file exists
def fileexists(filepath):
  '''
  Function: filexists
  Description: Checks for existence of file
  Input: filepath (or raw string of it)
  Output: Boolean
  Usage: if filexists(file_in):...
  Notes: Depending on system may need to 
  conver to raw string with r'file_in.
  '''
  import os.path
  if os.path.exists(filepath):
    return True
  else:
    return False    

    
    
# isinteger
def typecheck(input, type):
    return isinstance(input, type)

    
    
# file backup
def backupfile(src):
    import shutil
    backup = str(src) + ".bak"

    
    
# script params
def script_path_param(string1, vocal = 'yes'):
    '''
    Name:
    Function:
    Input:
    Output:
    Usage:
    Notes:
    '''
    #import sys
    #import os
    # Called as: script_path_param(sys.argv[0])
    
    try:
        script_name = os.path.basename(string1)
        script_dir = os.path.dirname(os.path.realpath(string1))
        script_full = script_dir + script_name
    except:
        print("Error loading script parameters. Possible problem with os module")
    
    if vocal != 'yes': 
        return ( script_name, script_dir, script_full )
    else:
        print("Script name: " + str(script_name))
        print("Script directory: " + str(script_dir))
        print("Script full: " + str(script_full))
        print ('Script started at: ' + time.strftime("%c"))
        return True


def pretty_print(b):
    '''
    Function: pretty_print
    Description : Pretty prints a dictionary
    Input : Dictionary
    Output: STDOUT
    Usage(print) : pretty_print(b)
    Usage(Assign): b = pretty_print(b) - True
    Notes : Only prints on screen
    '''
    print ("{ ")
    for a in b.keys():
        print ( "\t" + str(a) + " : " + str(b[a]) )
    print ("}\n")        
        
        
# Script End
def script_end():
    import time
    print("Script ended at: " + time.strftime("%c"))
    
 
 
# script time param
def script_time_param():
    # Name: time parameter
    # Function: script_time_param
    # Input: None
    # Output: string with formatted time
    # Usage: print (script_time_param) or a = script_time_param
    return time.strftime("%c")



def keywithmaxval(d):
 """ a) create a list of the dict's keys and values; 
     b) return the key with the max value"""  
 if len(d) != 0:
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]
 else:
    return 0    

    
    
def gettotalvalue(list_in, dict_in):
    
    in_dict = dict(dict_in)
    
    #print(in_dict)
    ot = 0
    for j in list_in:
        #print(j, typecheck(j, str),in_dict[j])
        ot += dict_in[j]
        
    return ot
    
    
    
def dictfunc(dict_in):
    print(dict_in)
    
    
    
def process(dict_in, limit_in):
    itercounter = 0
    dict_copy = dict(dict_in)
    pretty_print(dict_copy)
    print("LIMIT IS: " + str(limit_in))
    
    while len(dict_copy) != 0:
        itercounter += 1
        proc_key = keywithmaxval(dict_copy)
        print(proc_key)
    
        
        outlist1_length = gettotalvalue(outlist1, dict_count)
        outlist2_length = gettotalvalue(outlist2, dict_count)
        
        print("Outlist1: " + str(outlist1_length))
        print("Outlist2: " + str(outlist2_length))
    
        if itercounter % 2 == 1:
            outlist1.append(proc_key)
            del dict_copy[proc_key]
        else:
            outlist2.append(proc_key)
            del dict_copy[proc_key]    
    
        if gettotalvalue(outlist1, dict_count) > limit_in:
            print("LIMIT EXCEEDED")
            for j in dict_copy.keys():
                outlist2.append(j)
                del dict_copy[j]
            
            print(outlist1, gettotalvalue(outlist1, dict_count))
            print(outlist2, gettotalvalue(outlist2, dict_count))
            return (outlist1, outlist2)

            
        
        #pretty_print(dict_copy)
    
    
    
    
    
        #del dict_copy[proc_key]
    
    # pretty_print(dict_count2)
    # pretty_print(dict_count)
    
    print(outlist1, gettotalvalue(outlist1, dict_count))
    print(outlist2, gettotalvalue(outlist2, dict_count))


    
    return (outlist1, outlist2)
    
    
    
# ##################################################################
# PARSE ARGUMENTS AND FORMAT
try:
    file_in = args.file
    start_in = 2
    end_in = 6
except:
    print("Failed to parse arguments")
else:
    print("Arguments parsed succesfully")
finally:
    start_in = int(start_in)
    end_in = int(end_in)
    
    
    
# ###################################################################
# CHECKS

if not fileexists(file_in):
    print("Error: Input file could not be located. Terminating.")
    sys.exit(1)

if not typecheck(start_in, int):
    print("\n" + "Error: Provided number is not an integer. Terminating")
    sys.exit(9)

if not typecheck(end_in, int):
    print("\n" + "Error: Provided number is not an integer. Terminating")
    sys.exit(9)    
    
# if not typecheck(input_line_limit, int):
    # print("\n" + "Error: Provided number is not an integer. Terminating")
    # sys.exit(9)
    
    
    
    
    
# #####################################################################
# Initialize Iteration Vars
# #####################################################################    
    
group = ""
prev_group = ""
file_count = 0
counter2 = 0
dict_group = {}


# #####################################################################
# Script Start
# #####################################################################

# Handle quiet/verbose arguments
if args.quiet:
    pass
elif args.verbose:

    # Handle multiple verbosity values (ie, -vvv)
    if args.verbose > 3:
        # full script reporting
        print("\n" + "Launching script:")
        script_path_param(sys.argv[0])
        print("\n")
        chck_args_type(sys.argv)
    elif args.verbose >= 2:
        script_path_param(sys.argv[0])
    elif args.verbose >= 1:
        print("Processing file: " + str(file_in))

        
        
# Calculate input_line_limit
print("Calculating input line limit....")
count = len(open(file_in).readlines())
print("Total line count: " + str(count))
input_line_limit = int(count / 2)
print("Estimated split: " + str(int(count / 2)))
print("Estimated split: " + str(input_line_limit))

# Initialize two dicts
#   1. for entire data 
#   2. for counters and picking
dict_out = collections.defaultdict(list)
dict_count = collections.defaultdict(int)


#print(start_in)
#print(end_in)


print("Reading input file and populating dict...")
with open(file_in, 'r') as f:
    for line in f:
        file_count += 1
        line_fixed = line.rstrip("\n")
        key = line_fixed[start_in:end_in]
        #print(key)
        dict_out[key].append(line_fixed)
        
        
#pretty_print(dict_out)

print("Reading populated dict, creating counter dict")
for key_in in dict_out.keys():
    dict_count[key_in] = len(dict_out[key_in])
    counter2 += dict_count[key_in]
    
print("\n" + "Reporting:")    
print("read: " + str(file_count))
print("dict: " + str(counter2))    
pretty_print(dict_count)

#print(keywithmaxval(dict_count))
#print(len(dict_count))

# Initialize output lists, and processed key list.
outlist1 = []
outlist2 = []
processed_keys = []
out_counter = 0


# ##################################################################
# Main Job
# ##################################################################

# Initialize output filenames
file_ot = str(file_in) + ".out.0.txt"
file_ot2 = str(file_in) + ".out.1.txt"

# Open output files
outfile1 = open(file_ot, 'w')
outfile2 = open(file_ot2, 'w')

# Calculating split 
# Call on main function -> process
print("Calculate split....")
output = process(dict_count, input_line_limit)
print("Output is: " + str(output))

print("Processing 1st list: " + str(output[0]))
for j in output[0]:
    print("Processing key and writing : " + str(j))
    processed_keys.append(j)
    for line in dict_out[j]:
        outfile1.write(str(line) + "\n")
        out_counter += 1
        

print("Processing 2nd list: " + str(output[1]))
for j in output[1]:
    print("Processing key and writing: " + str(j))
    processed_keys.append(j)
    for line in dict_out[j]:
        outfile2.write(str(line) + "\n")
        out_counter += 1






outfile1.close()
outfile2.close()


# ###################################################################
# Final Controls and reporting
# ###################################################################

print("Final control...")
print("Lines read: " + str(count))
print("Lines written: " + str(count))
print("Processed keys: " + str(processed_keys))
difference = int(count) - int(out_counter)
if difference != 0:
    print("PROBLEM")
    sys.exit(1)
