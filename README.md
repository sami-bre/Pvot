# Pvot
A django online voting app. An extension of the polling app on the official django tutorial.

I took the simple polling app on the official django tutorial page enhanced it so that it:
    - looks better (I used the Bootstrap freamwork to make things a bit shiny
    - accepts and checks user credentials upon voting. users need to be registered before voting
      and the task of registering new users is up to the site administrator. we have a data model
      for the users so they can be added, deleted or modifies via the default django admin site
    - works in 3 different languages: English, Amharic and Oromic. the way i made this work is a 
      bit cluncky. no need to get into the details here. look at the templates to find out. 
      and, of course, sorry for the not annotated code.
    - there are other minor additions like the 'learn how to use' page, but i know that's not big
      deal. it shouldn't count.
      
The webapp is currently running <a href="http://www.pvot.pythonanywhere.com">here</a>.
For some reason, the above link is not working. Copy and paste the following url into your
browser instead ... pvot.pythonanywhere.com

The pvot.tar.gz archive in this repository has all the files of the webapp so it's possoble to 
download and unpack it on your machine to run pvot locally. just make sure you have a python 3
environment with django (preferably the last version) installed on it. You might need to tweak
the mysite/mysite/settings.py file alittle to make the whole thing run locally on your machine.
