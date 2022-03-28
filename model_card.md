# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model used in this project is a Random Forest Model, using the [Scikit-lear implementation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

The *n_estimators* parameters is defined by a grid search procedure during training, executed for the values 100, 200 and 400, following the F1 score for best model selection.

A detailes explanation on how Random Forest works can be seen [here](https://towardsdatascience.com/understanding-random-forest-58381e0602d2).

## Intended Use

This model was developed for Udacity Machine LEarning DevOPs nanodegree and aims to predict if a person's salary is above or bellow 50k dollars, given its attributes, detailed on section #Training Data.

## Training Data

The training data is composed of 32561 rows and 14 attributes:

- age: continuous.
- workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- fnlwgt: continuous.
- education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
- education-num: continuous.
- marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
- sex: Female, Male.
- capital-gain: continuous.
- capital-loss: continuous.
- hours-per-week: continuous.
- native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

The class are <=50K for salaries equal o bellow 50K dollars and >50K for salaries above 50K dollars.

## Evaluation Data 

The dataset was split into two parts, 80% pro training and 20% for testing. The results on both sets are:

- Train Precision : 1.0 
- Train Recall: 1.0
- Train Fbeta: 1.0
<br><br>

- Test Precision : 0.7463
- Test Recall: 0.6346
- Test Fbeta: 0.6859


## Metrics

The metrics used are:

- Precision = $\frac{TP}{TP+FP}$
- Recall = $\frac{TP}{TP+FN}$
- F$\beta$ = $(1+\beta^2) \cdot \frac{precision \cdot recall}{(\beta^2 \cdot precision) + recall}$

## Ethical Considerations

The data does not contain any sensitive information that could be matched with an specifc person, as we don't have the security ID, phone number, address or any attribute that relates directly with anybody.

Soma correlations with maritial status, native country, race or sex may be found in the data.

## Caveats and Recommendations

For a fairer performance evaluation, the metrics should be computed on a separated test set. This was not done because the project instruction specified that we should have only the train data on our DVC control.
