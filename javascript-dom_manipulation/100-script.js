document.addEventListener('DOMContentLoaded', function () {
  const addBtn = document.querySelector('#add_item');
  const removeBtn = document.querySelector('#remove_item');
  const clearBtn = document.querySelector('#clear_list');
  const ul = document.querySelector('.my_list');

  addBtn.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });

  removeBtn.addEventListener('click', function () {
    if (ul.lastElementChild) {
      ul.removeChild(ul.lastElementChild);
    }
  });

  clearBtn.addEventListener('click', function () {
    ul.innerHTML = '';
  });
});
