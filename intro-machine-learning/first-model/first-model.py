import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)


### Ejercicio 1
# print the list of columns in the dataset to find the name of the prediction target

print(home_data.columns)

# Index(['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
#        'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig',
#        'LandSlope', 'Neighborhood', 'Condition1', 'Condition2', 'BldgType',
#        'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd',
#        'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
#        'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual',
#        'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
#        'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
#        'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF',
#        'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath',
#        'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
#        'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType',
#        'GarageYrBlt', 'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual',
#        'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF',
#        'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC',
#        'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold', 'SaleType',
#        'SaleCondition', 'SalePrice'],
#       dtype='object')

y = home_data.SalePrice


### Ejercicio 2

# Create the list of features below
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF',
                 '2ndFlrSF', 'FullBath', 'BedroomAbvGr','TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]


### Review data

# Review data
# print description or statistics from X
print(X.describe())

# print the top few lines
print(X.head())


### Ejercicio 3

from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

### Ejercicio 4

predictions = iowa_model.predict(X)
print(predictions)
# Salida: [208500. 181500. 223500. ... 266500. 142125. 147500.]

### Comparing with head()

predictions = iowa_model.predict(X.head())
# Salida: [208500. 181500. 223500. 140000. 250000.]

