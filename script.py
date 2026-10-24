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
    
