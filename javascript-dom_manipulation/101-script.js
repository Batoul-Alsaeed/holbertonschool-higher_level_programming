document.addEventListener('DOMContentLoaded', function () {
  const btn = document.querySelector('#btn_translate');
  const select = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  btn.addEventListener('click', function () {
    const lang = select.value;
    if (!lang) return; // تجاهل لو ما تم اختيار لغة

    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        helloDiv.textContent = 'Translation error!';
        console.error(error);
      });
  });
});
