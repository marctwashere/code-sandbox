import os
import shutil

# USER PARAMETERS edit these MUST HAVE '/' not '\'
top_level = 'C:/Users/matv2/OneDrive/Desktop/test_top_level' # the path to the top-level directory for searching
list_loc = 'C:/Users/matv2/OneDrive/Desktop/find_these.txt' # path to text file containing search terms
output_dir = 'C:/Users/matv2/OneDrive/Desktop/test_output' # directory where you want files saved
# END USER PARAMETERS

# helper vars for logging
missed = []

# create targets directory
if os.path.exists('{}/targets'.format(output_dir)):
    shutil.rmtree('{}/targets'.format(output_dir))
    os.mkdir('{}/targets'.format(output_dir))

# get the list of folders that need to be found
with open(list_loc, 'r') as file:
    to_find = file.readlines()

# clean up the newline characters
to_find = [x.replace('\n','') for x in to_find]

# loop over every taget folder
for find_me in to_find:
    print('Looking for "{}"'.format(find_me))

    # reset flag
    found = False

    # reset directory to root folder
    os.chdir(top_level)

    # loop over every sub-folder (one level deep)
    for sub in os.listdir():

        # skip files
        if not os.path.isdir(sub) or sub == 'targets': continue

        # enter the sub-dir
        os.chdir(sub)
        print('Looking in {}'.format(sub))

        # look for the target folder
        if find_me in os.listdir():
            print('FOUND IT')

            # copy the folder to "targets"
            shutil.copytree(find_me, '{}/targets/{}'.format(output_dir, find_me))

            # flag for logging
            found = True

        # step out of the sub-folder
        os.chdir('..')
        
    # log misses
    if not found: missed.append(find_me)

# save missed to file
with open('{}/missed.txt'.format(output_dir), 'w') as file:
    for miss in missed:
        file.write(miss)
        file.write('\n') 

# give stats to user
print('Found {} targets'.format(len(to_find) - len(missed)))
print('Missed {} targets'.format(len(missed)))
print('A list of missed targets can be found at missed.txt')
input('Press enter to close...')