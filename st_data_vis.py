import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title('Sentiment Analysis of Tweets about US Airlines')
st.sidebar.title('Sentiment Analysis of Tweets about US Airlines')

st.markdown("## This application is a streamlit dashboard to aid in analysis of the sentiment of tweets about US airlines")
st.sidebar.markdown('WOOOOOOH')

data_url = ("/home/rhyme/Desktop/Project/Tweets.csv")


@st.cache(persist = True)
def load_data():
    data = pd.read_csv(data_url)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()

st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment: ', ('positive', 'neutral', 'negative'))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[["text"]].sample(n = 1).iat[0,0])


st.sidebar.markdown('### Number of tweets by sentiment')
select = st.sidebar.selectbox('Visualisation type', ['Histogram', 'Pie Chart'], key = 'I')
sentiment_count  = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values})

if not st.sidebar.checkbox('Hide', True):
    st.markdown('### Number of tweets by sentiment')
    if select == 'Histogram':
        fig = px.bar(sentiment_count, x = 'Sentiment', y = 'Tweets', color = 'Tweets', height = 500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values = 'Tweets', names = 'Sentiment')
        st.plotly_chart(fig)

st.sidebar.subheader('When and where are users tweeting from?')
hours_of_day = st.sidebar.slider('Hour of the day', 0, 23)
modified_data = data[data['tweet_created'].dt.hour == hours_of_day]
if not st.sidebar.checkbox("Close", True, key = '1'):
    st.markdown('### Tweets locations based on time of day')
    st.markdown('%i tweets between %i:00 and %i:00' % (len(modified_data), hours_of_day, (hours_of_day+1) % 24))
    st.map(modified_data)
    if st.sidebar.checkbox("Show raw data", False):
        st.write(modified_data)

st.sidebar.subheader('Breakdown airline tweets by sentiment')
choice = st.sidebar.multiselect('What airlines would you like to see?', ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'), key = '0')

if len(choice) > 0:
    choice_data = data[data.airline.isin(choice)]
    fig_choice = px.histogram(choice_data, x='airline', y = 'airline_sentiment', histfunc='count', color = 'airline_sentiment',
    facet_col='airline_sentiment', labels = {'airline_sentiment' : 'tweets'}, height = 600, width = 800)
    st.plotly_chart(fig_choice)


st.sidebar.header('Word Cloud')
word_sentiment = st.sidebar.radio('Display word cloud for what sentiment?', ('positive', 'neutral', 'negative'))
if not st.sidebar.checkbox('Close', True, key = '3'):
    st.header('Word cloud for %s sentiment' % (word_sentiment))
    sentiment_data = data[data['airline_sentiment'] == word_sentiment]
    words = ' '.join(sentiment_data['text'])
    processed_words = ' '.join([word for word in words.split() if 'http' not in word and word.startswith('@') and word != 'RT'])
    wordcloud = WordCloud(stopwords = STOPWORDS, background_color = 'white', height = 640, width = 800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()
