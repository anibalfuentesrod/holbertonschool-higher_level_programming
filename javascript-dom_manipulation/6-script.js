// URL of Star wars API for the specific character
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Fetch the character data form the api
fetch(url)
   .then(response => response.json()) // this converts the response to json
   .then(data => {
    // Select the element with the id of "character"
    const characterDiv = document.getElementById('character');
    // Updates the text content of the element with the character's name
    characterDiv.textContent = data.name
   })
   .catch(error => {
    console.error('Error:', error);
   });
