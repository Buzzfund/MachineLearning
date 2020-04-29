# MachineLearning
Testing machine learning techniques on the market

*Language:* Python

## Random Forest

Meant to output chance of upward movement in 1 week. Will likely use regression decision tree as weak learner. Logistic activation function:

```math
    f(x) = 1/(1+e^-x)
```

### Data format

*x = Sector, EPS, P/E, Current Ratio, Zack Rank, RSI, Volume.*
*y = 1 week movement*

In order for movement to be considered positive, it must surpass a threshold positive movement. i.e. +1.5%

## Logistic regression

Same purpose as random forest. Goal is to use L1--ridge--regularization for feature selection. Regardless of hypothesis efficacy, we can try to rule out useless metrics in analyzing stock performance by virtue of ridge regularization.
