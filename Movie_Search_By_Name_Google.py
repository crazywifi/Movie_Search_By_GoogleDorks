
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
movie = raw_input("Enter Movie Name: ")

query = "site:vidoza.net "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)

query = "site:filerio.in "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)

query = "site:uptobox.com "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)

query = "site:userscloud.com "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)
    
query = "site:dl2.yoozdl.com "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)
    
query = "site:dl8.heyserver.in "+movie
print query
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(j)

