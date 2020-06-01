# README
In this repository you can find all the files that I used for deploying a web app for crack concrete recognition. I used Flask for deploying and Heroku for hosting. Here is the link: https://crack-concrete-recognition.herokuapp.com/

## 1. Notebook
Here you find all the commands with comment for understanding. Data are public and so they are downloaded through the notebook. I developed a CNN using a pre-trained ResNet50 and I added an on top layer for fine tuning. The trained model, since it is to big for GitHub, can be downloaded at the following [link](https://1drv.ms/u/s!Am0EsyigtYzaiepTJ_aZu5I8teIzww?e=bufW4D).

## 2. App file
The following python script has the line of code for deploying the model, using the Flask framework.

## 3. Support files
For deploying a web-application on Heroku (and on others PaaS providers), some supporting files are needed. In summary:
- `runtime.txt` contains the python version to be used for deploying
- `requirements.txt` contains the required libraries to be used for executing the script
- `Procfile` is needed for Heroku and specifies the commands that are executed by the app on startup. In our case it will execute `app.py` script.

## 4. Tutorial for use
For using the web-app, you need to go to the following link, search for a concrete image, paste the link in the search bar and it give you an answer on if there is or not a crack in the pic you gave. At the moment is only possible use online picture, but I'm working on using also loading local pictures.

I provide you a youtube video where I recorder the procedure..

[![IMAGE ALT TEXT](http://img.youtube.com/vi/nXA1KXNK9DE/0.jpg)](http://www.youtube.com/watch?v=nXA1KXNK9DE "Concrete Crack Recognition")

## Thanks
Thanks for visiting my repository. For any feedback you can contact me at luca.riccardi@live.it.
