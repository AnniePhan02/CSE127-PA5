#!/usr/bin/env python3
ciphertext = """UANJHLUFLAFWZUQJIJYOVPFKKJSLOGNTSPJOBIRZUPONPNTUOMIAYWHUESKWRLKAHNXTJP
QGURTZAHVONGSFNLASFISUACZGPXGVPTZZKUTEYFSJAZIZSPJMGETSZHZQBFHPSUGWYNUN
NEKFILJAZIJWJLMFOZHOPFVONRWVDGWSYMVDBQWLSVNNHJHVUAZUFSKVGEJFYPVZNHXJJB
DVPDYVOMIAXYYVZTASHYFBGETSZAMAZFWKZFUAIJCLXBLRJUAMAZWTIBEGWITWAUBJTKZA
DBJLJUJDLLYNVUUFWPJFAABHYTZLOHNJHVTYRNHJHUPGNFILZMSALZHYPCNNAHAQVJKTYT
MGETSWYAZKYJMYQRACUYLEFETSHUPNOXTJPMGETSHUPFPWJUNFUASHFIQEOJHBYUGUYMLK
QCWWYTLZGEXTUATRBWTUAXVJJXVMFUAKNNOFNCFNUZFPUGJYJDVIJFUKIRGSTDMUEOYMHU
PGDJIHTMTAYMHAONJGJJHGFAIGFATBOJBOVQKLQTPAHHHSJYHNYAFSKPZFAHZYLELOYJTZ
IROZUWVDGWSILUOBQWFNLFUAZXLVRFAHZYLZRPBTYREGKUWLCQAPHDILDGDWJHAEGKTZYJ
DVPNHHSZNPNTUHXVJKWHZFEQHYBYQBQWNUAQYHJHABMYLWTWLDGUFSKVGEZFYHZANOYTWY
AZKYJVBDBRJWHSXFWKJAFMZAWNJHZPEYNGLZFYFWLKQRLQDHIAHPUWPCMPUFSKYUTDYQFZ
AZWSDJVYCWSNLZTNRJGLLZEAXUVUPVJLYVHYNNPJAKQZWSIMVDCNTIBJFFWSIZLDIEHJZA
TNPUWVAQPPYMLWDVRFHFHZQOJHBYUGUTKAOQVNHZZAAZAWXAOUFDFXNLZRNFYLKBBONYPC
QVJSTCHFVKSYOHFUWXGLLZPNZHPHXGKYMLKUTEYFSLOBJTRFDQGKTHHYQNXTZAATROJNTW
AEPFSAWDVJHNWSQFESILLPVPNXVBDBXQNNHFVKSYVBBUKQIJPHVHQNILDGEJXPUOYQINUN
FUAWNNOFGKUWPCMPUBJOHHRWQBHFEEAXULJFRZYMLMGAZFRLUFNHWNNOFBBUJVWXRPTJUN
MTANSWYUIWYJJVYZQSNJHFVKSXYLSNNIQLZEBBYMLTQQEZRVYFRYMSVSATUBMLATRNNYPZ
UAOYFUAYROXFNLEGACYZVDBHIKHZTVKSJKSQGPJWZJUGEEJUZTNRJYOLDVCMYAVOBIRZUP"""

ciphertext = ciphertext.replace('\n','')
key = "MNWFFHH"

def vigDecrypt(ciphertext, key):
    decrypted = ''
    for i, ch in enumerate(ciphertext):
        decrypted += unshiftLetter(ch, key[i % len(key)])
    return decrypted

def unshiftLetter(letter, keyLetter):
    letter = ord(letter) - ord("A")
    keyLetter = ord(keyLetter) - ord("A")
    new = (letter - keyLetter) % 26
    return chr(new + ord("A"))


decrypted_message = vigDecrypt(ciphertext, key)
print(decrypted_message)

# print(ciphertext.replace('\n',''))



def find_repeating_sequences(s):
    # Dictionary to store sequences and their counts
    sequence_counts = {}
    length = len(s)
    
    # Iterate through the string to find all possible substrings
    for i in range(length):
        for j in range(i + 1, length + 1):
            sequence = s[i:j]
            if sequence in sequence_counts:
                sequence_counts[sequence] += 1
            else:
                sequence_counts[sequence] = 1
    
    # Filter out sequences that repeat (count > 1)
    repeating_sequences = {seq: count for seq, count in sequence_counts.items() if count > 1}
    
    toReturn = []
    for word in repeating_sequences: 
        if (len(word) == 8):
            toReturn.append(word)
        
    return toReturn

# repeating_sequences = find_repeating_sequences(ciphertext)
# print(repeating_sequences)

# toReturn = find_repeating_sequences(ciphertext)
# print(toReturn)

