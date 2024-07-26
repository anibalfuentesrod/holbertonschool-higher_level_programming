// Selects the element with id "add_item"
const add_ittem = document.getElementById('add_item');

// Adds a click events listener to the element(add_item)
add_ittem.addEventListener('click', function() {
    // Creates a new 'li' ement
    const new_item = document.createElement('li');
    // Sets the text content of the new 'li' element
    new_item.textContent = 'Item';
    //Select the 'ul' element with class "my_list"
    const my_list = document.querySelector('.my_list');
    // Appends the new 'li' element to the 'ul' elementt
    my_list.appendChild(new_item);
});
