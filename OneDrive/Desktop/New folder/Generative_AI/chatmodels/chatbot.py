from dotenv import load_dotenv

load_dotenv()
# from langchain_mistralai import ChatMistralAI

# model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=12)

# # SHORT TERM MEMORY
# messages = []
# print("-------------welcome type 0 to exit the application-----------")
# # infinite loop till exit zero:ques ask again and again
# while True:
#     prompt = input("You:")
#     messages.append(prompt)
#     if prompt == "0":
#         break
#     response = model.invoke(messages)
#     # model.invoke multiple messages ko dekh paat hai usse koi problem ni hoti
#     messages.append(response.content)
#     print("Bot:", response.content)


# history story as messages and messages even to model.invoke
# model lamba data aaya tha toh confuse ho jayega messages se kaha se kisa aaya
# dictionery mai you:bot but storage badh jayega
"""
You:hi
Bot: Hello! 😊 How can I assist you today?
You:ur name?      
Bot: You can call me **🤖 Assistant** or
You:u r king
Bot: 👑 **Hail to the King, baby
You:ur name?
Bot: Haha, nice to meet you! 👑 You
You:ur name?
Bot: You can call me **🤖 Assistant** (
You:i name u king
Bot: Hail to the King, **Assistant**!
You:ur name?           
Bot: **Hail to the King, baby!**
"""

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=12)

print("Chhose AI mode to respond")
print("press 1 for funny mode")
print("press 2 fro angry mode")
print("press 3 for sad mode")
choice = int(input("tell your response:"))
if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


# SHORT TERM MEMORY
messages = [SystemMessage(content=mode)]
print("-------------welcome type 0 to exit the application-----------")
# infinite loop till exit zero:ques ask again and again
while True:
    prompt = input("You:")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    # model.invoke multiple messages ko dekh paat hai usse koi problem ni hoti
    messages.append(AIMessage(content=response.content))
    print("Bot:", response.content)
    # stored in the form of objects

    print(messages)
    """
    SystemMessage(content='you are funny ai agent', additional_kwargs={}, response_metadata={}), HumanMessage(content='joke on man', additional_kwargs={}, response_metadata={}), AIMessage(content="Here's a lighthearted one for you:\n\n**Why", additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]
    
    response_metadata and kwargs will be used in RAG
    """
