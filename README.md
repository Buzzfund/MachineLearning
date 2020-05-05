# MachineLearning
Testing machine learning techniques on the market

## Languages

Python

## Requirements

```
    pip install -r requirements
```


## Random Forest

Meant to output chance of upward movement in 1 week. Will likely use regression decision tree as weak learner. Logistic activation function:

```math
    f(x) = 1/(1+e^-x)
```

### Data format

*x = Sector, Stock rank, RSI, Average volume-week, Average volume-month, Average price over 10 days, Average price over 5 days, (Open - Close)/Open, (High - Low)/Low, Standard deviation of returns over 5 days, Average returns over 5 days, Greeks, Volume/(Open Interest)*

*y = +1 for gain over next 3 days, otherwise -1*


## Logistic regression

Same purpose as random forest. Goal is to use L1 ridge regularization for feature selection. Regardless of hypothesis efficacy, we can try to rule out useless metrics in analyzing stock performance by virtue of ridge regularization.
