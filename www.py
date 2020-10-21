#! python3
import re, string, time, webbrowser 
import pyperclip, pyautogui ,requests

#transforms the url into the title and hashtags
class WierdSite:
    def run(self):
        url = pyperclip.paste()
        r = requests.get(url)
        #r.encoding = r.apparent_encoding #take to much time
        source_code = r.text


        regex = re.compile('[%s]' % re.escape(string.punctuation))
        str2 = regex.sub(' ', url)

        removal_list = ["https","www","com","net","org","ro","de","http"]
        edit_string_as_list = str2.split()

        final_list = [word for word in edit_string_as_list if word not in removal_list]

        str2 = ' '.join(final_list)

        def ConvertStringToList(string):                                 
            li = list(string.split(" "))                     
            return li
        
            # return string   
            return str1  


        #Capitalize all letters  
                                    
        str1 = " ".join([                                    
            word.capitalize()                                
            for word in str2.split(" ")                      
        ])                                                   
                                                            
        # The prefix for the hashtags                                       
        prefix="#uber"                                         
                                                            
        # Append prefix to strings in list                   
        pres_res = [prefix + sub for sub in ConvertStringToList(str1)]     
        pres_res.append('#uberSpurcat #uberNinja #uberBotty')

        #del pres_res[:6]

        ConvertListToString = ' '.join(map(str, pres_res)) 


        time.sleep(10)

        pyautogui.write(str2)

        pyautogui.press('space')

        pyautogui.press('enter')

        pyautogui.press('enter')

        pyautogui.write(ConvertListToString)

        time.sleep(3)

        pyautogui.press('tab', presses = 8)

        pyautogui.press('enter')

        time.sleep(1)

        pyautogui.hotkey("ctrl","w")
