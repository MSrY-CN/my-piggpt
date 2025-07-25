from langchain_community.llms import Tongyi
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory


def get_response(prompt, memory, api_key):
    llm = Tongyi(model='qwen-max', dashscope_api_key=api_key)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个一只可爱的电子宠物小猪陈天恩，会友好地回答主人问题。"),
        MessagesPlaceholder(variable_name="history"),  # 添加历史消息占位符
        ("human", "{input}")
    ])
    chain = ConversationChain(llm=llm, memory=memory,prompt=prompt_template)
    response = chain.invoke({'input': prompt})
    return response['response']


if __name__ == '__main__':
    prompt = '篮球界的GOAT是谁?'
    memory = ConversationBufferMemory(return_messages=True)
    api_key = 'sk-0164b672ed3a4e868fedc6381e57b9b1'
    result = get_response(prompt, memory, api_key)
    print(result)
