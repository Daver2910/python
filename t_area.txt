#Script to calculate the area of the triangle with a base of 12inches & height of 16inches.
#I added units of measurement in the print(i hope this is allowed in the task).


#this is the length of the base in inches
base = 12 
#this is the height of the triangle in inches
height = 16 
#the result of calculation is assigned to "area"
area = (0.5*base)*height

#applied 'int()' to get whole number,
#then applied str() to allow the 'sq inches' text to be added(int & str cannot be printed together, only str+str or int+int)
print (str(int(area))+' sq inches')
