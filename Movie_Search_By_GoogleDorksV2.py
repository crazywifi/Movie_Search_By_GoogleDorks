from termcolor import colored
from colorama import init
import pyfiglet

init()
# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'


print (colored(pyfiglet.figlet_format("Movie Search By Google Dorks", font="standard"), "red"))
print (G+BOLD+"By Lazy hacker [Follow: https://lazyhacker22.blogspot.com/]\n"+END)


try:
    #pip install googlesearch-python
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    print("pip install googlesearch-python\npip3.exe install google\npip3.exe install beautifulsoup4")

# to search
movie = input("Enter Movie Name: ")

query = "site:vidoza.net "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:www.1377x.to "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:www.1377x.is "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:torrentz2eu.org "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:yts.rs "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END) 

query = "site:filerio.in "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:uptobox.com "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:userscloud.com "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:dl2.yoozdl.com "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:dl8.heyserver.in "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:cdn.par30dl.com "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:dl.sitemovie.ir "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:sv4avadl.uploadt.com "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:79.127.126.110/Movie/ "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
query = "site:tvtv.pk/torrents/ "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:dl.p30movies.co "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)


query = "site:thepiratebay.rocks/torrent/ "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)

query = "site:limetorrents.info "+movie
print (query)
for j in search(query, tld="com", num=10, stop=1, pause=2):
    print(G+j+END)
    
input("Press enter to close...")
