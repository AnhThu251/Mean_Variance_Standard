# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# The input of the function should be a list containing 9 digits. 
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

import numpy as np

def calculate(a):
  
    if len(a)==9:
        
        array = np.array(a).reshape(3, 3)
        calculations = {
            'mean': [np.mean(array, axis=0).tolist(), 
                     np.mean(array, axis=1).tolist(),
                     np.mean(array)],

            'variance': [np.var(array, axis=0).tolist(), 
                         np.var(array, axis=1).tolist(),
                         np.var(array.flatten())],
          
            'standard deviation': [np.std(array, axis=0).tolist(), 
                                   np.std(array, axis=1).tolist(),
                                   np.std(array.flatten())],
          
            'max': [np.max(array, axis=0).tolist(), 
                    np.max(array, axis=1).tolist(), 
                    np.max(array.flatten())],
          
            'min': [np.min(array, axis=0).tolist(), 
                    np.min(array, axis=1).tolist(), 
                    np.min(array.flatten())],
          
            'sum': [np.sum(array, axis=0).tolist(), 
                    np.sum(array, axis=1).tolist(), 
                    np.sum(array.flatten())]
            }
    else:
        raise ValueError('List must contain nine numbers.')
    return print(calculations)

calculate([0,1,2,3,4,5,6,7,8])