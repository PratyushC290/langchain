from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(   #kwargs = keyword arguments 
        temperature=0.5,
        max_new_tokens=30
    )
)
model = ChatHuggingFace(llm=llm)

answer = model.invoke("What is the capital of India")

print(answer.content)