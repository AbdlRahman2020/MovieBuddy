# Movie Buddy

## Installation 📦

>pip install -r requirements.txt

#### Clone

- Clone this repo to your local machine.

#### Run server locally

```shell
$ falsk run
```
> Go to localhost:5000

---
## Features 📋
* User can enter the name of a movie of preference.
* The system will generate a list of movie recommendations based on a content based ML model.
* User can view a list of 10 recommended movies based on their preferred movie.
---

## Algorithm
##### Content Based Recommendations (Recommender Algorithm)
* To build our model, we created a count matrix that is created by the hlp of a count vectorizer.
* We used cosine similarity from scikit-learn to determine how similar the movies are, regardless of the size.
* After building the cosine similarity matrix for our dataset, we can now sort the results to find out the top 10 similar movies.
* We return the movie title & indexes to the user.

