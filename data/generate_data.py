import numpy as np

def get_data():
    data = {
        'A1': np.array([
            [0,0,1,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,1,0,0],
            [0,0,1,0,1,0,0],
            [0,1,1,1,1,1,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [1,1,1,0,1,1,1]
        ]),
        'A2': np.array([
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,1,0,0],
            [0,0,1,0,1,0,0],
            [0,1,0,0,0,1,0],
            [0,1,1,1,1,1,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,1,0]
        ]),
        'A3': np.array([
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,1,0,1,0,0],
            [0,0,1,0,1,0,0],
            [0,1,0,0,0,1,0],
            [0,1,1,1,1,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,0,0,0,1,1]
        ]),
        
        'B1': np.array([
            [1,1,1,1,1,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,1,1,1,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [1,1,1,1,1,1,0]
        ]),
        
        'B2': np.array([
            [1,1,1,1,1,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,0]
        ]),
        
        'B3': np.array([
            [1,1,1,1,1,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,1,1,1,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [1,1,1,1,1,1,0]
        ]),
        
        'C1': np.array([
            [0,0,1,1,1,1,1],
            [0,1,0,0,0,0,1],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [0,1,0,0,0,0,1],
            [0,0,1,1,1,1,0]
        ]),
        
        'C2': np.array([
            [0,0,1,1,1,0,0],
            [0,1,0,0,0,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,1],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0]
        ]),
        
        'C3': np.array([
            [0,0,1,1,1,0,1],
            [0,1,0,0,0,1,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,1],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0]
        ]),
        
        'D1': np.array([
            [1,1,1,1,1,0,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,1,0],
            [1,1,1,1,1,0,0]
        ]),
        
        'D2': np.array([
            [1,1,1,1,1,0,0],
            [1,0,0,0,0,1,0],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,0,1],
            [1,0,0,0,0,1,0],
            [1,1,1,1,1,0,0]
        ]),
        
        'D3': np.array([
            [1,1,1,1,1,0,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,1,0],
            [1,1,1,1,1,0,0]
        ]),
        
        'E1': np.array([
            [1,1,1,1,1,1,1],
            [0,1,0,0,0,0,1],
            [0,1,0,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,1,1,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1]
        ]),
        
        'E2': np.array([
            [1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,1,1,1,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,1,1,1,1,1,1]
        ]),
        
        'E3': np.array([
            [1,1,1,1,1,1,1],
            [0,1,0,0,0,0,1],
            [0,1,0,1,0,0,0],
            [0,1,1,1,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1]
        ]),
        
        'J1': np.array([
            [0,0,0,1,1,1,1],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0]
        ]),
        
        'J2': np.array([
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0]
        ]),
        
        'J3': np.array([
            [0,0,0,0,1,1,1],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0]
        ]), 
        
        'K1': np.array([
            [1,1,1,0,0,1,1],
            [0,1,0,0,1,0,0],
            [0,1,0,1,0,0,0],
            [0,1,1,0,0,0,0],
            [0,1,1,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,0,1,0,0],
            [0,1,0,0,0,1,0],
            [1,1,1,0,0,1,1]
        ]),
        
        'K2': np.array([
            [1,0,0,0,0,1,0],
            [1,0,0,0,1,0,0],
            [1,0,0,1,0,0,0],
            [1,0,1,0,0,0,0],
            [1,1,0,0,0,0,0],
            [1,0,1,0,0,0,0],
            [1,0,0,1,0,0,0],
            [1,0,0,0,1,0,0],
            [1,0,0,0,0,1,0]
        ]),
        
        'K3': np.array([
            [1,1,1,0,0,1,1],
            [0,1,0,0,0,1,0],
            [0,1,0,0,1,0,0],
            [0,1,0,1,0,0,0],
            [0,1,1,0,0,0,0],
            [0,1,0,1,0,0,0],
            [0,1,0,0,1,0,0],
            [0,1,0,0,0,1,0],
            [1,1,1,0,0,1,1]
        ]),
    }
    
    return data

