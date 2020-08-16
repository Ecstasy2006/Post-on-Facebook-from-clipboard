<img src="share02.png" align="right" />

# Share-link-with-modified-hashtags-on-Facebook
Share link with modified hashtags on Facebook (#uberSpurcat)

It posts on facebook whatever you have on your clipboard or copied (ctrl+c) and it makes custom hashtags from the url title.

Most important thing to modify or it will not work:

-  share = 'https://www.facebook.com/dialog/share?app_id=<your custom 11 digit facebook id>&href='
                                                              
  example:
+    share = 'https://www.facebook.com/dialog/share?app_id=11111111111&href='
    
Also install:
+  pyperclip, pyautogui, beautifulsoup4, urllib3

+If you want to automatically press share you can uncomment this line:

#pyautogui.press('tab', presses =8)

Don't forget to set the path variable to the folder where you install/copy the scripts so the batch file works.
