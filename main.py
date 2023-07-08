import openai
import streamlit as st

openai.api_key = st.secrets['pass']

st.header("Summary Writer")

article_text = st.text_area("Enter the text that you want to summarize")

output_size = st.radio( label = ' What kind of output do you want?', 
                        options= ['To-The-Point', 'Concise', 'Detailed'])

# First, we'll use an if statement to determine the desired output size 
# and set the out_token variable accordingly:

if output_size == 'To-The-Point':
 out_token = 50
elif output_size == 'Concise':
 out_token = 128
else:
 out_token = 516


if len(article_text)>40:
    if st.button("Get the Summary"):
         response = openai.Completion.create(
                    engine = "text-davinci-002",
                    prompt = "Please summarize this scientific article for me in a few sentences: "+ article_text,
                    max_tokens = out_token,
                    temperature = 0.5)
 # Generate the summary
    res = response['choices'][0]['text']
    st.success(res)

    st.download_button('Download result', res)
            
else:
    st.warning("Not enough words to summarize!")