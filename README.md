# MachineLearning
Testing machine learning techniques on the market

*Language:* Python

## Random Forest

Meant to output chance of upward movement in 1 week. Will likely use regression decision tree as weak learner. Logistic activation function:

```math
    f(x) = 1/(1+e^-x)
```

### Data format

*x = Sector, EPS, P/E, Current Ratio, Zack Rank.*
*y = 1 week movement*

## Logistic regression

Same purpose as random forest. Goal is to use L1 regularization for feature selection.
