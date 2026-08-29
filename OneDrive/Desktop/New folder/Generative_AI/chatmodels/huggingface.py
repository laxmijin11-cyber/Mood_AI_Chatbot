from dotenv import load_dotenv

load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# https://huggingface.co/deepseek-ai/DeepSeek-R1
# https://docs.langchain.com/oss/python/integrations/chat/huggingface
# model card mei repo id
llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-R1", max_new_tokens=10)
model = ChatHuggingFace(llm=llm)
response = model.invoke("who are you ?")
print(response.content)
