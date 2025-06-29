def bmi(X):
    X = X.copy()
    X['bmi'] = X['peso'] / (X['altura'] ** 2)
    return X

def bmi_clasificador(X):
    X = X.copy()
    X['BMI Category'] = (X['bmi'] >= 25.0).astype(int)
    return X[['BMI Category']]

def Pulse_Pressure(X):
    X = X.copy()
    X['Pulse Pressure'] = X['systolic'] - X['diastolic']
    return X

def nurse_func(X):
    return (X == 'Sí').astype(int)

def gender_func(X):
    X = X.copy()
    X['Gender_code'] = (X == 'Femenino').astype(int)
    return X[['Gender_code']]