# POV
POV is an app that a user can search a term or topic and is then returned with data from the general public on that search. For example a user may want to search the
term "Liverpool" to see what other people think about the club after they lose match.

This data includes:
- Positive rating percentage
- User comments
- Statitics on the data
- Word bubble of the most commonly used words

The project was split into two parts, the backend and the frontend.

## Backend
- A python flask server that hosts the four python classes to parse the data recieved from the external endpoints. The twitter and reddit classes search for posts about
the search term and then use the sentiment analysis library "Vader" to get the positive, negative and neutral values on each user post. The amazon and imdb classes
use the built in user rating values to get the positive rating of the search term. The frontend makes an API connection to the backend server and passes the 
search term and category via the url.

## Frontend
- This is made using react native (expo). We have a navigation controller made using a “stack” and this is used to show at which screen in the app the user is at. 
It displays the home screen by default.  
- The home screen is made up of several components. There is the app’s title at the top of the screen. Below that is a search bar with a pressable search icon. 
Below that is a trending carousel. Each card on this carousel is a search term that is considered trending by us. A user may swipe on a card to go to the 
next one or they can click on a card to search it. When a user searches something in the search bar a category pop up will appear on their screen. 
Here the user must select the category most relevant to their search term. For example, a search for Liverpool would have much different results in the 
Sports category versus Travel. Once selected the navigation controller will push the results screen onto the stack.
-Once the results screen will parse the results received by the backend server. A results wheel is the first component and this fills to whatever percentage 
of a positive rating the search term had. There are two boxes that display user comments about the search term. Below that will also be other relevant information 
about the search term. At the top of the screen there is a pressable home icon. When pressed the navigation controller will pop the results screen of the stack 
and the home screen will disappear. 
- If the search term does not return any data from our backend server an error screen will be pushed onto the navigation stack and a user can return to the 
home screen if they would like to do so. 

# Using this code

## Backend
The backend server is hosted on python anywhere. However you can run it as a local host for personal use. Set backend as a current directory and create a virtual
enviroment. Then run the commmand `pip install -r requirments.txt`. You must also download to nlkt libraries. To get these libraries run the commands
```
python -m nltk.downloader stopwords
python -m nltk.downloader sentiment.vader
```
Once installed, run the python file flask_app.py in the Server directory.

## Frontend
You must install the most recent versions of Node.js and npm. Once installed set Frontend as current directory and run the command `npm install`. Once that is complete
you can run the command `npm start`. You can now run the app on the expo app or on an android simulator.

