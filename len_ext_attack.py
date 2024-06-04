import sys, urllib.parse
from pymd5 import md5, padding
url = sys.argv[1]

parsedUrl = urllib.parse.urlparse(url)
# print(parsedUrl)
hash_old = parsedUrl.query[6:38] # token value
#print(hash_old)
command_old = parsedUrl.query[39:]

# # get the current hash
old_len = len("AAAAAAAA" + command_old)
bits = (old_len + len(padding(old_len * 8))) * 8
h = md5(state=bytes.fromhex(hash_old), count=bits) 


# need to calculate the padding length
x = "&command3=UnlockAllSafes" # appended value
h.update(x)

result = command_old + urllib.parse.quote(padding(old_len*8))+ x

# print(result)

# print(h.hexdigest()) # new token value


new_url= "http://bank.cse127.ucsd.edu/pa5/api?token=" + h.hexdigest() + "&" + result
print(new_url)
