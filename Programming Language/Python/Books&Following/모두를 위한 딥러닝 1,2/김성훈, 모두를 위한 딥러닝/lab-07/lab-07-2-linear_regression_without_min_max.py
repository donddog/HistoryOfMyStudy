import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

xy = np.array([[828.659973, 833.450012, 908100, 828.349976, 831.659973],
               [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
               [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
               [816, 820.958984, 1008100, 815.48999, 819.23999],
               [819.359985, 823, 1188100, 818.469971, 818.97998],
               [819, 823, 1198100, 816, 820.450012],
               [811.700012, 815.25, 1098100, 809.780029, 813.669983],
               [809.51001, 816.659973, 1398100, 804.539978, 809.559998]])

x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4, 1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.matmul(X, W) + b
cost = tf.reduce_mean(tf.square(hypothesis - Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(7):
    cost_val, hy_val, _ = sess.run(
        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
    print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

'''result
0 Cost:  2455327000000.0 
Prediction:
 [[-1104436.2]
 [-2224343. ]
 [-1749606.6]
 [-1226179.4]
 [-1445287.1]
 [-1457459.5]
 [-1335740.5]
 [-1700924.5]]
1 Cost:  2.69762e+27 
Prediction:
 [[3.6637149e+13]
 [7.3754336e+13]
 [5.8019879e+13]
 [4.0671629e+13]
 [4.7933685e+13]
 [4.8337135e+13]
 [4.4302659e+13]
 [5.6406091e+13]]
2 Cost:  inf 
Prediction:
 [[-1.2143879e+21]
 [-2.4446870e+21]
 [-1.9231472e+21]
 [-1.3481161e+21]
 [-1.5888267e+21]
 [-1.6021996e+21]
 [-1.4684714e+21]
 [-1.8696560e+21]]
3 Cost:  inf 
Prediction:
 [[4.0252522e+28]
 [8.1032447e+28]
 [6.3745308e+28]
 [4.4685124e+28]
 [5.2663807e+28]
 [5.3107068e+28]
 [4.8674466e+28]
 [6.1972267e+28]]
4 Cost:  inf 
Prediction:
 [[-1.3342243e+36]
 [-2.6859301e+36]
 [-2.1129243e+36]
 [-1.4811488e+36]
 [-1.7456130e+36]
 [-1.7603054e+36]
 [-1.6133809e+36]
 [-2.0541546e+36]]
5 Cost:  inf 
Prediction:
 [[inf]
 [inf]
 [inf]
 [inf]
 [inf]
 [inf]
 [inf]
 [inf]]
6 Cost:  nan 
Prediction:
 [[nan]
 [nan]
 [nan]
 [nan]
 [nan]
 [nan]
 [nan]
 [nan]]
'''