import re, string, time, webbrowser, ssl
import pyperclip, pyautogui
from bs4 import BeautifulSoup
from urllib.request import urlopen

share = 'https://www.facebook.com/dialog/share?app_id=11111111111&href='

url = pyperclip.paste()

webbrowser.open(share + url)

context = ssl._create_unverified_context()
html = urlopen(url, context=context).read().decode("utf-8")
# using beautifulsoup
bs = BeautifulSoup(html, 'html.parser')

str4 = bs.find(["title"])

ConvertListToString = ' '.join(map(str, str4)) 

#remove html code from our scrape (<title>)
str3=re.sub('<title>' , '', ConvertListToString)

#delete punctuation characters
regex = re.compile('[%s]' % re.escape(string.punctuation))
str2 = regex.sub(' ', str3)


def ConvertStringToList(string):                                 
    li = list(string.split(" "))                     
    return li
  
    # return string   
    return str1  

ConvertStringToList(str2)

#removals of any space elements in the list
removal_list = [" "]
edit_string_as_list = str2.split()

final_list = [word for word in edit_string_as_list if word not in removal_list]

str2 = ' '.join(final_list)

#Capitalize all letters  
                            
str1 = " ".join([                                    
    word.capitalize()                                
    for word in str2.split(" ")                      
]) 

# The prefix for the hashtags                                       
prefix="#share"    

# Append prefix to strings in list                   
pres_res = [prefix + sub for sub in ConvertStringToList(str1)]     
pres_res.append('#uberSpurcat #uberNinja #uberBotty')

ConvertListToString = ' '.join(map(str, pres_res)) 

time.sleep(8)

pyautogui.write(str3)

pyautogui.press('space')

pyautogui.press('enter')

pyautogui.press('enter')

pyautogui.write(ConvertListToString)

#pyautogui.press('tab', presses = 8)

pyautogui.press('enter')
