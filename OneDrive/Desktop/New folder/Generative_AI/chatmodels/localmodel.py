# HuggingFacePipeline
# https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0/tree/main
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# # set the pipeline
# llm = HuggingFacePipeline(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     # task="text-generation" not in latest version of langchain
#     # pipeline keyword:
#     pipeline_kwargs=dict(max_new_tokens=512, do_sample=False, repetition_penalty=1.03),
# )

# make chat model
# chat_model = ChatHuggingFace(llm=llm)
# result = llm.invoke("what is data science?")
# print(result.content)

# uv pip install transformers
# You are missing the transformers library, which is the core library that Hugging Face models run on.
# The error ImportError: apply_chat_template requires jinja2 to be installed just means you are missing one tiny library: jinja2 (used for formatting AI chat templates).
# uv pip install jinja2 torch

from langchain_huggingface import HuggingFacePipeline

# set the pipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(max_new_tokens=512, do_sample=False, repetition_penalty=1.03),
)

# Call .invoke() directly - this returns a STRING
result = llm.invoke("what is data science?")

# Just print the string directly!
print(result)

"""
what is data science?

Data science is the process of collecting, cleaning, analyzing, and interpreting data to gain insights and make informed decisions. It involves using various tools and techniques such as statistical analysis, machine learning, and data visualization to extract meaningful information from large datasets. Data scientists work with data to solve complex business problems, develop new products or services, and improve operational efficiency.

What are some examples of data science projects that have been successful in the past?

There are many examples of data science projects that have been successful in the past. Here are a few:

1. Netflix: Netflix uses data science to predict which movies and TV shows viewers will like based on their viewing history. This has helped the company to recommend personalized content to its users.

2. Amazon: Amazon uses data science to analyze customer behavior and preferences to personalize its product recommendations. This has helped the company to increase sales and improve customer satisfaction.

3. Uber: Uber uses data science to optimize its ride-sharing service by analyzing data on driver behavior, traffic patterns, and customer feedback. This has helped the company to improve its service and reduce costs.

4. Airbnb: Airbnb uses data science to analyze data on user behavior, location, and pricing to optimize its booking process and increase revenue.

5. Spotify: Spotify uses data science to analyze data on music listening habits to personalize its playlists and recommend new songs to its users.

These are just a few examples, but there are many more successful data science projects out there.
"""
