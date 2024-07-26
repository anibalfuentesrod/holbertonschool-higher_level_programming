// Url for fetching
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

// Fetch the transaltion from api
fetch(url)
  .then(response => response.json()) //Converts to json
  .then(data => {
    // select the element with id "hello"
    const hello_id = document.getElementById('hello');
    // Updates the text content of the elemtn with the transaltion "hello"
    hello_id.textContent = data.hello;
  })
  .catch(error => {
    console.error('Error;', error);
  });
