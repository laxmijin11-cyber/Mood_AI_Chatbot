from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
# Using init_chat_model
from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")
# model = init_chat_model("gpt-5")
# print(model)
# response=model.invoke("What is cricket?")
# print(response.content)

# Using Model Class
# from langchain_openai import ChatopenAI
# model=ChatOpenAI(model="gpt-5")
# response=model.invoke("What is cricket?")
# print(response.content)

# Gemini models
# model = init_chat_model(model="gemini-3.7-flash", model_provider="google_genai")
# model = init_chat_model(model="gemini-3.5-flash-lite", model_provider="google_genai")

# response = model.invoke("What is a football?")
# print(response.content)

# answer_text = response.content[0]["text"]
# with open("football.txt", "w", encoding="utf-8") as f:
#     f.write(answer_text)
# print("saved to football.txt")

# from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
# response = model.invoke("What is a football?")
# print(response.content)

# from langchain_groq import ChatGroq
# model = ChatGroq(model="openai/gpt-oss-120b")
# response = model.invoke("explain ml in 25 words")
# print(response.content)

# from langchain.chat_models import init_chat_model
# model = init_chat_model("groq:openai/gpt-oss-120b")
# response = model.invoke("explain ml in 25 words")
# print(response.content)

# MistralAI-mistralai studio->docs and api->model choose
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=10)
response = model.invoke("write a poem on ml")
print(response.content)
# temperature-0--->mathematical
# temperature=0.7/0.8 for poetry,creativity,story,funny joke
# max_tokens to not hit free tier limits
