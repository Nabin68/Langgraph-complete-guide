from langchain_cohere import ChatCohere
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["LANGCHAIN_PROJECT"]="Sequential LLM App"

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1=ChatCohere(model="command-r-plus-08-2024")


model2 = ChatCohere(model="command-r-08-2024")

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser


#to insert the tags and metadata explicitly in trace
config={
    "run_name":"sequential_chain", #to give name explicitly to each trace
    "tags":["llm_app","report_generation","summarization"],
    "metadata":{"model1":"Cohere","model2":"HuggingFace Inference","parser":"stroutputparser"}
}

result = chain.invoke({'topic': 'Unemployment in India'},config=config)

print(result)
