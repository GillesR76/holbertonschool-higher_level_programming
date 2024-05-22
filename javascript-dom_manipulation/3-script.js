const element = document.getElementById('toggle_header');
element.addEventListener('click', () => {
  if (element.classList.contains('red')) {
    element.classList.replace('red', 'green');
  } else {
    element.classList.replace('green', 'red');
  }
});
