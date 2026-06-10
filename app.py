import gradio as gr
from query import ask


def handle_query(question):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    answer = result["answer"]
    sources = "\n".join(f"• {source}" for source in result["sources"])

    return answer, sources


with gr.Blocks() as demo:
    gr.Markdown("# The Unofficial Guide to UMD CS")
    gr.Markdown("Ask a question about UMD CS professors, courses, workload, grading, or research opportunities.")

    question = gr.Textbox(label="Your question", placeholder="Example: What programming language is used in CMSC414?")
    ask_button = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Retrieved from", lines=4)

    ask_button.click(handle_query, inputs=question, outputs=[answer, sources])
    question.submit(handle_query, inputs=question, outputs=[answer, sources])


if __name__ == "__main__":
    demo.launch()
