__author__ = 'adi'

cipher1 = "F64E6B2CA93517BD29580AEDC58DDCD18E2D5C5EA98BE9CDA24200229EC11B2A00C5E4D010DD42716D660C5099FF632DC5E5AFF8D84C8CADD4F96391B5CDD6730F1FC4B1A5"
cipher2 = "F9456B2CB83600BD6C5D0AEED39FD1909A3B135EE886A1DAA611116DD6CF1D38458CE58510955339462F1C5183BC7F7ABEA4B3F2C340C08CDFFA6385B1C8DF361F02CDB0E5165BE556F68CC629F6C6A481128BD78F9D"
cipher3 = "E441617FAD6401F37E5658E48497DB909D3A5C43BA97BDCBB2110471D6DB142700C5F9DC44E64221576E4B7582AA746CFCE1FBEFDF0CC8C3C5F5268AA28BD677081281B8E41613E14AB2C3DC22FC9D"
cipher4 = "FD457662A96315BF685749EAC0DEC7C6993B5C47A7D2A4DEA054456193DA082349C2AA840CD45371706A1B4C8CF85D62E0E0BAF5D540DB82C2BD2D8CA48BD67F1F1FC4BBE20C1CAA"
cipher5 = "FA597D6FA92F1EB2294A4BE6C0DEDBDF912C085BA19CAE9FBF59006CDA881D2C448CFE9801955434537B0A1881B9656AFAE1BFBBD10CC38DD6BD348AA4C39A62040E81A7EE110FA457F48CC629FC93AF880284C7909D"
cipher6 = "E0452F7BA93117F37D5846E4CD90CF909D2B1346BCD2BDD7AE1115709FC61F270C8CD9910AC64671506E025CC1F87868E0A4ADF4D903C9C3C2F22597F0CAC9360D4BCABCF81155"
cipher7 = "E4486A2CBB2201F37D514FAFC09FDDD7943D1941E89DAF9F9C580B7693DA1A274CC0AD8344C65334546E195CCDB97E69B2D7BAF5C3018B9091F92682A2CEC9624C0DD3BCEE0C1FAA"
cipher8 = "FF45287FEC241DBA675E0AFBCBDEC5D18E3B0513A097BB93EB5D0C7682C4196262C9FE9844C64638472F0F4A88B97D64FEFDF7BBD815CB84D8F324C3B8CEC8650907C7FB"
cipher9 = "E4486A2CA42216F3681948E0CA8788D69D2A191FE881A1DEB94145678FCD0F6E00CDE49444D407254B66051881B16061F7F7A8BBDD0FD997D9BD2E82B4CE9A70031981B3F90D0CEA51FCCB9C"
cipher10 = "E4486A2CBE2C01B6294D45AFCC9BDA909A2C1947E4D2BACBAA43066A93CC5C314BC5F88417955524507B075183BF306CE1A4A8F3D540DF97D0EF3786B48BDB751E04D2A6AB1613E118E0C3DD2CB7"
cipher11 = "F652766DE06311BC645C0AEDC59DC390942C0E56E9D28DD0A51611228FC7096254CDE19544D4493E57670E4ACDAB6468E2A5FBC2DF15DEC3DDFC279AF0C6D562040ED3F5FC0B17E818FAC9D333B9DCA5C91285CB909D"

plain4 = "Jeyne glanced over to make certain that Septa Mordane was not listening."
plain5 = "Myrcella said something then, and the septa laughed along with the rest of the ladies."

messages = [cipher1, cipher2, cipher3, cipher4, cipher5, cipher6, cipher7, cipher8, cipher9, cipher10]
cipherAscii = []
key = []
decrypted = []
keyPos = []
partial = []
xoredCiphers = []
xoredOutputs = []

import re


def slide():
    charset = '^[A-z ]+$'
    response = ''

    while response != 'end':
        crib = raw_input("Please enter your crib: ")
        crib_len = len(crib)

        for combined in xoredOutputs:
            ctext = combined
            ctext_len = len(ctext)
            display_ctext = "_" * ctext_len
            display_key = "_" * ctext_len
            results = sxor(ctext, crib)
            results_len = len(results)

            # Generate results
            for result_index in xrange(results_len):
                if (re.search(charset, results[result_index])):
                    print '*** ' + str(result_index) + ': "' + results[result_index] + '"'
            print combined.encode('hex')
            print "===============================================next=========================================================="
                    # else:
                    #   print str(result_index) + ': "' + results[result_index] + '"'

            '''response = raw_input("Enter the correct position, 'none' for no match, or 'end' to quit: ")

            # Replace part of the message or key
            try:
                response = int(response)
                if (response < results_len):
                    message_or_key = ''
                    while (message_or_key != 'message' and message_or_key != 'key'):
                        message_or_key = raw_input(
                            "Is this crib part of the message or key? Please enter 'message' or 'key': ")
                        if (message_or_key == 'message'):
                            display_ctext = display_ctext[:response] + crib + display_ctext[response + crib_len:]
                            display_key = display_key[:response] + results[response] + display_key[response + crib_len:]
                        elif (message_or_key == 'key'):
                            display_key = display_key[:response] + crib + display_key[response + crib_len:]
                            display_ctext = display_ctext[:response] + results[response] + display_ctext[
                                                                                           response + crib_len:]
                        else:
                            print 'Invalid response. Try again.'

            except ValueError:
                if (response == 'end'):
                    print "Your message is: " + display_ctext
                    print "Your key is: " + display_key
                elif (response == 'none'):
                    print "No changes made."
                else:
                    print "Invalid entry."'''


def sxor(ctext, crib):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    results = []
    single_result = ''
    crib_len = len(crib)
    positions = len(ctext) - crib_len + 1
    for index in xrange(positions):
        single_result = ''
        for a, b in zip(ctext[index:index + crib_len], crib):
            single_result += chr(ord(a) ^ ord(b))
        results.append(single_result)
    return results


def print_linewrapped(text):
    line_width = 40
    text_len = len(text)
    for chunk in xrange(0, text_len, line_width):
        if chunk > text_len - line_width:
            print str(chunk) + chr(9) + text[chunk:]
        else:
            print str(chunk) + chr(9) + text[chunk:chunk + line_width]


def hexToString(hexString):
    decoded = hexString.decode("hex")
    # print decoded
    return decoded


def strToHex(string):
    encoded = string.encode("hex")
    # print encoded
    return encoded


def check_for_space(string, index):
    counter = -1
    for cipher in cipherAscii:
        counter += 1
        if cipher is not string and index < len(cipher):
            # print cipher[counter], ":", ord(cipher[counter])
            c = chr(ord(cipher[index]) ^ ord(string[index]))
            if not c.isalpha():
                return False
            '''if c.isalpha():
                print "Alphaed:", "counter:", counter, "index:", index, "char:", cipher[index], "ascii value:", ord(cipher[index])
                return (True, counter)'''
    return True


def construct_key():
    for i in range(max(map(len, cipherAscii))):
        space = False
        counter = -1
        for cipher in cipherAscii:
            counter += 1
            if i < len(cipher) and check_for_space(cipher, i):
                #print "returnd:", "counter:", counter, "index:", i, "char:", cipher[i], "ascii value:", ord(cipher[i])
                key.append(chr(ord(cipher[i]) ^ ord(' ')))
                keyPos.append(i)
                space = True
        if not space:
            key.append('0')


'''def xor(a, b):
    result = int(a, 16) ^ int(b, 16)  # convert to integers and xor them
    return '{:x}'.format(result)'''


def axor(s1, s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def xoroutputs():
    counter = 0
    for j in range(0, 9):
        s3 = axor(cipher11.decode('hex'), messages[j].decode('hex'))
        counter += 1
        #print s3, len(s3), i, j
        xoredOutputs.append(s3)
    #print counter

def xorciphers():
    counter = 0
    for i in range(0, 10):
        for j in range(i + 1, 10):
            if i is not j:
                s3 = axor(messages[i].decode('hex'), messages[j].decode('hex'))
                counter += 1
                #print s3, len(s3), i, j
                xoredCiphers.append(s3)
                # print counter

def output(a):
    decr = axor(a.decode('hex'), cipher11.decode('hex'))
    stringn = [' '] * 86
    for i in keyPos:
        if i < len(decr):
            stringn[i] = decr[i]
    print ''.join(stringn)

if __name__ == '__main__':
    '''print messages[1]
    print messages[4]
    print xor(messages[1],messages[4])'''
    for m in messages:
        # print m, len(m)
        #print "cipher ascii", hexToString(m)
        cipherAscii.append(hexToString(m))
    #print "31c164311191e0f4517410813410a4f0b171b05491a0f45194811010c47001401001b1d1100070d1554164902051a1044450c49124c03010947570f150b45541b0c4c170b07544101020000000a550b09100f101f00".decode(
        #'hex')
    construct_key()
    # print key
    a = strToHex(''.join(key))
    # print "key:", a, len(a)
    # print hexToString(a), len(hexToString(a))

    for m in messages:
        decrypted.append(axor(a.decode('hex'), m.decode('hex')))
    for p in decrypted:
        #print p, len(p)
        # print hexToString(p)
        string = [' '] * 86
        for i in keyPos:
            if i < len(p):
                string[i] = p[i]
        #print ''.join(string)
        partial.append(''.join(string))
    indices = [' ']*86
    for i in range(0, 85):
        indices[i] = str(i%10)
    print ''.join(indices)
    for m in partial:
        print m
    output(a)
    print len(plain5), len(cipher5.decode('hex'))
    finalKey = axor(plain5, cipher5.decode('hex'))
    finalOutput = axor(finalKey, cipher11.decode('hex'))
    for m in messages:
        print (axor(finalKey, m.decode('hex')))
    print finalOutput
    xorciphers()
    xoroutputs()
    slide()
