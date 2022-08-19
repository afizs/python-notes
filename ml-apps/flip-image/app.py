import numpy as np

def flip_image(x):
    return np.fliplr(x)
    
import gradio as gr

gr.Interface(fn=flip_image, inputs="image", outputs="image").launch();
