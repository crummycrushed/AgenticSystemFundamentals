import requests 
# Libraray to make api calls
import pandas as pd
# libraray to handle data 

import matplotlib.pyplot as plt


url = "https://jsonplaceholder.typicode.com/posts"  #The is the place where data lives


response = requests.get(url) # Fetch data from the server, equivalent to url in browser

print("Status code: ", response.status_code) # show status 


data = response.json() #convert into python dict

# convert json into pandas dataframe

df = pd.DataFrame(data) #data frame , basically kind of tabular data

#print(df.head()) #Shows first 5 rows


# API --> JSON --> Dataframe

#print(df.shape)
#print(df.info()) #column name, data tyoes, null values
#print(df.describe()) # mean, min, max, 



#cleaning of data 
# rename column userId to user_id
# drop column id

df = df.rename(columns={
    "userId": "user_id"
})

df = df.drop(columns=["id"])

#print(df.head())



# count posts per user
post_counts = df.groupby("user_id").size()  # group rows by users #count rows in each group
print(post_counts)


# Create new colum , post_length 

df["post_length"] = df["body"].apply(len) # runs len fucntion over each row
# len is a function , apply -- apply this function over each row of the given column


# len(" quia et suscipit\nsuscipit recusandae consequu... ") 158
#  len (" est rerum tempore vitae\nsequi sint nihil repr... ") 206
#  len("et iusto sed quo iure\nvoluptatem occaecati om...   ") 164

print(df.head())

#post_counts.plot(kind="bar")

#plt.title("Posts per user")
#plt.xlabel("User ID")
#plt.ylabel("Number of Posts")

#plt.show()


df["post_length"].hist()
plt.title("Post length destribution")
plt.xlabel("Characters")
plt.ylabel("Frequency")
plt.show()