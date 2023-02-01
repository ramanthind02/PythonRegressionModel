import sklearn
import turtle 



#Greets the user and asks for the name of the csv file to be used 
print('Welcome, I am the Machine learning bot!')



file_input = input('Please enter the name of the csv file(make sure to write .csv at the end!)\n')


file = open(file_input)

i = 1

# a while loop that runs until the user provides a valid response for the question
#asks the user if a header is present in the file 
while i == 1:
    header_question = input('Does your file contain a header(yes/no)?\n').lower()

    if header_question == 'yes':
        screw_header = file.readline()
        i = 0
        

    elif header_question == 'no':
        i = 0

    else:
        print('Please provide a valid response')

# asks the user about which column the prediction is in and
#which range of the columns the inputs are in
#informs the user that only numbers can be present in each column 
print('Note the first column is assigned value 1 and the second column is assigned 2 etc...')
print('Note that all values from each column must be numerical only!')
prediction_column = int(input('Which column is the prediction in?\n'))

print('Which columns are the inputs in(Please input a range from column n to column m)\n')



n = int(input('type in n\n'))
m = int(input('type in m\n'))


#Since columns in python start at 0 and not 1, we subtract by 1
#Note: we dont change m as the index will stop before its value anyways
prediction_column = prediction_column-1
n = n-1




input_list = []
output_list = []

#splits the data in the file and creates 2 lists. One with the predictors as data called input list
#and another one with the predictions called output list
for data in file:
  datalist = data.split(',')
  input_list.append(datalist[n:m])
  output_list.append(datalist[prediction_column])



list_length = len(input_list[0])



float_input_values = []

float_output_list = []

#turns input values into floats 
for values in input_list:

    for i in values:
        float_input_values.append(float(i))


#turns output list in floats only and removes \n if present 
for values in output_list:

    values.strip('\n')

    float_output_list.append(float(values))






length_values = len(float_input_values)


float_input_list = []


#turns the list of values that were turned to numbers from strings and into floats
#back into a list of lists with length of the original list instead a long list of numbers 
for i in range (0,length_values,list_length):
    number = float_input_values[i:i+list_length]
    float_input_list.append(number)





total_length = len(float_output_list)


eighty_percent = int(total_length*0.8)


training_output_list = []
training_input_list = []
testing_input_list = []
testing_output_list = []

#Splits the input and output lists into 2 different lists. 80% of the list becomes training lists
#While the other 20% is for testing purposes 
for i in range (eighty_percent):
  training_input_list.append(float_input_list[i])
  

for i in range(eighty_percent,total_length):
  testing_input_list.append(float_input_list[i])


for i in range(eighty_percent,total_length):
  testing_output_list.append(float_output_list[i])



for i in range(eighty_percent):
 training_output_list.append(float_output_list[i])


#imports machine learning model and trains the machine learning algorithm
from sklearn.linear_model import LinearRegression 

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=training_input_list, y=training_output_list)

outcome = predictor.predict(X=testing_input_list)



percent_error = []


testing_range = total_length - eighty_percent
length_testing_output_list = len(testing_output_list)


#takes the range of the testing output list to determine the percent error by
#comparing the predicted values with the actual values that were predetermined 
for i in range (testing_range):
  
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


#initializes the turtle module 
levi = turtle.Turtle()
levi.speed(0)
levi.back(500)
levi.hideturtle()

scale_response = int(input('What scale do you want for the graph?(1 - smallest graph 10 - larger graph)\n'))

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
#with a scale value to make the bars larger or smaller 
def draw_bars(x,scale):

   for keys in x:


    levi.begin_fill()
    levi.color('red')
    
    levi.left(90)
    
    levi.forward(scale*error_dictionary[keys])


    
    levi.right(90)
    levi.forward(50)
    levi.right(90)
    levi.forward(scale*error_dictionary[keys])
    levi.left(90)

    levi.end_fill()
    #highlights each bar with black border
    levi.color('black')
    levi.back(50)
    levi.left(90)

    levi.forward(scale*error_dictionary[keys])
    levi.right(90)

    levi.forward(50)
    levi.right(90)
    levi.forward(scale*error_dictionary[keys])
    levi.left(90)
    
    
#writes out a string with a specific font size 
def write_something(string,font_size):
    style = ('Courier', font_size, 'bold')
    levi.write(string, font=style, align='center')


#This writes out potential levels on the y axis of the graph
def draw_vertical_scale (scale):
    for i in range (7):
        
        write_something(((i*50)/scale),7)
        levi.forward(50)


#draws graph wiht bars with the height of each correspanding value 
draw_rectangle(600,450)

levi.forward(20)

draw_bars(values,scale_response)

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
for i in range (7):
  
    levi.dot(5,'red')
    levi.forward(50)


levi.setpos(-510,0)


#Draws out the vertical scale 
draw_vertical_scale(scale_response)


levi.setpos(-220,-50)

write_something('Percent error', 12)

levi.setpos(-570,150)

write_something('Amount of\npredicted\nvalues out of\n' + str(length_testing_output_list), 12)

levi.setpos(-220,450)

write_something('Graph', 15)


















        

