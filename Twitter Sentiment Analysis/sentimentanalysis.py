import tensorflow as tf
import numpy as np
from create_sent_features import create_features_lables

train_x, train_y, test_x, test_y = create_features_lables('pos.txt', 'neg.txt')

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 2
batch_size = 100

# height x width y
x = tf.placeholder('float', [None, len(train_x[0])])
y = tf.placeholder('float', )

def neural_net(data):
	hidden1 = {'weights':tf.Variable(tf.random_normal([len(train_x[0]), n_nodes_hl1])),
			   'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))}
	hidden2 = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
			   'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))}
	hidden3 = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
			   'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))}
	out = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
		   'biases':tf.Variable(tf.random_normal([n_classes]))}

	l1 = tf.add(tf.matmul(data, hidden1['weights']), hidden1['biases'])
	l1 = tf.nn.relu(l1) # activation function
	l2 = tf.add(tf.matmul(l1, hidden2['weights']), hidden2['biases'])
	l2 = tf.nn.relu(l2)
	l3 = tf.add(tf.matmul(l2, hidden3['weights']), hidden3['biases'])
	l3 = tf.nn.relu(l3)
	
	output = tf.add(tf.matmul(l3, out['weights']), out['biases'])
	
	return output

def train_nn(x):
	prediction = neural_net(x)
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
	optimiser = tf.train.AdamOptimizer().minimize(cost)

	n_epochs = 10
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		for epoch in range(n_epochs):
			epoch_loss = 0

			i = 0
			while i<len(train_x):
				start = i
				end = i+batch_size
				batch_x = np.array(train_x[start:end])
				batch_y = np.array(train_y[start:end])
				_, c = sess.run([optimiser, cost], feed_dict={x:batch_x, y:batch_y})
				epoch_loss += c
				i += batch_size
			print('Epoch',epoch,'completed ','loss: ',epoch_loss)
		correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))

		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		z = accuracy.eval({x:test_x, y:test_y})
	print("Accuracy:",z)


train_nn(x)
