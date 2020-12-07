import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


# map of userID to number of complete TODOs for that user
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            # increment the existing user's count
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # this user has not been seen. set their count to 1
            todos_by_user[todo["userId"]] = 1



# sort dictionary by value 
top_users = sorted(todos_by_user.items(), key = lambda x:x[1], reverse=True)

# max_complete
max_complete = top_users[0][1]

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)