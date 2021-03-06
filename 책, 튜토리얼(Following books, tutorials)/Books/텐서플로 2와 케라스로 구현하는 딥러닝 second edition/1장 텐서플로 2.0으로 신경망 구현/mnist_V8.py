import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.optimizers import SGD

EPOCHS = 20
BATCH_SIZE = 256
VERBOSE = 1
NB_CLASSES = 10
N_HIDDEN = 128
VALIDATION_SPLIT=0.2
DROPOUT = 0.3
OPTMIZER = SGD(lr=0.001)

mnist = keras.datasets.mnist

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

RESHAPED = 784

X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train, X_test = X_train / 255.0, X_test / 255.0

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
'''
60000 train samples
10000 test samples
'''

Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test = tf.keras.utils.to_categorical(Y_test, NB_CLASSES)

model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(N_HIDDEN, input_shape=(RESHAPED,), name='dense_layer', activation='relu'))
model.add(keras.layers.Dropout(DROPOUT))
model.add(keras.layers.Dense(N_HIDDEN, name='dense_layer_2', activation='relu'))
model.add(keras.layers.Dropout(DROPOUT))
model.add(keras.layers.Dense(NB_CLASSES, name='dense_layer_3', activation='softmax'))

model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_layer (Dense)          (None, 128)               100480    
_________________________________________________________________
dropout (Dropout)            (None, 128)               0         
_________________________________________________________________
dense_layer_2 (Dense)        (None, 128)               16512     
_________________________________________________________________
dropout_1 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_layer_3 (Dense)        (None, 10)                1290      
=================================================================
Total params: 118,282
Trainable params: 118,282
Non-trainable params: 0
_________________________________________________________________
Train on 48000 samples, validate on 12000 samples
'''

model.compile(optimizer=OPTMIZER, loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=VERBOSE,
		  validation_split=VALIDATION_SPLIT)

test_loss, test_acc = model.evaluate(X_test, Y_test)

print('Test accuracy:', test_acc)
'''Test accuracy: 0.8082'''

predictions = model.predict(X_test)
'''
Epoch 1/20

  256/48000 [..............................] - ETA: 33s - loss: 2.3806 - accuracy: 0.0664
 6400/48000 [===>..........................] - ETA: 1s - loss: 2.3777 - accuracy: 0.0948 
12800/48000 [=======>......................] - ETA: 0s - loss: 2.3677 - accuracy: 0.0978
18944/48000 [==========>...................] - ETA: 0s - loss: 2.3570 - accuracy: 0.1028
25344/48000 [==============>...............] - ETA: 0s - loss: 2.3508 - accuracy: 0.1068
31488/48000 [==================>...........] - ETA: 0s - loss: 2.3458 - accuracy: 0.1099
37632/48000 [======================>.......] - ETA: 0s - loss: 2.3414 - accuracy: 0.1105
43776/48000 [==========================>...] - ETA: 0s - loss: 2.3356 - accuracy: 0.1136
48000/48000 [==============================] - 1s 14us/sample - loss: 2.3327 - accuracy: 0.1151 - val_loss: 2.2501 - val_accuracy: 0.1887
Epoch 2/20

  256/48000 [..............................] - ETA: 0s - loss: 2.3079 - accuracy: 0.1367
 6656/48000 [===>..........................] - ETA: 0s - loss: 2.2835 - accuracy: 0.1400
12800/48000 [=======>......................] - ETA: 0s - loss: 2.2788 - accuracy: 0.1405
18944/48000 [==========>...................] - ETA: 0s - loss: 2.2753 - accuracy: 0.1429
25344/48000 [==============>...............] - ETA: 0s - loss: 2.2708 - accuracy: 0.1469
31488/48000 [==================>...........] - ETA: 0s - loss: 2.2664 - accuracy: 0.1506
37888/48000 [======================>.......] - ETA: 0s - loss: 2.2623 - accuracy: 0.1535
44032/48000 [==========================>...] - ETA: 0s - loss: 2.2583 - accuracy: 0.1565
48000/48000 [==============================] - 0s 9us/sample - loss: 2.2558 - accuracy: 0.1592 - val_loss: 2.1757 - val_accuracy: 0.3184
Epoch 3/20

  256/48000 [..............................] - ETA: 0s - loss: 2.2194 - accuracy: 0.1758
 6400/48000 [===>..........................] - ETA: 0s - loss: 2.2096 - accuracy: 0.1964
12800/48000 [=======>......................] - ETA: 0s - loss: 2.2094 - accuracy: 0.1972
18944/48000 [==========>...................] - ETA: 0s - loss: 2.2032 - accuracy: 0.2013
25088/48000 [==============>...............] - ETA: 0s - loss: 2.1998 - accuracy: 0.2039
31232/48000 [==================>...........] - ETA: 0s - loss: 2.1974 - accuracy: 0.2069
37376/48000 [======================>.......] - ETA: 0s - loss: 2.1943 - accuracy: 0.2097
43520/48000 [==========================>...] - ETA: 0s - loss: 2.1913 - accuracy: 0.2119
48000/48000 [==============================] - 0s 9us/sample - loss: 2.1880 - accuracy: 0.2141 - val_loss: 2.1057 - val_accuracy: 0.4158
Epoch 4/20

  256/48000 [..............................] - ETA: 0s - loss: 2.1612 - accuracy: 0.2383
 6400/48000 [===>..........................] - ETA: 0s - loss: 2.1543 - accuracy: 0.2484
12288/48000 [======>.......................] - ETA: 0s - loss: 2.1508 - accuracy: 0.2431
18176/48000 [==========>...................] - ETA: 0s - loss: 2.1475 - accuracy: 0.2460
24064/48000 [==============>...............] - ETA: 0s - loss: 2.1447 - accuracy: 0.2502
29952/48000 [=================>............] - ETA: 0s - loss: 2.1404 - accuracy: 0.2553
35840/48000 [=====================>........] - ETA: 0s - loss: 2.1372 - accuracy: 0.2580
41984/48000 [=========================>....] - ETA: 0s - loss: 2.1334 - accuracy: 0.2613
48000/48000 [==============================] - 0s 10us/sample - loss: 2.1293 - accuracy: 0.2644 - val_loss: 2.0350 - val_accuracy: 0.4918
Epoch 5/20

  256/48000 [..............................] - ETA: 0s - loss: 2.1002 - accuracy: 0.2930
 6400/48000 [===>..........................] - ETA: 0s - loss: 2.0933 - accuracy: 0.2911
12800/48000 [=======>......................] - ETA: 0s - loss: 2.0890 - accuracy: 0.3011
18944/48000 [==========>...................] - ETA: 0s - loss: 2.0865 - accuracy: 0.3014
25344/48000 [==============>...............] - ETA: 0s - loss: 2.0811 - accuracy: 0.3061
31744/48000 [==================>...........] - ETA: 0s - loss: 2.0756 - accuracy: 0.3112
37888/48000 [======================>.......] - ETA: 0s - loss: 2.0715 - accuracy: 0.3139
44288/48000 [==========================>...] - ETA: 0s - loss: 2.0658 - accuracy: 0.3186
48000/48000 [==============================] - 0s 9us/sample - loss: 2.0637 - accuracy: 0.3196 - val_loss: 1.9607 - val_accuracy: 0.5558
Epoch 6/20

  256/48000 [..............................] - ETA: 0s - loss: 2.0286 - accuracy: 0.3359
 6400/48000 [===>..........................] - ETA: 0s - loss: 2.0265 - accuracy: 0.3384
12544/48000 [======>.......................] - ETA: 0s - loss: 2.0229 - accuracy: 0.3441
18688/48000 [==========>...................] - ETA: 0s - loss: 2.0185 - accuracy: 0.3471
24832/48000 [==============>...............] - ETA: 0s - loss: 2.0139 - accuracy: 0.3492
30720/48000 [==================>...........] - ETA: 0s - loss: 2.0091 - accuracy: 0.3524
36864/48000 [======================>.......] - ETA: 0s - loss: 2.0039 - accuracy: 0.3574
43008/48000 [=========================>....] - ETA: 0s - loss: 2.0001 - accuracy: 0.3601
48000/48000 [==============================] - 0s 9us/sample - loss: 1.9975 - accuracy: 0.3619 - val_loss: 1.8824 - val_accuracy: 0.6051
Epoch 7/20

  256/48000 [..............................] - ETA: 0s - loss: 1.9818 - accuracy: 0.4023
 6144/48000 [==>...........................] - ETA: 0s - loss: 1.9657 - accuracy: 0.3813
12032/48000 [======>.......................] - ETA: 0s - loss: 1.9609 - accuracy: 0.3868
18176/48000 [==========>...................] - ETA: 0s - loss: 1.9556 - accuracy: 0.3896
24320/48000 [==============>...............] - ETA: 0s - loss: 1.9481 - accuracy: 0.3947
30464/48000 [==================>...........] - ETA: 0s - loss: 1.9427 - accuracy: 0.3978
36608/48000 [=====================>........] - ETA: 0s - loss: 1.9396 - accuracy: 0.3979
42752/48000 [=========================>....] - ETA: 0s - loss: 1.9352 - accuracy: 0.4006
48000/48000 [==============================] - 0s 9us/sample - loss: 1.9307 - accuracy: 0.4036 - val_loss: 1.8000 - val_accuracy: 0.6392
Epoch 8/20

  256/48000 [..............................] - ETA: 0s - loss: 1.9271 - accuracy: 0.3789
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.8903 - accuracy: 0.4250
12800/48000 [=======>......................] - ETA: 0s - loss: 1.8961 - accuracy: 0.4190
19200/48000 [===========>..................] - ETA: 0s - loss: 1.8921 - accuracy: 0.4212
25344/48000 [==============>...............] - ETA: 0s - loss: 1.8845 - accuracy: 0.4262
31744/48000 [==================>...........] - ETA: 0s - loss: 1.8782 - accuracy: 0.4301
37888/48000 [======================>.......] - ETA: 0s - loss: 1.8717 - accuracy: 0.4325
44032/48000 [==========================>...] - ETA: 0s - loss: 1.8671 - accuracy: 0.4352
48000/48000 [==============================] - 0s 9us/sample - loss: 1.8638 - accuracy: 0.4365 - val_loss: 1.7150 - val_accuracy: 0.6652
Epoch 9/20

  256/48000 [..............................] - ETA: 0s - loss: 1.8563 - accuracy: 0.4102
 6656/48000 [===>..........................] - ETA: 0s - loss: 1.8092 - accuracy: 0.4573
12800/48000 [=======>......................] - ETA: 0s - loss: 1.8093 - accuracy: 0.4584
19200/48000 [===========>..................] - ETA: 0s - loss: 1.8108 - accuracy: 0.4597
25600/48000 [===============>..............] - ETA: 0s - loss: 1.8059 - accuracy: 0.4626
31744/48000 [==================>...........] - ETA: 0s - loss: 1.8022 - accuracy: 0.4622
37888/48000 [======================>.......] - ETA: 0s - loss: 1.7994 - accuracy: 0.4643
44288/48000 [==========================>...] - ETA: 0s - loss: 1.7943 - accuracy: 0.4656
48000/48000 [==============================] - 0s 9us/sample - loss: 1.7909 - accuracy: 0.4674 - val_loss: 1.6287 - val_accuracy: 0.6866
Epoch 10/20

  256/48000 [..............................] - ETA: 0s - loss: 1.7658 - accuracy: 0.5000
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.7570 - accuracy: 0.4814
12800/48000 [=======>......................] - ETA: 0s - loss: 1.7420 - accuracy: 0.4907
19200/48000 [===========>..................] - ETA: 0s - loss: 1.7395 - accuracy: 0.4915
25600/48000 [===============>..............] - ETA: 0s - loss: 1.7355 - accuracy: 0.4911
32000/48000 [===================>..........] - ETA: 0s - loss: 1.7329 - accuracy: 0.4920
38400/48000 [=======================>......] - ETA: 0s - loss: 1.7276 - accuracy: 0.4947
44544/48000 [==========================>...] - ETA: 0s - loss: 1.7238 - accuracy: 0.4950
48000/48000 [==============================] - 0s 9us/sample - loss: 1.7211 - accuracy: 0.4964 - val_loss: 1.5424 - val_accuracy: 0.7046
Epoch 11/20

  256/48000 [..............................] - ETA: 0s - loss: 1.6912 - accuracy: 0.5156
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.6844 - accuracy: 0.5048
12544/48000 [======>.......................] - ETA: 0s - loss: 1.6758 - accuracy: 0.5056
18688/48000 [==========>...................] - ETA: 0s - loss: 1.6729 - accuracy: 0.5050
24832/48000 [==============>...............] - ETA: 0s - loss: 1.6696 - accuracy: 0.5062
30976/48000 [==================>...........] - ETA: 0s - loss: 1.6650 - accuracy: 0.5090
37120/48000 [======================>.......] - ETA: 0s - loss: 1.6600 - accuracy: 0.5088
43008/48000 [=========================>....] - ETA: 0s - loss: 1.6545 - accuracy: 0.5119
48000/48000 [==============================] - 0s 10us/sample - loss: 1.6517 - accuracy: 0.5129 - val_loss: 1.4587 - val_accuracy: 0.7197
Epoch 12/20

  256/48000 [..............................] - ETA: 0s - loss: 1.7056 - accuracy: 0.4609
 6656/48000 [===>..........................] - ETA: 0s - loss: 1.6103 - accuracy: 0.5216
12800/48000 [=======>......................] - ETA: 0s - loss: 1.6125 - accuracy: 0.5220
18944/48000 [==========>...................] - ETA: 0s - loss: 1.6067 - accuracy: 0.5285
25088/48000 [==============>...............] - ETA: 0s - loss: 1.6027 - accuracy: 0.5315
31232/48000 [==================>...........] - ETA: 0s - loss: 1.5968 - accuracy: 0.5329
37376/48000 [======================>.......] - ETA: 0s - loss: 1.5925 - accuracy: 0.5332
43776/48000 [==========================>...] - ETA: 0s - loss: 1.5884 - accuracy: 0.5335
48000/48000 [==============================] - 0s 9us/sample - loss: 1.5854 - accuracy: 0.5344 - val_loss: 1.3788 - val_accuracy: 0.7318
Epoch 13/20

  256/48000 [..............................] - ETA: 0s - loss: 1.5320 - accuracy: 0.5625
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.5371 - accuracy: 0.5467
12544/48000 [======>.......................] - ETA: 0s - loss: 1.5352 - accuracy: 0.5466
18688/48000 [==========>...................] - ETA: 0s - loss: 1.5367 - accuracy: 0.5439
24832/48000 [==============>...............] - ETA: 0s - loss: 1.5343 - accuracy: 0.5436
30720/48000 [==================>...........] - ETA: 0s - loss: 1.5289 - accuracy: 0.5463
36608/48000 [=====================>........] - ETA: 0s - loss: 1.5246 - accuracy: 0.5480
43008/48000 [=========================>....] - ETA: 0s - loss: 1.5219 - accuracy: 0.5494
48000/48000 [==============================] - 0s 9us/sample - loss: 1.5182 - accuracy: 0.5508 - val_loss: 1.3032 - val_accuracy: 0.7439
Epoch 14/20

  256/48000 [..............................] - ETA: 0s - loss: 1.5623 - accuracy: 0.5352
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.4694 - accuracy: 0.5659
12288/48000 [======>.......................] - ETA: 0s - loss: 1.4718 - accuracy: 0.5663
18432/48000 [==========>...................] - ETA: 0s - loss: 1.4711 - accuracy: 0.5654
24832/48000 [==============>...............] - ETA: 0s - loss: 1.4668 - accuracy: 0.5656
30976/48000 [==================>...........] - ETA: 0s - loss: 1.4629 - accuracy: 0.5677
37376/48000 [======================>.......] - ETA: 0s - loss: 1.4601 - accuracy: 0.5686
43520/48000 [==========================>...] - ETA: 0s - loss: 1.4586 - accuracy: 0.5685
48000/48000 [==============================] - 0s 9us/sample - loss: 1.4562 - accuracy: 0.5691 - val_loss: 1.2334 - val_accuracy: 0.7549
Epoch 15/20

  256/48000 [..............................] - ETA: 0s - loss: 1.3685 - accuracy: 0.6094
 6656/48000 [===>..........................] - ETA: 0s - loss: 1.4167 - accuracy: 0.5816
13056/48000 [=======>......................] - ETA: 0s - loss: 1.4111 - accuracy: 0.5837
19456/48000 [===========>..................] - ETA: 0s - loss: 1.4170 - accuracy: 0.5794
25856/48000 [===============>..............] - ETA: 0s - loss: 1.4150 - accuracy: 0.5786
32256/48000 [===================>..........] - ETA: 0s - loss: 1.4129 - accuracy: 0.5794
38656/48000 [=======================>......] - ETA: 0s - loss: 1.4078 - accuracy: 0.5815
45056/48000 [===========================>..] - ETA: 0s - loss: 1.4061 - accuracy: 0.5803
48000/48000 [==============================] - 0s 9us/sample - loss: 1.4051 - accuracy: 0.5803 - val_loss: 1.1695 - val_accuracy: 0.7667
Epoch 16/20

  256/48000 [..............................] - ETA: 0s - loss: 1.3286 - accuracy: 0.6211
 6656/48000 [===>..........................] - ETA: 0s - loss: 1.3742 - accuracy: 0.5934
13056/48000 [=======>......................] - ETA: 0s - loss: 1.3709 - accuracy: 0.5927
19456/48000 [===========>..................] - ETA: 0s - loss: 1.3701 - accuracy: 0.5922
25856/48000 [===============>..............] - ETA: 0s - loss: 1.3668 - accuracy: 0.5915
32256/48000 [===================>..........] - ETA: 0s - loss: 1.3601 - accuracy: 0.5927
38656/48000 [=======================>......] - ETA: 0s - loss: 1.3556 - accuracy: 0.5943
45056/48000 [===========================>..] - ETA: 0s - loss: 1.3520 - accuracy: 0.5956
48000/48000 [==============================] - 0s 9us/sample - loss: 1.3512 - accuracy: 0.5955 - val_loss: 1.1108 - val_accuracy: 0.7773
Epoch 17/20

  256/48000 [..............................] - ETA: 0s - loss: 1.3122 - accuracy: 0.6094
 6656/48000 [===>..........................] - ETA: 0s - loss: 1.3191 - accuracy: 0.6073
12800/48000 [=======>......................] - ETA: 0s - loss: 1.3212 - accuracy: 0.6047
19200/48000 [===========>..................] - ETA: 0s - loss: 1.3188 - accuracy: 0.6042
25344/48000 [==============>...............] - ETA: 0s - loss: 1.3167 - accuracy: 0.6064
31488/48000 [==================>...........] - ETA: 0s - loss: 1.3137 - accuracy: 0.6058
37632/48000 [======================>.......] - ETA: 0s - loss: 1.3074 - accuracy: 0.6075
44032/48000 [==========================>...] - ETA: 0s - loss: 1.3052 - accuracy: 0.6076
48000/48000 [==============================] - 0s 9us/sample - loss: 1.3031 - accuracy: 0.6068 - val_loss: 1.0570 - val_accuracy: 0.7866
Epoch 18/20

  256/48000 [..............................] - ETA: 0s - loss: 1.3247 - accuracy: 0.5859
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.2904 - accuracy: 0.6108
12544/48000 [======>.......................] - ETA: 0s - loss: 1.2787 - accuracy: 0.6132
18944/48000 [==========>...................] - ETA: 0s - loss: 1.2693 - accuracy: 0.6160
25344/48000 [==============>...............] - ETA: 0s - loss: 1.2667 - accuracy: 0.6160
31488/48000 [==================>...........] - ETA: 0s - loss: 1.2650 - accuracy: 0.6160
37632/48000 [======================>.......] - ETA: 0s - loss: 1.2637 - accuracy: 0.6157
43776/48000 [==========================>...] - ETA: 0s - loss: 1.2603 - accuracy: 0.6172
48000/48000 [==============================] - 0s 9us/sample - loss: 1.2587 - accuracy: 0.6173 - val_loss: 1.0080 - val_accuracy: 0.7961
Epoch 19/20

  256/48000 [..............................] - ETA: 0s - loss: 1.2564 - accuracy: 0.6328
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.2271 - accuracy: 0.6327
12288/48000 [======>.......................] - ETA: 0s - loss: 1.2192 - accuracy: 0.6358
18176/48000 [==========>...................] - ETA: 0s - loss: 1.2199 - accuracy: 0.6329
24320/48000 [==============>...............] - ETA: 0s - loss: 1.2186 - accuracy: 0.6332
30208/48000 [=================>............] - ETA: 0s - loss: 1.2171 - accuracy: 0.6341
36352/48000 [=====================>........] - ETA: 0s - loss: 1.2163 - accuracy: 0.6329
42496/48000 [=========================>....] - ETA: 0s - loss: 1.2155 - accuracy: 0.6323
48000/48000 [==============================] - 0s 10us/sample - loss: 1.2142 - accuracy: 0.6329 - val_loss: 0.9632 - val_accuracy: 0.8041
Epoch 20/20

  256/48000 [..............................] - ETA: 0s - loss: 1.0974 - accuracy: 0.6602
 6400/48000 [===>..........................] - ETA: 0s - loss: 1.1945 - accuracy: 0.6380
12544/48000 [======>.......................] - ETA: 0s - loss: 1.2047 - accuracy: 0.6299
18688/48000 [==========>...................] - ETA: 0s - loss: 1.1987 - accuracy: 0.6318
24832/48000 [==============>...............] - ETA: 0s - loss: 1.1929 - accuracy: 0.6329
30976/48000 [==================>...........] - ETA: 0s - loss: 1.1895 - accuracy: 0.6345
37120/48000 [======================>.......] - ETA: 0s - loss: 1.1896 - accuracy: 0.6351
43264/48000 [==========================>...] - ETA: 0s - loss: 1.1848 - accuracy: 0.6371
48000/48000 [==============================] - 0s 9us/sample - loss: 1.1827 - accuracy: 0.6376 - val_loss: 0.9231 - val_accuracy: 0.8110

   32/10000 [..............................] - ETA: 0s - loss: 0.8755 - accuracy: 0.8438
 3072/10000 [========>.....................] - ETA: 0s - loss: 1.0355 - accuracy: 0.7679
 6208/10000 [=================>............] - ETA: 0s - loss: 0.9898 - accuracy: 0.7837
 9408/10000 [===========================>..] - ETA: 0s - loss: 0.9246 - accuracy: 0.8099
10000/10000 [==============================] - 0s 16us/sample - loss: 0.9278 - accuracy: 0.8082
'''