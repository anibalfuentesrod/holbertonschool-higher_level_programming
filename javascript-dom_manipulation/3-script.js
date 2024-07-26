// Select the element with 'id' "toggle_header"
const tog_header = document.getElementById('toggle_header')

// Add a click event listener to the element
tog_header.addEventListener('click', function() {
    // Selects the element header
    const header = document.querySelector('header')
    // Toggle the class betwen 'red' and 'gree'
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});