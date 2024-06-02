import sys, urllib.parse
from pymd5 import md5, padding
url = sys.argv[1]

# Your code to modify url goes here

# # Parse the URL to extract the token and parameters
# parsed_url = urllib.parse.urlparse(url)
# query_params = urllib.parse.parse_qs(parsed_url.query)

# # Extract the token
# token = query_params['token'][0]

# # Reconstruct the original message without the token part
# original_message = parsed_url.query.split('&', 1)[1]

# # Calculate the length of the original message including the password
# # The password length is 8 characters
# original_message_length = 8 + len(original_message)

# # Calculate the padding for the original message
# padding_str = padding(original_message_length * 8)

# # Create a new md5 object with the given token as the initial state
# h = md5(state=bytes.fromhex(token), count=(original_message_length + len(padding_str)) * 8)

# # Update the hash with the new data to append
# append_data = '&command3=UnlockAllSafes'
# h.update(append_data)

# # Generate the new token
# new_token = h.hexdigest()

# # Construct the new URL
# new_message = original_message + padding_str.decode('latin1') + append_data
# new_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?token={new_token}&{urllib.parse.quote(new_message)}"

# print(new_url)

# print(query_params['token'])






# ------------ MY PSEUDOCODE --------


token = list(urllib.parse.parse_qs(url).values())[0][0] # with this i can get the token value of the url
# print(token)

# get current state of h
h = md5(state=bytes.fromhex(token), count=512) # is the count correct? Need to check
print(h.hexdigest())


## need to calculate the padding length


appended_value_x = "&command3=UnlockAllSafes"

newMsg = m.encode("utf-8") + padding(len(m)*8) + appended_value_x.encode("utf-8")


h.update(newMsg)
print(h.hexdigest()) # MD5 hash should be the same

new_token = h.hexdigest()

new_url= oldUrlParsed + token + appended_value_x
print(new_url)