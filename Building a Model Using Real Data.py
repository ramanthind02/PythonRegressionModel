
import sklearn
import turtle 



#opens file and deletes header
file = open('SeoulBikeData.csv')

screw_header = file.readline()






input_list = []
output_list = []

#splits the data in the file and creates 2 lists. One with the predictors as data called input list
#and another one with the predictions called output list
for data in file:
  datalist = data.split(',')
  input_list.append(datalist[2:14])
  output_list.append(datalist[1])

#Turns strings in input list into numbers to be processed 
float_input_values = []
for values in input_list:
  
  if values[9] == 'Winter':
    values[9] = 0

  elif values[9] == "Spring":
    values[9] = 1

  elif values[9] == "Summer":
    values[9] = 2

  elif values[9] == "Autumn":
    values[9] = 3


  if values[10] == "No Holiday":
    values[10] = 0
  elif values[10] == "Holiday":
    values[10] = 1


  if values[11] == "Yes\n":
    values[11] = 1
  elif values[11] == "No\n":
    values[11] = 0
  
  #turns input values into floats 
  for i in values:
    float_input_values.append(float(i))
  
   
float_output_list = []

#turns output list in floats only 
for values in output_list:
    float_output_list.append(float(values))
    



float_input_list = []

#turns the list of values that were turned to numbers from strings and into floats
#back into a list of lists with length 12 instead a long list of numbers 
for i in range(0,105120,12):
  mini_list = float_input_values[i:i+12]
  float_input_list.append(mini_list)





training_output_list = []
training_input_list = []
testing_input_list = []
testing_output_list = []


#Splits the input and output lists into 2 different lists. 80% of the list becomes training lists
#While the other 20% is for testing purposes 
for i in range (7008):
  training_input_list.append(float_input_list[i])
  

for i in range(7008,8760):
  testing_input_list.append(float_input_list[i])


for i in range(7008,8760):
  testing_output_list.append(float_output_list[i])



for i in range(7008):
 training_output_list.append(float_output_list[i])



#imports machine learning model and trains the machine learning algorithm
from sklearn.linear_model import LinearRegression 

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=training_input_list, y=training_output_list)

outcome = predictor.predict(X=testing_input_list)



length_testing_output_list = len(testing_output_list)
percent_error = []



#takes the range of the testing output list to determine the percent error by
#comparing the predicted values with the actual values that were predetermined 
for i in range (length_testing_output_list):
  
  if testing_output_list[i] != 0:
    error_value = (abs(testing_output_list[i]-outcome[i]))/testing_output_list[i]
    error_value = error_value*100
    percent_error.append(error_value)

#Creates a dictionary to store the results 
error_dictionary = {'0%-10%': 0, '10%-20%':0, '20%-30%':0,'30%-40%':0, '40%-50%':0,'50%-60%':0, '60%-70%':0, '70%-80%':0,'80%-90%':0, '90%-100%':0, '>100%':0 }


#organizes and tallys up the percent error values into 11 different categories 
for values in percent_error:
  if values <= 10 and values >= 0:
    error_dictionary['0%-10%'] += 1 

  if values > 10 and values <= 20:
    error_dictionary['10%-20%'] += 1 

  if values > 20 and values <= 30:
    error_dictionary['20%-30%'] += 1 

  if values > 30 and values <= 40:
    error_dictionary['30%-40%'] += 1 

  if values > 40 and values <= 50:
    error_dictionary['40%-50%'] += 1 
  
  if values > 50 and values <= 60:
    error_dictionary['50%-60%'] += 1 
  
  if values > 60 and values <= 70:
    error_dictionary['60%-70%'] += 1 

  if values > 70 and values <= 80:
    error_dictionary['70%-80%'] += 1 
  
  if values > 80 and values <= 90:
    error_dictionary['80%-90%'] += 1 

  if values > 90 and values <= 100:
    error_dictionary['90%-100%'] += 1 

  if values > 100:
    error_dictionary['>100%'] += 1


#creates a list of the keys of the dictionary that can be used to draw a graph 
values = error_dictionary.keys()



levi = turtle.Turtle()

#initializes the turtle module 
levi.speed(0)
levi.back(500)
levi.hideturtle()


#draws rectangle with dimensions x and y 
def draw_rectangle(x,y):
    levi.forward(x)
    levi.left(90)
    levi.forward(y)
    levi.left(90)
    levi.forward(x)
    levi.left(90)
    levi.forward(y)
    levi.left(90)




#Draws bars with height of the values of each key from the dictionary 
def draw_bars(x):

   for keys in x:


    levi.begin_fill()
    levi.color('red')
    
    levi.left(90)

    levi.forward(error_dictionary[keys])
    

    
    levi.right(90)
    levi.forward(50)
    levi.right(90)
    levi.forward(error_dictionary[keys])
    levi.left(90)

    levi.end_fill()

    #highlights each bar with black border
    levi.color('black')
    levi.back(50)
    levi.left(90)

    levi.forward(error_dictionary[keys])
    levi.right(90)

    levi.forward(50)
    levi.right(90)
    levi.forward(error_dictionary[keys])
    levi.left(90)
 
    
#writes out a string with a specific font size 
def write_something(string,font_size):
    style = ('Courier', font_size, 'bold')
    levi.write(string, font=style, align='center')





#draws graph wiht bars with the height of each correspanding value 
draw_rectangle(600,450)
levi.forward(20)

draw_bars(values)

levi.penup()



levi.setpos(-450,-15)

#this writes out each key horizontally along the graph to correspond with each bar 
for keys in values:
  write_something(keys,7)
  levi.forward(50)

levi.setpos(-500,0)
levi.left(90)
levi.penup()

#This draws dots along the graph vertically 
for i in range (8):

    levi.dot(5,'red')
    levi.forward(50)


levi.setpos(-510,0)

#This writes out potential levels on the y axis of the graph 
for i in range (8):

    write_something(i*50,7)
    levi.forward(50)

#The code below writes several labels on the graph 
levi.setpos(-220,-50)

write_something('Percent error', 12)

levi.setpos(-570,150)

write_something('Amount of\npredicted\nvalues out of\n'+str(length_testing_output_list), 12)

levi.setpos(-220,450)

write_something('Graph', 15)
















