'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
import sklearn.linear_model as skmod
import sklearn.model_selection as sksel
import sklearn.preprocessing as skprepro


input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]
input3 = [int(i) for i in input3.split(',')]


arr1 = np.array(input1).reshape(-1, 1)
arr2= np.array(input2).reshape(-1, 1)
arr3 = np.array(input3).reshape(-1, 1)

data_x = np.hstack([arr1, arr2, arr3])
# print(data_x)


#use this printing (where "data_x" is your features scaled and standardized)

scaler = skprepro.StandardScaler()
scaler_f = scaler.fit(data_x)
data_x_stan = scaler_f.transform(data_x)

data_x_train, data_x_test = sksel.train_test_split(data_x_stan, train_size = 0.75, shuffle = False)

# plt.scatter(data_x_train, data_y_train)
# plt.scatter(data_x_test, data_y_test)


#use this printing (where "data_x" is your features scaled and standardized)
print("{}".format(np.round(data_x_train,2)))