facebook_posts = eval(input())

total_likes = 0
# Catching the KeyError exception in the dictionary
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass

print(total_likes)
##sample inouts
##[{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]