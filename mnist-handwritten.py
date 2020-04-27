import tensorflow as tf
mnist = tf.keras.datasets.mnist

#callback fxn
class StopTrainingCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if (logs.get('acc') >= 0.99):
      print('\nReached desired accuracy (0.99), No more training.')
      self.model.stop_training = True

mCallback = StopTrainingCallback()


(x_train, y_train),(x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, callbacks=[mCallback])

# Must add a code block to verify prediction later
