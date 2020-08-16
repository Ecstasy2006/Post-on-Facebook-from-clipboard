<img src="Share003.png" align="right" />

# Share-link-with-modified-hashtags-on-Facebook
Share link with modified hashtags on Facebook (#uberSpurcat)

It posts on facebook whatever you have on your clipboard or copied (ctrl+c) and it makes custom hashtags from the url title.

Most important thing to modify or it will not work:

-  share = 'https://www.facebook.com/dialog/share?app_id=<your custom 11 digit facebook id>&href='
                                                              
  example:
+    share = 'https://www.facebook.com/dialog/share?app_id=11111111111&href='
    
# Install:
Use the requirments.txt file (  pyperclip, pyautogui, beautifulsoup4, urllib3 )

Also I was using python 3.6.1 when I did this code.

+If you want the script to automatically press share you can uncomment this line:

#pyautogui.press('tab', presses =8)

Don't forget to set the path variable to the folder where you install/copy the scripts so the batch file works.
