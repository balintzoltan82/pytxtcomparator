class Compare:

    def comparator(list1,list2):
        
        diflines=[]
        
        for i in range(0,len(list1)):
            if (list1[i]!=list2[i]):
                diflines.append(i)

        print ("The two files differ in the following line(s): ")
        print (*diflines, sep=",")
        
                
                
                
         
                
    
