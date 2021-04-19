# chuyển đổi mô hình keras sang tflite

import tensorflow as tf

tfl_file_path = 'model_key.tflite'
converter = tf.compat.v1.lite.TFLiteConverter.from_keras_model_file('model_key.h5')
tfl_model = converter.convert()
open(tfl_file_path, "wb").write(tfl_model)