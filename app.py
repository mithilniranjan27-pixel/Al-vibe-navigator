import gradio as gr
from inference import predict

def main(city):
    return predict(city)

iface = gr.Interface(
    fn=main,
    inputs="text",
    outputs="text"
)

iface.launch()
