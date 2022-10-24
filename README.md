# Pvot
A django online voting app. An extension of the polling app on the official django tutorial.
pvot is currently hosted here ... https://pvot.pythonanywhere.com

I took the simple polling app on the official django tutorial page enhanced it so that it:
    - looks better (I used the Bootstrap freamwork to make things a bit shiny
    - accepts and checks user credentials upon voting. users need to be registered before voting
      and the task of registering new users is up to the site administrator. we have a data model
      for the users so they can be added, deleted or modified via the default django admin site
    - works in 3 different languages: English, Amharic and Oromic. the way i made this work is a 
      bit cluncky. no need to get into the details here. look at the templates to find out. 
      and, of course, sorry for the not annotated code.
    - there are other minor additions like the 'learn how to use' page, but i know that's not big
      deal. it shouldn't count.

It's possible to download and unpack the code on your machine to run pvot locally. just make sure 
you have a python 3 environment with django (preferably the latest version) installed on it. You 
might need to tweak the mysite/mysite/settings.py file a little to make the whole thing run 
locally on your machine.
