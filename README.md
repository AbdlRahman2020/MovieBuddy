# Movie Buddy

### Live application [here](https://movie-buddyy.herokuapp.com)

### [Project Wiki](https://github.com/AbdlRahman2020/MovieBuddy/wiki/Project-Wiki)

## Motivation
We all have this friend that has watched so many movies and we would go to in case we would like to get a movie recommendation.
The problem is when this friend's taste doesn't match our taste. This is the motivation behind Movie Buddy application. 
Movie Buddy uses Machine Learning to suggest a list of movies to the user based on their last watched/ preferred movie. 
For example, if your favorite movie is Inception, the recommender is going to go through the Kaggle movie data set and figure out 
some other movies you might like to watch based on many factors such as Director, User Ratings, Genre, Actors, etc.


## Installation 📦

``` shell
$ pip install -r requirements.txt
``` 

#### Clone

- Clone this repo to your local machine.

#### Run server locally

```shell
$ falsk run
```
> Go to localhost:5000

---

## OVERVIEW

### Features 📋
* User can enter the name of a movie of preference.
* The system will generate a list of movie recommendations based on a content based ML model.
* User can view a list of 10 recommended movies based on their preferred movie.
---

#### Project Architecture
The Projects consists of 3 main components:
1. Frontend: mainly HTML, CSS & Javascript. 
2. Backend: Flask application exposing a ML model API for giving recommendations.
3. ML model: in python and uses movies dataset from kaggle, Pandas library, 

#### Directory Setup

The project consists mainly of:
* Model repo: contains tmdb.cv, movies dataset obtained from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).
* Templates repository: Holds all the main application HTML files.
   1. index.html
    2. positive.html
     3. negative.html 

* Static repository: Holds the .css styling sheets. 
* app.py: Main python file for running the Flask application.

![Project Structure](./static/images/image1.png)

### Functionality

The webpage takes into consideration simple UI/UX requirements. 
We tried to design it so that it looks very simple yet informative enough for everyone to understand. 

We provide the main input field inside a form where the user input’s the movie name and the form is submitted by the action of the button. Upon submission, the movie name is captured at the backend and further processed. We also provide good effects on the div and other CSS properties so that the UI looks eye friendly and easy to use.

First we have created the index.html web page. It contains the main UI for the application where the user can input their favorite movie's name.
We connected index.html to the flask. The page is rendered when the application is initially opened. 

So let’s jump to the basics of the flask web application framework to render it for the user.

We use the following code in app.py to simply render the page we just created.

``` python
import flaskapp = flask.Flask(__name__, template_folder=’templates’)# Set up the main route
@app.route(‘/’, methods=[‘GET’, ‘POST’])def main():
    if flask.request.method == ‘GET’:
        return(flask.render_template(‘index.html’))
```
Now that we have our index.html rendered, We prompt the user to enter their favorite movie's name.
For this part we are using a standard HTML form where it takes the user's input and sends it to the backend.
Upon entering, the user clicks on the submit button and the form is submitted.

Once we have a movie name, which is submitted by the user in the form. Let’s hold this name into the m_name variable in python. 
We accept the form submission using the post method.

``` python
if flask.request.method == ‘POST’:
    m_name = flask.request.form[‘movie_name’]
    m_name = m_name.title()
```
We also convert the input movie name to the title format. The title form will simply convert every character of each word to upper case. Now we have 2 options:

1. If the input movie name is misspelled or does not exist in the database then show error page & possible similar movie name based on the input.
2. If a correct movie name is entered & present in the database, then show the recommendations.

The code below is responsible for doing this:

``` python
if m_name not in all_titles:
   return(flask.render_template(‘negative.html’,name=m_name))
else:
   result_final = get_recommendations(m_name)
   names = []
   dates = []
   for i in range(len(result_final)):
      names.append(result_final.iloc[i][0])
      dates.append(result_final.iloc[i][1])   
   return flask.render_template(‘positive.html’,movie_names=names,movie_date=dates,search_name=m_name)
```

Let’s carefully look into positive.html & negative.html.

_**negative.html**_ is rendered if the input from the user does not match with all_titles list which contains all the movie names present in the database.
_**Negative.html**_ page simply shows possible reason(s) for not able to find the searched movie. It also searches throughout the whole database and makes use of similar word search techniques(difflib.get_close_matches() method in python & Levenshtein distance method ) to find the closest match and suggests the user about the movie names which are very similar to the one user entered. All this is done using javascript and finally rendered on the HTML page.

_**positive.html**_ is rendered if the input movie name matches with the database. If so, we call the get_recommendations function by passing the movie name. The get_recommendations function is the same as we have discussed in section 2. We take the movie name, calculate the cosine matrix with respect to the dataset and find the most similar movie to the input movie. We sort the results and return back top 10 results. We send similar movie names as well as their release date in a list to the _**positive.html**_. We create a tabular layout and print the 10 movies along with their release dates.

### Algorithm
##### Content Based Recommendations (Recommender Algorithm)
* To build our model, we created a count matrix that is created by the help of a count vectorizer.
* We used cosine similarity from scikit-learn to determine how similar the movies are, regardless of the size.
* After building the cosine similarity matrix for our dataset, we can now sort the results to find out the top 10 similar movies.
* We return the movie title & indexes to the user.
