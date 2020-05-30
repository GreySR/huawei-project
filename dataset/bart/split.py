import pandas as pd
from sklearn.model_selection import train_test_split
X = pd.read_csv('dataset.csv', sep=';')
train_source, test_source, train_target, test_target = train_test_split(X.text, X.title, 
																		test_size=0.2, random_state=42)
test_source, val_source, test_target, val_target = train_test_split(test_source, test_target, 
																		test_size=0.5, random_state=42)		
train_source.to_csv('train.source', header=False, index=False)
train_target.to_csv('train.target', header=False, index=False)
test_source.to_csv('test.source', header=False, index=False)
test_target.to_csv('test.target', header=False, index=False)
val_source.to_csv('val.source', header=False, index=False)
val_target.to_csv('val.target', header=False, index=False)																		