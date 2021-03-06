import sys
sys.path.append('..')
from tfomics import utils, init
from tfomics.build_network import *
import tensorflow as tf


def model(input_shape, num_labels=None):
  # design a neural network model
  
  # placeholders
  inputs = utils.placeholder(shape=input_shape, name='input')
  is_training = tf.placeholder(tf.bool, name='is_training')
  keep_prob = tf.placeholder(tf.float32, name='keep_prob')
  targets = utils.placeholder(shape=(None,num_labels), name='output')
  
  # placeholder dictionary
  placeholders = {'inputs': inputs, 
                  'targets': targets, 
                  'keep_prob': keep_prob, 
                  'is_training': is_training}

  # create model
  layer1 = {'layer': 'input',
            'inputs': inputs,
            'name': 'input'
            }
  layer2 = {'layer': 'conv2d', 
            'num_filters': 18,
            'filter_size': (2, 5),
            'b': init.Constant(0.1),
            'activation': 'tanh',
            'name': 'conv1'
            }
  layer3 = {'layer': 'conv2d', 
            'num_filters': 40,
            'filter_size': (2, 5),
            'b': init.Constant(0.1),
            'activation': 'tanh',
            'pool_size': (1,10),
            'name': 'conv2'
            }
  layer4 = {'layer': 'conv2d', 
            'num_filters': 15,
            'filter_size': (1,1),
            'b': init.Constant(0.1),
            'activation': 'tanh',
            'name': 'conv3'
            }
  layer5 = {'layer': 'dense', 
            'num_units': 100,
            'activation': 'relu',
            'name': 'dense1'
            }
  layer6 = {'layer': 'dense', 
            'num_units': num_labels,
            'activation': 'softmax',
            'name': 'dense2'
            }

  #from tfomics import build_network
  model_layers = [layer1, layer2, layer3, layer4, layer5, layer6]
  net = build_network(model_layers)

  # optimization parameters
  optimization = {"objective": "categorical",
                  "optimizer": "adam",
                  "learning_rate": 0.001,      
                  "l2": 1e-6,
                  # "l1": 0, 
                  }

  return net, placeholders, optimization

