#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends2 = friends + new_friend

friends3 = sorted(friends2)
print(friends3)

# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))