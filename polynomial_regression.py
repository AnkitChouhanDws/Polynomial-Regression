################################################### Polynomial regression #################################################
# In this example we will try to find the expected salaries of new applicants bases on their experience
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Path To Dataset')

# Splitting into dependent and independent variable
X= dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values


# Since we have very less data in dataset. Therefore, we will take our whole dataset as training data

# Fitting linear Regression to the dataset(For Comparison)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
# Here we will import a new class that will give us tools to include some polynomial terms into the linear regression equation.
from sklearn.preprocessing import PolynomialFeatures
# Create object of this class
# This will convert our matrix of features(X) to new matrix containing x1^1, x1^2, x1^3.......X1^n, upto whatever we want
poly_reg = PolynomialFeatures(degree = 5)
# It will automatically include a column of y-intercept into our X_poly matrix
X_poly = poly_reg.fit_transform(X)

# To build our model as multiple linear regression model
lin_reg2= LinearRegression()
lin_reg2.fit(X_poly, y)


# Visualizing the Linear Regression Results

plt.scatter(X,y, color='red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualizing the Polynomial Regression Results

X_grid= np.arange(min(X), max(X),0.1)
X_grid= X_grid.reshape(len(X_grid),1)
plt.scatter(X,y, color='red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# Predicting a new result with Linear Regression
level= float(input('Enter your Experience level: '))
print(lin_reg.predict(level))


# Predicting a new result with Polynomial Regression

level= float(input('Enter your Experience level: '))
print(lin_reg2.predict(poly_reg.fit_transform(level)))


