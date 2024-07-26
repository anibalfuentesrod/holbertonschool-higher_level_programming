// Selects elemend with ID "red_header"
const header_red = document.getElementById('red_header')

// Here i add a click events listener to the element
header_red.addEventListener('click', function() {
    // Selects the header elements
    const header = document.querySelector('header')
    // Change the color of text of the header
    header.style.color = '#FF0000'
});
