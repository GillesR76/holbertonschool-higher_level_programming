const element = document.getElementById('update_header');
element.addEventListener('click', () => {
  const headerText = document.querySelector('header')
  headerText.textContent = 'New Header!!!';
});
