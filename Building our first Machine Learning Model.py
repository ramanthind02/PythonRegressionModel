
import random
from random import randint 
import sklearn 

random_list = []

#creates a lis of 300 random values
for i in range (300):
  value = randint(0,1000)
  random_list.append(value)


input_list = []


#Creates a list of lists with each sublist of length 3 
for i in range(0,300,3):
  
  triplets = random_list[i:i+3]
  
  input_list.append(triplets)



output_list = []

#creates an output list from each sublist by multiplying each value by coefficent and adding them up
for values in input_list:
  
  output = values[0] + (2*values[1]) + (3*values[2])
  output_list.append(output)

#imports machine learning model and trains the machine learning algorithm
from sklearn.linear_model import LinearRegression 

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=input_list, y=output_list)

#creates a testing list to see if the ML algorithm can make an accurate prediction 
X_test = [[10,20,30]]

outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_

#prints out the ML predictions 
print('Prediction: ' + str(outcome))
print('Coefficients: ' +str(coefficients))
