# class Factory:
#     a = "I'm an attribute mention inside Factory"
#     def hello(self):
#         print("hello I'm a method mention inside Factory")

# obj1 = Factory()
# obj1.hello()

# import urllib.request
# import json

# url = "https://jsonplaceholder.typicode.com/users"

# with urllib.request.urlopen(url,timeout=10) as response:
#     raw_data = response.read()
    
# text_data = raw_data.decode("utf-8")
# data = json.loads(text_data)
# for user in data:
#     print(f"user name is {user["name"]}")
  
# import urllib.request
# import urllib.error
# import json
    
# url = "https://jsonplaceholder.typicode.com/posts"

# try:
#     with urllib.request.urlopen(url,timeout=10) as response:
#      raw_data = response.read()
    
#     text_data = raw_data.decode("utf-8")
#     data = json.loads(text_data)
    
# except urllib.error as e:
#     print(f"error is : {e}")
# else:
#     print(
#     data[0]["title"],
#     data[0]["body"] 
#     )


# filteration


# import urllib.request
# import json

# url = "https://jsonplaceholder.typicode.com/users"

# with urllib.request.urlopen(url,timeout=10) as response:
#     raw_data = response.read()
    
# text_data = raw_data.decode("utf-8")
# data = json.loads(text_data)
# for user in data:
#     print(f"user name is {user["name"]}")
  
# import urllib.request
# import urllib.error
# import json

# filtered_post = []
# url = "https://jsonplaceholder.typicode.com/posts"

# try:
#     with urllib.request.urlopen(url,timeout=10) as response:
#      raw_data = response.read()
    
#     text_data = raw_data.decode("utf-8")
#     data = json.loads(text_data)
    
# except urllib.error as e:
#     print(f"error is : {e}")
# else:
#    for post in data:
#        if post["userId"] == 1:
#            filtered_post.append(post)
#    print (f"append successfully")
#    for post in filtered_post:
#         print(post["title"])


# import urllib.request
# import urllib.error
# import json

# filtered_post = []
# transformed_post = []
# url = "https://jsonplaceholder.typicode.com/posts"

# try:
#     with urllib.request.urlopen(url,timeout=10) as response:
#      raw_data = response.read()
    
#     text_data = raw_data.decode("utf-8")
#     data = json.loads(text_data)
    
# except urllib.error as e:
#     print(f"error is : {e}")
# else:
#    for post in data:
#        if post["userId"] == 1:
#            filtered_post.append(post)
#    print (f"append successfully")
#    for post in filtered_post:
#         new_post = {
#             "id":post["id"],
#             "title":post["title"].upper()
#         }
#         transformed_post.append(new_post)
        
# print("First transformed post:",transformed_post[0])
# print("lenght of transformed post:",len(transformed_post))


# import urllib.request
# import urllib.error
# import json
# import socket
# import csv

# all_post = []

# page = 1
# limit = 10
# url = "https://jsonplaceholder.typicode.com/posts?_limit=10"

# try:
#     with urllib.request.urlopen(url,timeout=10) as response:
#         raw_data = response.read()
#         data = json.loads(raw_data)
# except(urllib.error.URLError,TimeoutError,socket.timeout) as e:
#     print(f"page {page} have this error {e}")
# if(len(data) == 10):
#     all_post.extend(data)
#     print(f"page {page} fetched: {len(data)} posts")
# print("Total post:", len(all_post))
# print("Total post:", all_post)

# with open("post.csv","w") as file:
#     writer = csv.DictWriter(
#         file,
#         fieldnames=["userId", "id", "title", "body"]
#     )
#     writer.writeheader()
#     writer.writerows(data)
# print("CSV file created successfully!")
               

# import csv

# with open("post.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

