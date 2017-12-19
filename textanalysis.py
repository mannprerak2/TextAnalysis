# Know your file
from os.path import exists
'''constants'''
total_options = 8
my_file = file
operations = [
              "Word Count",
              "Line Count",
              "Byte size",
              "word list and occurence number",
              "sort alphabetical",
              "sort reverse alphabetical",
              "word search",
              "words list with given byte size",
              ]
option_selected = 0
'''constants end'''


'''defining functions'''
def word_count():
    print "Total words >>",
    print len(my_file.read().split())


def line_count():
    print "Total lines >>",
    counter = 0
    while my_file.readline():
        counter+=1
    print counter

def byte_size():
    my_file.seek(0,2) # 2nd arg 2 makes postion relative to EOF
    print "byte size is ",my_file.tell(),"bytes"#gives curent file position

def word_list_and_occurence():
    print "Generating word list with occurence"
    listw = my_file.read().split()
    listw.sort()
    old = listw[0]
    print listw[0],
    count = 1
    for a in listw:
        if a ==old :
            count+=1
            continue
        else:
            print "%s"%count
        old = a
        print "%s"%a,
        count = 1
    print count

def sort():
    print "sorting alphabetically"
    listw = my_file.read().split()
    listw.sort()
    old = ""
    for a in listw:
        if a ==old :
            continue
        old = a
        print "%s "%a

def rev_Sort():
    print "sorting reverse alphabetically"
    listw = my_file.read().split()
    listw.sort()
    listw = reversed(listw)
    old = ""
    for a in listw:
        if a ==old :
            continue
        old = a
        print "%s "%a

def word_search():
    print "Enter word to search > ",
    word_in = raw_input()
    listw = my_file.read().split()
    listw.sort()
    count = 0
    for a in listw:
        if(a==word_in):
            count+=1
    print "'",word_in,"'","occured",count,"times"

def word_with_byte_size():
    print "enter byte size / word length (integer only) > ",
    size = int(raw_input())
    listw = my_file.read().split()
    listw.sort()
    count=0
    for a in listw:
        if len(a)==size:
            count+=1
            print a,
        old = a
    print "\nfound",count,"words"

def checkFileExistsAndProceed(file_name):
    if(exists(file_name)):
        print "File exists"
    else:
        print "file not found"
        quit()

def options():
    print " Choose an option (ctrl+z to quit)"
    for i in range(total_options):
        print str(i+1)+". ",operations[i]
    return int(raw_input("Select one(integer only) > "))

def check_option(option_chosen):
    if(option_chosen in range(1,total_options+1)):
        print "task '%s' chosen"%option_chosen
    else:
        print "invalid option"
        quit()
def block_():
    print "="*30

'''defined functions end'''


'''function dictionary starts'''

function_dict = {"1":word_count,
                 "2":line_count,
                 "3":byte_size,
                 "4":word_list_and_occurence,
                 "5":sort,
                 "6":rev_Sort,
                 "7":word_search,
                 "8":word_with_byte_size}

'''function dictionary ends'''


    #asking user file name and checking if it exists then proceeding to choose an option
my_file_name = raw_input("Enter File Name > ")
checkFileExistsAndProceed(my_file_name)
while 1:
    #print option lists and input option from user
    option_selected = options()
    #check if option is valid, procced if yes or quit
    check_option(option_selected)
    #set file variable and open file
    my_file = open(my_file_name)
    #call function on file
    block_()
    function_dict[str(option_selected)]()
    #go back to start again
    block_()
