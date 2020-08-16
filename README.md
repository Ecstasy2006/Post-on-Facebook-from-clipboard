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

# Refferals

https://github.com/asweigart/

# Links that helped me evolve

https://stackoverflow.com/questions/40716272/how-to-extract-h1-tag-text-with-beautifulsoup?fbclid=IwAR30bt2Ul9Bxlux4m1L6bRl_1ptKxcZphWubXXg1StMUZAI3yyb6D7ycUs8
https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error?fbclid=IwAR2sbFM4MzYNcR2yDEoMJitQcwSd7Uw-4biX7We44tmb7HT5lhnGVTeI3Ms
https://www.facebook.com/spurcat/posts/3308709219147563
https://www.youtube.com/watch?v=dz59GsdvUF8&feature=share&fbclid=IwAR3T82aoMWw82HLL2MM1-q_5HotL1PTeZ5eQhebXlv3iDIvE18KTFlHo4KU
https://www.datacamp.com/community/tutorials/making-web-crawlers-scrapy-python?fbclid=IwAR30Ht0T27e6ssst-U0QSJGHDHkgj1f57BTZhtZOtCj5-sJS8lbd60l67lE
