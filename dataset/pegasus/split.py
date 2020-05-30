import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split


X = pd.read_csv('dataset.csv', sep=';')

def _bytes_feature(value):
  """����������� string / byte � bytes_list."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList �� ����� ������������� ������ �� EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
  
def serialize_example(inputs, targets):
  """
  ������� tf.Example-��������� ������� � ������ � ����.
  """
  # ������� ������� ����������� ���� ��������� � tf.Example-�����������
  # ���� ������.
  feature = {
      'inputs': _bytes_feature(inputs),
      'targets': _bytes_feature(targets),
  }
  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()
  
train, test = train_test_split(X, test_size=0.2, random_state=42)
test, val = train_test_split(test, test_size=0.5, random_state=42)

with tf.io.TFRecordWriter('train.tfrecord') as writer:
  for i, r in train.iterrows():
    example = serialize_example(bytes(r.text.strip(), encoding='utf-8'), bytes(r.title.strip(), encoding='utf-8'))
    writer.write(example)
with tf.io.TFRecordWriter('test.tfrecord') as writer:
  for i, r in test.iterrows():
    example = serialize_example(bytes(r.text.strip(), encoding='utf-8'), bytes(r.title.strip(), encoding='utf-8'))
    writer.write(example)
with tf.io.TFRecordWriter('val.tfrecord') as writer:
  for i, r in val.iterrows():
    example = serialize_example(bytes(r.text.strip(), encoding='utf-8'), bytes(r.title.strip(), encoding='utf-8'))
    writer.write(example)
