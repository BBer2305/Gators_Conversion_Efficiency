#read csv file and adjust columns
file <- read.csv("C:/Users/Ben/Documents/Projects/Gators_Conversion_Efficiency/Conversion_Results.csv")
file$Yards.Gained <- NULL
names(file)[1] <- "Down"
file$Down <- as.factor(file$Down)
file$Current.Quarter <- as.factor(file$Current.Quarter)

#create correlation chart
source("https://raw.githubusercontent.com/briatte/ggcorr/master/ggcorr.R")
ggcorr(file, label=TRUE, nbreaks=5)

#import random forest library
library("randomForest")

#create random forest and make predictions
ResultTree = randomForest(Result~., data=file)
PredDRF = predict(ResultTree, type="prob")
importance(ResultTree, type=2)

#remove highly correlated/less significant predictors and try again
file$Rush.Efficiency <- NULL
file$Pass.Efficiency <- NULL
file$Offense.SP. <- NULL
ggcorr(file, label=TRUE, nbreaks=5)

#create random forest and make predictions
ResultTreeB = randomForest(Result~., data=file)
PredDRF = predict(ResultTreeB, type="prob")
importance(ResultTreeB, type=2)

#remove a few more predictors
file$Rush.Grade <- NULL
file$Pass.Grade <- NULL
ggcorr(file, label=TRUE, nbreaks=5)

#create random forest and make predictions
ResultTreeC = randomForest(Result~., data=file)
PredDRF = predict(ResultTreeC, type="prob")
importance(ResultTreeC, type=2)
