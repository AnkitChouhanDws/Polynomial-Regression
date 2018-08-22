# What is Regression?
***

- Regression takes a group of random variables, thought to be predicting Y, and tries to find a mathematical relationship between them. 
- This relationship is typically in the form of a straight line (linear regression) or may be some curve(in case of polynomial regression) that best approximates all the individual data points.

Read more: Regression https://www.investopedia.com/terms/r/regression.asp#ixzz5OA1H851T 
Follow us: Investopedia on Facebook

# What is Polynomial Regression?
***
Polynomial regression is a statistical method that allows us to summarize and study relationships between two continuous (quantitative) variables:

One variable, denoted x, is regarded as the predictor, explanatory, or independent variable.
The other variable, denoted y, is regarded as the response, outcome, or dependent variable.

#### In this example, we will only deal with polynomial relations with single variable

## Polynomial models in one variable
The k<sub>th</sub> order polynomial model in one variable is given by
<i> 
   y= b<sub>0</sub> + b<sub>1</sub>x + b<sub>2</sub>x<sup>2</sup> + b<sub>3</sub>x<sup>3</sup> + ...
</i>
### Order of Polynomial
- Example of order 2 polynomial:
  <i> 
   y= b<sub>0</sub> + b<sub>1</sub>x + b<sub>2</sub>x<sup>2</sup> 
</i>

is a polynomial regression model in one variable and is called as second order model or quadratic
model. The coefficients b<sub>1</sub> AND b<sub>2</sub> are called the linear effect parameter and quadratic effect
parameter respectively.

Now, let's directly dive into our code and see how to implement this in python.<br> Comments written in code will help you to understand polynomial regression in a better way.

#### To know more about Polynomial regression, follow this link: http://home.iitk.ac.in/~shalab/regression/Chapter12-Regression-PolynomialRegression.pdf<br>
