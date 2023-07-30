import gradio as gr


def echo(text):
    return text


iface = gr.Interface(fn=echo, inputs="text", outputs="text", title="Hello World!")
iface.launch(share=True)
