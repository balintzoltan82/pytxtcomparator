from shutil import copyfile
from classes import Filecl
from comp import Compare
import filecmp
import os
import sys



#Requests first filename from the user:

while True:  
    file1=input('Give me the first file or press Q to quit: ')
    if (file1.upper()=="Q"):
        sys.exit()
    file2=input('Give me the second file or press Q to quit: ')

    #Exit point
    
    if (file2.upper()=="Q"):
        sys.exit()

    #Checking if the files exist
        
    exists1=os.path.isfile(file1)
    exists2=os.path.isfile(file2)
    if (exists1==False):
        print ("The first file does not exist")
    if (exists2==False):
        print ("The second file does not exist")
    elif (exists1 and exists2):
        break
    
#checks if the 2 files are identical. If they're, the programs ends.
    
result=filecmp.cmp(file1, file2, shallow=False)
print (file1,"versus",file2)

if (result):
    print ("The two files are the same")
    sys.exit()
    
    #If they're not identitcal, compares them by comparing the line lists:
    
else:
    inf1=Filecl(file1)
    inf2=Filecl(file2)
    file1rowlist=inf1.makelinelist()
    file2rowlist=inf2.makelinelist()
    if (len(file1rowlist) < len(file2rowlist)):
        Compare.comparator(file1rowlist, file2rowlist)
        diff=len(file2rowlist)-len(file1rowlist)
        print (file1, "contains", diff, "more rows than", file2)
    elif (len(file2rowlist) < len(file1rowlist)):
         Compare.comparator(file2rowlist,file1rowlist)
         diff=len(file1rowlist)-len(file2rowlist)
         print (file1, "contains", diff, "more rows than", file2)
    else:
         Compare.comparator(file1rowlist,file2rowlist)
         lenght=len(file1rowlist)
         print (file1, "and", file2, "contains", lenght, "rows.")

        
        
    
    
    








