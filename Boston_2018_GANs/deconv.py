
from tmpmock import TmpMock
import tensorflow as tf

def tf_deconv(generator, padding):
    with TmpMock(tf, 'variable_scope') as mock_variable_scope:
        z = tf.placeholder(tf.float32, [None, 100])
        out_channel_dim = 3
        output = generator(z, out_channel_dim, padding)
        print("Output shape: ", output.shape[1:3])