# First demo
# import gradio as gr
#
# def greet(name):
#     return "Hello a  " + name + "!!"
#
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
#
# demo.launch(share=True)
#



# Second demo
# import gradio as gr
#
# def greet(name):
#     return "Hello " + name + "!"
#
# demo = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(lines=2, placeholder="Name Here..."),
#     outputs="text",
# )
#
# demo.launch(share=True)

# Third demo
# import gradio as gr
#
# def greet(name, is_morning, temperature):
#     salutation = "Good morning" if is_morning else "Good evening"
#     greeting = "%s %s. It is %s degrees today" % (salutation, name, temperature)
#     celsius = (temperature - 32) * 5 / 9
#     return greeting, round(celsius, 2)
#
# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     outputs=["text", "number"],
# )
# demo.launch(share=True)

# Fourth demo
import numpy as np

import gradio as gr

def sepia(input_img):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")

demo.launch(share=True)