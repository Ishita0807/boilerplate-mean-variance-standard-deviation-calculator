import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    flat_list = np.array(list)
    mat = flat_list.reshape(3, 3)
    calculations = dict()
    calculations['mean'] = [np.mean(mat, axis=0).tolist(), np.mean(mat, axis=1).tolist(), np.mean(flat_list)]
    calculations['variance'] = [np.var(mat, axis=0).tolist(), np.var(mat, axis=1).tolist(), np.var(flat_list)]
    calculations['standard deviation'] = [np.std(mat, axis=0).tolist(), np.std(mat, axis=1).tolist(), np.std(flat_list)]
    calculations['max'] = [np.max(mat, axis=0).tolist(), np.max(mat, axis=1).tolist(), np.max(flat_list)]
    calculations['min'] = [np.min(mat, axis=0).tolist(), np.min(mat, axis=1).tolist(), np.min(flat_list)]
    calculations['sum'] = [np.sum(mat, axis=0).tolist(), np.sum(mat, axis=1).tolist(), np.sum(flat_list)]






    return calculations