import streamlit as st
from openai import OpenAI


model_ia = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
                  )

st.set_page_config(
    page_title="Hello Kitty IA",
    page_icon="https://pngimg.com/d/hello_kitty_PNG22.png"

)



css = """
<style>
    .stChatMessage:has([data-testid="stChatMessageAvatarAssistant"]) {
        background-color: #fa9db8;
    }
    .stChatMessage:has([data-testid="stChatMessageAvatarUser"]) {
        background-color: #f06e94;
    }
    [data-testid="stAppViewContainer"] {
        background-image: url("https://cdn.wallpapersafari.com/26/19/M26bXs.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat; 
        background-attachment: fixed; 
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); 
    }
    div[data-testid="stChatInput"] {
        background-color: #d1567a;
        border-radius: 12px;
        padding: 3px;
    }

    div[data-testid="stChatInput"] textarea::placeholder {
        color: #d1567a !important;
    }

    div[data-testid="stChatInput"] button {
        background-color: #d1567a;
        color: black;
        border-radius: 50%;
    }

    /* Área onde você digita */
    div[data-testid="stChatInput"] textarea,
    div[data-testid="stChatInput"] textarea:focus {
        background-color: #f9a8d4 !important; /* rosa */
    }
    div[data-testid="stChatInput"] > div {
        background-color: #f9a8d4 !important;
        border-radius: 16px;
}
</style>
"""
st.html(css)

style_image = """
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 500px;
    height: 300px;
"""


st.markdown(

    f'<img src="https://brandlogos.net/wp-content/uploads/2014/11/hello_kitty-logo_brandlogos.net_peylh-512x480.png" style="{style_image}">',
    
    unsafe_allow_html=True
)


if not "message_list" in st.session_state:
    st.session_state["message_list"] = []


for message in st.session_state["message_list"]:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content)


message_user = st.chat_input("Escreva sua mensagem")


if message_user:
    st.chat_message("user").write(message_user)
    message = {"role": "user", "content": message_user}
    st.session_state["message_list"].append(message)


    model_chat = model_ia.chat.completions.create(
        messages=st.session_state["message_list"],
        model="openai/gpt-oss-20b:free"
    )

    message_model = model_chat.choices[0].message.content

    st.chat_message("assistant").write(message_model)
    message_ia = {"role": "assistant", "content": message_model}
    st.session_state["message_list"].append(message_ia)


