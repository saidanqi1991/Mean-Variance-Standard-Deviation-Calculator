import numpy as np

def calculate(list):
    #Check the length of the list
    if len(list) == 9: 
        #reshape list to 3*3 mean
        arr = np.array(list).reshape(3,3)
        ##calculate mean
        axis0_mean = arr.mean(axis=0).tolist()
        axis1_mean = arr.mean(axis=1).tolist()
        flatten_mean = arr.mean()
        mean_list = [axis0_mean, axis1_mean, flatten_mean]
        #calculate variance
        axis0_variance = arr.var(axis=0).tolist()
        axis1_variance = arr.var(axis=1).tolist()
        flatten_variance = arr.var()
        var_list = [axis0_variance, axis1_variance, flatten_variance]
        #calculate standard deviation
        axis0_std = arr.std(axis=0).tolist()
        axis1_std = arr.std(axis=1).tolist()
        flatten_std = arr.std()
        std_list = [axis0_std, axis1_std, flatten_std]
        #calculate max
        axis0_max = arr.max(axis=0).tolist()
        axis1_max = arr.max(axis=1).tolist()
        flatten_max = arr.max()
        max_list = [axis0_max, axis1_max, flatten_max]
        #calculate min
        axis0_min = arr.min(axis=0).tolist()
        axis1_min = arr.min(axis=1).tolist()
        flatten_min = arr.min()
        min_list = [axis0_min, axis1_min, flatten_min]
        #calculate sum
        axis0_sum = arr.sum(axis=0).tolist()
        axis1_sum = arr.sum(axis=1).tolist()
        flatten_sum = arr.sum()
        sum_list = [axis0_sum, axis1_sum, flatten_sum]

        #Merge all list into a dictionary
        calculations = {
            'mean': mean_list,
            'variance': var_list,
            'standard deviation': std_list,
            'max': max_list,
            'min': min_list,
            'sum': sum_list
        }
        return calculations
    else: 
        raise ValueError("List must contain nine numbers.")