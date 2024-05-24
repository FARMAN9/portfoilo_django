/**
* PHP Email Form Validation - v3.7
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function (e) {
    e.addEventListener('submit', function (event) {
      event.preventDefault();

      let thisForm = this;
      let action = thisForm.getAttribute('action');
      
      thisForm.querySelector('.loading').style.display = 'block';
      thisForm.querySelector('.error-message').style.display = 'none';
      thisForm.querySelector('.sent-message').style.display = 'none';

      let formData = new FormData(thisForm);

      fetch(action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': thisForm.querySelector('[name=csrfmiddlewaretoken]').value
        }
      })
      .then(response => {
        thisForm.querySelector('.loading').style.display = 'none';
        if (response.ok) {
          return response.json();
        } else {
          throw new Error(`${response.status} ${response.statusText} ${response.url}`);
        }
      })
      .then(data => {
        if (data.status === 'OK') {
          thisForm.querySelector('.sent-message').style.display = 'block';
          thisForm.reset();
        } else {
          let errorMessage = thisForm.querySelector('.error-message');
          errorMessage.style.display = 'block';
          errorMessage.innerHTML = data.errors ? JSON.stringify(data.errors) : 'Form submission failed.';
        }
      })
      .catch((error) => {
        let errorMessage = thisForm.querySelector('.error-message');
        errorMessage.style.display = 'block';
        errorMessage.innerText = error;
      });
    });
  });

})();