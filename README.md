# AiHeart
# Project in KI/SU ML413N Project Managment for HI
# as part of program in Master of Health Informatics

Package requirements are saved in requirements.txt.

Create a new virtual environment by going to the AiHeart folder in the terminal using the cd command.
Then type the following commands: 

"python -m venv [Insert the desired name of the virtual environment here]"
".\\[Name of virtual environment]\Scripts\activate.bat"

At this point the terminal should start with the name of your virtual environment. For example like this,
if the name were to be ".venv":
"(.venv) C:\Users\matti\MAIniacs\AiHeart>"

We are now in our virtual environment. In the next part we will install all necessary packages into our
virtual environment. write these commands while being inside the virtual environment:

"pip install -r requirements.txt"

If you have changed any packages while developing and want to save it into the requirements.txt, use the
following command:

"pip freeze > requirements.txt"