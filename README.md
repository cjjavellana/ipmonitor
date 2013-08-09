Short Story
===============================================
I have setup my personal CI (Continuous Integration Tool) using jenkins and GitHub. 
Whenever I push something to GitHub, GitHub would call Jenkins (using webhook) to tell it 
to update and initiate the build. But what would happen, if my router's external IP address change?
Ofcourse, GitHub would not be able to contact Jenkins anymore, right?

Well, here's the solution (proposed, atlease).

Create a perpetual monitor, a sort of watchdog program to continually probe the router if the external IP has changed.
Once a change is detected, Update Jenkin's Webhook in GitHub with the new external IP of my router.

How To Detect that the router's IP has changed?
====================================================
Comparing the IP of the previous run against the IP extracted in the current run 

Project Dependencies
===================================================
Python 2.7.5
BeautifulSoup 4

