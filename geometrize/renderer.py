import numpy as np

def render_shape(canvas, mask, color, alpha):
    color_arr = np.array(color, dtype=np.int16)
    mask = mask[:,:,None]
    return (canvas*(1-alpha*mask) + color_arr*(alpha*mask)).astype(np.int16)
