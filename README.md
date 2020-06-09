# MachineLearning
Testing machine learning techniques on the market

## Languages

Python

## Requirements

```
    pip install -r requirements
```


## Random Forest

Meant to output chance of upward movement in 1 week. Will likely use regression decision tree as weak learner.

Preliminary results: Random Forest is whack. It's terrible. It gives terrible results. It would rather try to classify everything as don't buy rather than get a single buy wrong. We need more time to tweak some hyperparameters perhaps.

## Adaboost

Cross validation preliminary: tree depth 2, ~1000 weak learners, balanced weight

Preliminary results: similar to random forest, boosting is not great. It's slightly better than random forest, but barely beats random guessing. Most importantly, these ensemble methods have high rates of false positives, our worst nightmare. https://stats.stackexchange.com/questions/163560/how-many-adaboost-iterations

TODO: try to customize the loss function to add importance to false positives (https://www.google.com/search?q=sklearn+change+loss+function&oq=sklearn+change+loss+fun&aqs=chrome.0.0j69i57j0l2.2437j0j4&sourceid=chrome&ie=UTF-8)

## Logistic Regression

Same purpose as random forest. Goal is to use L1 ridge regularization for feature selection. Regardless of hypothesis efficacy, we can try to rule out useless metrics in analyzing stock performance by virtue of ridge regularization.

Updated goal: toss what I wrote up there, go go log reg!

Notes: do not forget to normalize dataset

Preliminary results: bad as well haha. Will try to tune loss function. Will also try Bayesian regression.

### Data format

PLEASE UPDATE


