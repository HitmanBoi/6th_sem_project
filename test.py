import gradio as gr

def predict(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=predict,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()