## Repo structure

![Project Structure](../static/images/image1.png)

_**index.html**_ is the first and main rendered page of the UI. When the user visite the application home page, the Flask application renders this page first.
It uses a simple HTML form to take the input movie from the user and submit to the backend.

_**negative.html**_ is rendered if the input from the user does not match with all_titles list which contains all the movie names present in the database.
_**Negative.html**_ page simply shows possible reason(s) for not able to find the searched movie. It also searches throughout the whole database and makes use of similar word search techniques(difflib.get_close_matches() method in python & Levenshtein distance method ) to find the closest match and suggests the user about the movie names which are very similar to the one user entered. All this is done using javascript and finally rendered on the HTML page.

_**positive.html**_ is rendered if the input movie name matches with the database. If so, we call the get_recommendations function by passing the movie name. The get_recommendations function is the same as we have discussed in section 2. We take the movie name, calculate the cosine matrix with respect to the dataset and find the most similar movie to the input movie. We sort the results and return back top 10 results. We send similar movie names as well as their release date in a list to the _**positive.html**_. We create a tabular layout and print the 10 movies along with their release dates.