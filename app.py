import gradio as gr
import warnings
warnings.filterwarnings('ignore')

from utils import get_chain

def get_answer_and_query(question):
    chain = get_chain()
    response = chain.invoke(question)
    result = response['result']
    sql_query = response['intermediate_steps'][1]
    return result, sql_query

# Define the Gradio interface
demo = gr.Interface(
    fn=get_answer_and_query, 
    inputs=gr.Textbox(label="Enter your question here"), 
    outputs=[
        gr.Textbox(label="Result"),
        gr.Textbox(label="SQL Query")
    ],
    allow_flagging='never'
)

# Add Markdown content
markdown_content = gr.Markdown(
    """
    <div style='text-align: center; font-family: "Times New Roman";'>
        <h1 style='color: #FF6347;'>Query with your DataBase in Natural Language</h1>
        <h3 style='color: #4682B4;'>Model: Text-bison-001</h3>
        <h3 style='color: #32CD32;'>Made By: Md. Mahmudun Nabi</h3>
    </div>
    """
)

# Combine the Markdown content and the demo interface
demo_with_markdown = gr.Blocks()
with demo_with_markdown:
    markdown_content.render()
    demo.render()

if __name__ == "__main__":
    demo_with_markdown.launch()
