# Bechdel Test Score and Gender Distribution in Recent Movies
* This project takes movie information from IMDB, TMDb API, and Bechdel test to help analzye the gender distribution in recent major movies. Information such as the Bechdel test score, the % female in the cast, etc is analzyed and displayed in a minimal interaction Flask app (inside the flask folder)

# Content
* flask folder : contains the flask application MovieInfo
* base folder: contains some csv files, json files, and the jupyter notebooks used to analyze the data.
    * not all the data contained is included in the file
    * jupyter notebooks:
        * Parsing and converting json files from The Movie Database API to dataframe.ipynb
        * Combining and analyzing people information.ipynb
        * csv to sqlite3 files.ipynb
        * IMDB database - combining tables.ipynb
        * Bechdel Test - EDA.ipynb
        * Bechdel Test - obtaining the data from the API.ipynb

# Flask app MovieInfo:
* setup.py - contains information about the app
* movieinfo folder - the main Flask app folder
* movieinfo.sqlite - SQLite database containing information about the movies and cast