### ejercicios

home_data = 'datos de ejemplo'
feature_columns = ['Datos de ejemplo', 'Datos de ejemplo']

# features en el dataframe x:
X = home_data[feature_columns]

# El objetivo a calcular es y:
y = home_data.SalePrice

# Step 1: Split Your Data
# Use the train_test_split function to split up your data.
# Give it the argument random_state=1 so the check functions know what to expect when verifying your code.
# Recall, your features are loaded in the DataFrame X and your target is loaded in y.

# Import the train_test_split function and uncomment
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# fill in
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# You imported DecisionTreeRegressor in your last exercise
# and that code has been copied to the setup code above. So, no need to
# import it again

# Specify the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)


from sklearn.metrics import mean_absolute_error
val_mae = mean_absolute_error(val_y, val_predictions)

print(val_mae)
