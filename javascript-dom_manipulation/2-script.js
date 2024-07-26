// THis part selects the element with ID "red_header"
const header_red = document.getElementById('red_header');

// ADDS a click event listener to the element
header_red.addEventListener('click', function() {
    // Selects the header element
    const header = document.querySelector('header')
    // Adds the class "red" to the header element
    header.classList.add('red')
});
