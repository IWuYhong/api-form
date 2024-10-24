document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
      .then(function() {
          alert('Email sent successfully!');
      }, function(error) {
          alert('Failed to send email: ' + JSON.stringify(error));
      });
});
