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

The performance are measured on slices of data, considering categorical features, and the following results were found:

workclass
- Precision on slice workclass: 1.0000
- Recall on slice workclass: 1.0000
- $F\beta$ on slice workclass: 1.0000

education
- Precision on slice education: 1.0000
- Recall on slice education: 1.0000
- $F\beta$ on slice education: 1.0000

marital-status
- Precision on slice marital-status: 1.0000
- Recall on slice marital-status: 0.0000
- $F\beta$ on slice marital-status: 0.0000

occupation
- Precision on slice occupation: 1.0000
- Recall on slice occupation: 1.0000
- $F\beta$ on slice occupation: 1.0000

relationship
- Precision on slice relationship: 1.0000
- Recall on slice relationship: 0.3750
- $F\beta$ on slice relationship: 0.5455

race
- Precision on slice race: 0.7143
- Recall on slice race: 0.5000
- $F\beta$ on slice race: 0.5882

sex
- Precision on slice sex: 0.7447
- Recall on slice sex: 0.6584
- $F\beta$ on slice sex: 0.6989

native-country
- Precision on slice native-country: 1.0000
- Recall on slice native-country: 1.0000
- $F\beta$ on slice native-country: 1.0000


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
