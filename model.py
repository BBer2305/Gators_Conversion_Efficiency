from __future__ import absolute_import, division, print_function, unicode_literals

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import random

import numpy as np
import pandas as pd

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

tf.keras.backend.set_floatx('float64')
print(tf.__version__)

file = pd.read_csv("Conversion_Results.csv")

train, val = train_test_split(file, test_size=0.02)

def df_to_dataset(dataframe, batch_size, shuffle=True):
  dataframe = dataframe.copy()
  labels = dataframe.pop('Result')
  #print(tf.shape(labels))
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

train_ds = df_to_dataset(train, batch_size=len(train))

val_ds = df_to_dataset(val, batch_size=len(val))

#for feature_batch, label_batch in train_ds.take(1):
  #print('Every feature:', list(feature_batch.keys()))
  #print('A batch of YTG:', feature_batch['YardsToGo'])
  #print('A batch of targets:', label_batch)
  #print(tf.shape(label_batch))

example_batch = next(iter(train_ds))[0]

def demo(feature_column):
  feature_layer = layers.DenseFeatures(feature_column)
  print(feature_layer(example_batch).numpy())

feature_columns = []
for header in ['Down', 'ScoreDifferential', 'CurrentQuarter', 'OffenseSPRank', 'RushRank', 'PassRank', 'OpponentPlay', 'YardsToGo', 'YardsToGoal', 'Location']:
  feature_columns.append(feature_column.numeric_column(header))

Down = feature_column.numeric_column("Down")
Quarter = feature_column.numeric_column("CurrentQuarter")
Score = feature_column.numeric_column("ScoreDifferential")
SP = feature_column.numeric_column("OffenseSPRank")
RushR = feature_column.numeric_column("RushRank")
PassR = feature_column.numeric_column("PassRank")
YTGo = feature_column.numeric_column("YardsToGo")
YTGoal = feature_column.numeric_column("YardsToGoal")
Play = feature_column.categorical_column_with_vocabulary_list('OpponentPlay', ['Pass', 'Run'])
Location = feature_column.categorical_column_with_vocabulary_list('Location', ['Home', 'Neutral', 'Away'])

Down_buckets = feature_column.bucketized_column(Down, boundaries=[4])
feature_columns.append(Down_buckets)
Quarter_buckets = feature_column.bucketized_column(Quarter, boundaries=[2, 3, 4])
feature_columns.append(Quarter_buckets)
Score_buckets = feature_column.bucketized_column(Score, boundaries=[-15, -8, -4, 4, 8, 15])
feature_columns.append(Score_buckets)
SP_buckets = feature_column.bucketized_column(SP, boundaries=[11, 26, 46, 71, 101])
feature_columns.append(SP_buckets)
RushR_buckets = feature_column.bucketized_column(RushR, boundaries=[11, 26, 46, 71, 101])
feature_columns.append(RushR_buckets)
PassR_buckets = feature_column.bucketized_column(PassR, boundaries=[11, 26, 46, 71, 101])
feature_columns.append(PassR_buckets)
YTGo_buckets = feature_column.bucketized_column(YTGo, boundaries=[2, 5, 8, 12])
feature_columns.append(YTGo_buckets)
YTGoal_buckets = feature_column.bucketized_column(YTGoal, boundaries=[6, 21, 36, 51, 66, 81, 95])
feature_columns.append(YTGoal_buckets)
Play_buckets = feature_column.indicator_column(Play)
feature_columns.append(Play_buckets)
Location_buckets = feature_column.indicator_column(Location)
feature_columns.append(Location_buckets)
QScore = feature_column.crossed_column([Quarter_buckets, Score_buckets], hash_bucket_size=28)
QScore = feature_column.indicator_column(QScore)
feature_columns.append(QScore)

feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

exit(0)

model = tf.keras.Sequential([
  feature_layer,
  layers.Dense(128, activation='relu'),
  layers.Dense(128, activation='relu'),
  layers.Dense(5, activation='softmax_cross_entropy_with_logits')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(train_ds,
          validation_data=val_ds,
          epochs=5)

#rest of code to come