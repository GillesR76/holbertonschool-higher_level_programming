const element = document.getElementById('add_item');
element.addEventListener('click', () => {
  const newListItem = document.createElement('li');
  newListItem.innerHTML = 'Item';
  document.querySelector('.my_list').append(newListItem);
});
