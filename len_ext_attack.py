import sys, urllib.parse
from pymd5 import md5, padding
url = sys.argv[1]

parsedUrl = urllib.parse.urlparse(url)
# print(parsedUrl)
hash_old = parsedUrl.query[6:38] # token value
# print(hash_old)
command_old = parsedUrl.query[39:]
# print(command_old)

# token = list(urllib.parse.parse_qs(url).values())[0][0] # with this i can get the token value of the url
# print(token)
m = hash_old + command_old
# m = token + "&user=earlence&command1=ListSquirrels&command2=NoOp" # need a way to somehow parse the message

# # get the current hash
# bits = (len(m) + len(padding(len(m) * 8))) * 8
bits = (len(m) + len(padding(len(m) * 8))) * 8
h = md5(state=bytes.fromhex(hash_old), count=bits) 
# h = md5(m)
# h.update(m)
# print(h.hexdigest())


# need to calculate the padding length


x = "&command3=UnlockAllSafes" # appended value

result = m + urllib.parse.quote(padding(len(m)*8))+ x

# print(result)

h.update(result)
# print(h.hexdigest()) # new token value


new_url= "http://bank.cse127.ucsd.edu/pa5/api?token=" + h.hexdigest() + command_old
print(new_url)