/*
python table multiplication Write a function that takes 2 parameters (how many tables to be displayed and range of the table) 
Consider the following code and modify it to get the desired output: def table(no_table, range_table): #code here return Function 
call: table(2, 5) 
Expected Output 
        1 x 1= 1 
        1 x 2= 2 
        1 x 3= 3 
        1 x 4= 4 
        1 x 5= 5
        2 x 1= 2 
        2 x 2= 4 
        2 x 3= 6 
        2 x 4= 8 
        2 x 5= 10

*/

#Main function start of loop and range
def function(num , rage):
    for first in range (1 , num+1):
        print("Table Number : " , first)
        for second in range(1 , rage+1):
            
            #print the second output  
            print(first , "X" , second , "=" , first*second)

#giving a value            
function(2 , 5)
