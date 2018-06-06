import urllib

def read_text():
    quotes = open("C:\Users\eshu\Desktop\python projects\fie.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    #print (output)
    connection.close()
    if "true" in output:
        print ("Profanity Alert!!")
    elif "false" in output:
         print ("No curse words!")
    else:
         print ("Not Sure if any curse words.")
         

read_text()
