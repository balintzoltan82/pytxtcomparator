class Filecl:
    'A file to work with'
    
    
    def __init__(self, filename):
        self.filename=filename

    #This method creates a list with the lines of the text file:

    def makelinelist(self):
        line_list=[]
        f=open(self.filename,'r')
        for line in f:
            line_list.append(line.strip()) 
        f.close()
        return line_list
    

            
   
    
    

    
            
                
        
            
            

        
            
            
            
	
                
