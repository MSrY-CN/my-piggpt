import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import get_response
import os

#设置页面标题、图标
st.set_page_config(
    page_title="赛博猪咪小恩酱",           # 页面标题
    page_icon="🐷",                      # 页面图标
)

#左侧侧边栏
with st.sidebar:
    # 优先使用环境变量中的 API Key
    api_key = os.getenv('DASHSCOPE_API_KEY')
    if not api_key:
        api_key = st.text_input('请输入Tongyi账号的API KEY:', type='password')
        st.markdown('[获取Tongyi账号的API KEY](https://bailian.console.aliyun.com/?tab=app&productCode=p_efm&switchAgent=12416977#/api-key)')
    else:
        st.success("已配置 API Key")

#页面标题
st.title('你的专属奶萌小猪猪')

#创建会话记忆体
if 'memory' not in st.session_state:
    #用户第一次访问该页面,创建一个会话记忆体
    st.session_state['memory'] = ConversationBufferMemory(return_messages=True)
    st.session_state['messages'] = [{'role':'🐷','content':'主人好吖~我是你的电子宠物小恩,主人有什么吩咐呢~~~'}]

#创建消息区
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(message['content'])

#创建文本框,接收用户输入的问题
prompt = st.chat_input('想对恩恩说什么呢：')

#判断输入是否不为空，继续执行
if prompt:
    if not api_key:
        st.warning('请先配置 API KEY')
        st.stop()
    #把用户录入的信息,添加到会话记忆体中
    st.session_state['messages'].append({'role':'🤴','content':prompt})
    #把用户录入的信息,打印到消息区中
    st.chat_message('🤴').write(prompt)
    #调用自定义函数,获取AI回复结果
    with st.spinner('小恩正在思考哦...'):
        response = get_response(prompt, st.session_state['memory'], api_key)

    #把AI的回复添加到会话记忆体中，并打印到消息区
    st.session_state['messages'].append({'role':'🐷','content':response})
    st.chat_message('🐷').write(response)
