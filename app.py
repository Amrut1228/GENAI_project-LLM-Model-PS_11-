"""Run with: python -m streamlit run app.py"""
import json
import streamlit as st
from chatbot import Chatbot, load_sheet

st.set_page_config(page_title='CampusDesk | MIT ADT', page_icon='🎓', layout='wide')
st.markdown('''<style>
.stApp {background:#f6f8fc; color:#17243b}
h1,h2,h3 {color:#122a4d}
[data-testid="stSidebar"] {background:#11294b}
[data-testid="stSidebar"] * {color:#eef4ff}
[data-testid="stChatMessage"] {background:white; border:1px solid #e2e8f2; border-radius:14px; padding:18px}
.block-container {max-width:1120px;padding-top:2rem}
.eyebrow {font-size:12px;font-weight:700;letter-spacing:2px;color:#4c66a4}
.hero {padding:24px 0 12px}.hero h1{font-size:42px;margin:0}
</style>''', unsafe_allow_html=True)

@st.cache_resource
def get_bot():
    return Chatbot()

sheet = load_sheet()
if 'messages' not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.title('🎓 CampusDesk')
    st.caption('MIT ADT UNIVERSITY')
    st.divider()
    st.markdown('**Your college, a conversation away.**')
    st.write('Courses · Fees · Admissions')
    st.caption('Local AI • Source-based answers')
    if st.button('New conversation', use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.download_button('Download conversation', json.dumps(st.session_state.messages, indent=2),
                       'campusdesk_chat.json', 'application/json', use_container_width=True)
    st.divider()
    st.caption('PROJECT 11 · GENAI MINI PROJECT')
    st.write('Amrut Sachin Shelke')
    st.caption('LYCORE-1 | Roll No. 11')
    st.caption('ADT23SOCB0122')

st.markdown('<div class="eyebrow">MIT ADT UNIVERSITY / ADMISSIONS HELPDESK</div><div class="hero"><h1>Ask. Explore. Plan your next step.</h1></div>', unsafe_allow_html=True)
st.write('Ask about programmes, published fees, and how to apply. Every answer starts with the college information sheet.')
st.info('Academic prototype, not an official university service. Information snapshot: 22 November 2026. Confirm current details with admissions.')
with st.expander('View the college information sheet and official sources'):
    st.text(sheet)
    st.download_button('Download information sheet', sheet, 'college_info.txt', 'text/plain')

if not st.session_state.messages:
    st.subheader('How can we help you today?')
    examples = ['Which engineering courses are listed?', 'What is the B.Tech CSE fee?', 'How do I apply for admission?']
    cols = st.columns(3)
    for col, example in zip(cols, examples):
        if col.button(example, use_container_width=True):
            st.session_state.pending = example

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

question = st.chat_input('Ask a question about MIT ADT University…', max_chars=2000)
question = question or st.session_state.pop('pending', None)
if question:
    with st.chat_message('user'):
        st.markdown(question)
    try:
        with st.chat_message('assistant'):
            with st.spinner('Reading the information sheet…'):
                answer = get_bot().answer(question, st.session_state.messages, sheet)
            st.markdown(answer)
        st.session_state.messages.extend([{'role':'user','content':question}, {'role':'assistant','content':answer}])
    except Exception as exc:
        st.error(f'Could not generate a reply: {exc}')
        st.caption('Your question was not saved. Check the model setup and try again.')
