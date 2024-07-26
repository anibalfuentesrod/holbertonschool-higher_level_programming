// URL of star wars
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Fetch the films data from api
fetch(url)
  .then(response => response.json()) // converts to json
  .then(data => {
    // Selects the 'ul' element  with id "list_movies"
    const list_of_movies = document.getElementById('list_movies');
    // Create through each filsm in the data
    data.results.forEach(film => {
        // creates a new 'li' element for each film
        const listItem = document.createElement('li');
        // Set the text conten of the 'li' element to the filsm's title
        listItem.textContent = film.title;
        // Appends the 'li' to the 'ul' elelment
        list_of_movies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
