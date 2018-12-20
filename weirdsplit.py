# ##########################################################################
#
#   Author: P.Doulgeridis
#
# # ------------------------------------------------------------------------
#   Use as: python weirdsplit.py <file_in> <lines> <start> <end> <-v|-q>
#                                   
#          <file_in>: BN (Αρχεια ΑΤΜ)
#          <lines>  : ~42k
#          <start>  : integer
#          <end>    : integer
#
#
#
# # ------------------------------------------------------------------------ 
#
#   Location: C:\Users\p.doulgeridis\Desktop\weirdsplit\weirdsplit.py
#
# # ------------------------------------------------------------------------
#   Function: Reads the input file and limit and starts parsing, if the limit
#             gets exceeded mid grouping, then the entire group will be outputed
#             in the same file, then a new file will be initialized.
#
# # ------------------------------------------------------------------------
#
#   Notes: 
#           Encoding problem with input file: solved with errors=ignore. 
#           Check encoding python.
#           
#           Used to split BN files in banks <= 14 and banks > 14
#
# # ------------------------------------------------------------------------
#


# ##########################################################################
# Necessary Modules
import sys
import os
import time

try:
    import argparse
except:
    print("Failed to load argparse. Terminating")
    sys.exit(2)


# ##########################################################################
# Initiate Parser
# MODIFY: CENTRAL HELP TEXT
parser = argparse.ArgumentParser(
        prog="FileSplitter_Fast", 
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
parser.add_argument("lines", type=int, help="Provide the target lines")
parser.add_argument("start", type=int, help="Provide the beginning of substring - notepad++ column")
parser.add_argument("end", type=int, help="Provide the end of the substring - notepad++ column")


###### 
# Parse arguments
args = parser.parse_args()


######
# Assign arguments
# NUM_OF_LINES=args.lines
# filename = args.file



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


# ##################################################################
# PARSE ARGUMENTS AND FORMAT
try:
    file_in = args.file
    input_line_limit = args.lines
    start_in = args.start
    end_in = args.end
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
    
if not typecheck(input_line_limit, int):
    print("\n" + "Error: Provided number is not an integer. Terminating")
    sys.exit(9)


# #####################################################################
# Initialize Iteration Vars
    
group = ""
prev_group = ""
file_count = 0
dict_group = {}


# #####################################################################
# Script Start


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



with open(file_in, 'r') as f:

    fout = open(str(file_in)  + ".out" + ".0.txt", "w")
    line_status = 0
    file_count += 1
    counter = 0
    last_line = ''
    total_lines = 0
    file_line_counter = 0
    file_lines = []
    
    for i, lines in enumerate(f):
        
        print("#####")
        print("Line: " + str(i) + " with content: " + str(lines))
        
        last_line = lines
        
        # parse group
        #group = lines[2:6]
        group = lines[2:6]
        print("Comp: " + str(group) + " : " + str(prev_group))
        
        
        # check if group is different than previous
        if group != prev_group:
        
            print("new group: " + str(group))
            
            # check line status
            print("Checking line status: " + str(line_status) + " <-> " + str(input_line_limit))
            if line_status < input_line_limit:
                if prev_group in dict_group.keys():
                    print("Writing to output")
                    for j in dict_group[prev_group]:
                        line_status += 1
                        fout.write(j)
                        file_line_counter += 1
                    
                    
                    file_lines.append(file_line_counter)
                    file_line_counter = 0
            
            if line_status >= input_line_limit:
                print("Checking line status: " + str(line_status) + " <-> " + str(input_line_limit))
                print("Starting new file")
                #file_count += 1
                fout.close()
                fout = open(str(file_in) + ".out" + ".%d.txt"%(file_count), "w")
                file_count += 1
                line_status = 0
            
            # initialize new group
            dict_group = {}
            dict_group[group] = []
            
            # add line to group 
            dict_group[group].append(lines)
        
        else: 
        
            # same group
            dict_group[group].append(lines)
            
        prev_group = group
    

    for j in dict_group[group]:
        fout.write(j)
        file_line_counter += 1
    
    file_lines.append(file_line_counter)
    file_line_counter = 0

    
    #fout.write(lines)
    fout.close()
    
    
    
    # Reporting
    print("Reporting:")
    print(file_lines)
    print("Lines read: " + str(int(i + 1)))         # i starts at 0
    print("Total lines in all files: " + str(sum(file_lines)))
    

# ##########################################################################################
# Script end
script_end()
