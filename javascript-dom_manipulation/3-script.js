#!/usr/bin/node

function change () {
  const title = document.getElementById('toggle_header');
  if (title.className === 'red') {
    title.className = 'green';
  } else {
    title.className = 'red';
  }
}
change();
