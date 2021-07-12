#Main function start of loop and range
def function(num , rage):
    #loop start 
    for first in range (1 , num+1):
        #print the first table name output
        print("Table Number : " , first)
        #loop start of second of table print 
        for second in range(1 , rage+1):
            #print the second output  
            print(first , "X" , second , "=" , first*second)

#giving a value            
function(2 , 5)
