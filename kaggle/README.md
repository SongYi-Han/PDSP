##  👾 Kaggle Competion

This competition is the a part of your course Prototyping Data Science Products. By joining this competition you ensure that your algorithm behind your web application is reliable and accurate.  
  
Refer to the following kaggle comepetition site
https://www.kaggle.com/competitions/prototyping-data-science-products-pdsp/leaderboard

### Challenge
In this competition, you will develop an algorithm (machine learning supervised/unsupervised, text matching etc..) to estimate the most accurate Co2 kg/emission per each recipe in the test set presented in this competition. You can train your model with the data provided in this competition and in the database. Your ranking in the competition will be based on your RMSE score. Your input will help us understanding how to best parse 'raw' ingredients into 'clean' and consequently be able to associate aCo2 score with all the ingredients in a recipe and ultimately with the recipe.

### Evaluation
The evaluation metric for this competition is RMSE score. The group with the best RMSE score wins the competition. Some useful reference: (https://en.wikipedia.org/wiki/Root-mean-square_deviation) and (https://machinelearningmastery.com/regression-metrics-for-machine-learning/).
  
The RMSE score is popular metric to estimate a model performance when the target variable is a continuous variable, by providing the differences between the values predicted by a model (or estimated by the accurate text matching in this case) and the real values (which we calculated for each recipe).
  
### Submission Format
The submission files should contain an "Id" column (corresponding to the unique key we gave to each recipe contained in the file "recipes_test.csv" and called "id") and the predicted Co2 score you estimated with your model for each recipe.

The file should contain a header and have the following format:

|  ID | Predicted  |
|-----|------------|
| 134 |    0.35    |
