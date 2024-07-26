// Selects the element with id "update_header"
const update_the_header = document.getElementById('update_header');

// Adds the click event
update_the_header.addEventListener('click', function() {
    // Selects the header elemnt
    const header = document.querySelector('header');
    // Updates the text content
    header.textContent = 'New Header!!!';

});
