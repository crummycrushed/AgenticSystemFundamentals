import streamlit as st
import pandas as pd
import requests
import plotly.express as px


# step 1 : get the data
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)



# step 2: data cleaning
df = df.rename(columns={"userId": "user_id"})
df = df.drop(columns=["id"])

df["post_length"] = df["body"].apply(len)


st.title(" Simple Post Dashboard")


st.write("Showing Data")
st.dataframe(df.head(20))



st.subheader("Filter by user")
user = st.selectbox("Select User", df["user_id"].unique()) # 4
user_df = df[df["user_id"] == user] # df[give me all userId details whose value = 2] # df[df["user_id"] == 5]
st.write(user_df)




st.subheader("Post Length Distribution")
fig = px.histogram(df, x="post_length")
st.plotly_chart(fig)
