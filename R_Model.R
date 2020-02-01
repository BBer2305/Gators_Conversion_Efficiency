#read csv file and adjust columns
file <- read.csv("-")
file$YardsGained <- NULL
names(file)[1] <- "Down"
file$Down <- as.factor(file$Down)
file$CurrentQuarter <- as.factor(file$CurrentQuarter)

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
file$RushEfficiency <- NULL
file$PassEfficiency <- NULL
file$OffenseSP <- NULL
ggcorr(file, label=TRUE, nbreaks=5)

#create random forest and make predictions
ResultTreeB = randomForest(Result~., data=file)
PredDRF = predict(ResultTreeB, type="prob")
importance(ResultTreeB, type=2)

#remove a few more predictors
file$RushGrade <- NULL
file$PassGrade <- NULL
ggcorr(file, label=TRUE, nbreaks=5)

#create random forest and make predictions
ResultTreeC = randomForest(Result~., data=file)
PredDRF = predict(ResultTreeC, type="prob")
importance(ResultTreeC, type=2)
