document.addEventListener("DOMContentLoaded", function () {

  document.getElementById("subscribe-form").addEventListener("submit", function (event) {
    
    const emailInfo = document.getElementById("subscribe-form-0-email").value;
    if (emailInfo === "") return;


    const spinner = document.getElementById("subscribe-spinner");
    spinner.classList.remove("hidden");
    event.preventDefault();
    fetch("/api/subscriptions/", {
      method: "POST",
      body: JSON.stringify({ email: emailInfo }),
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json", // Set correct content type
        "X-CSRFToken": getCSRFToken(),
      },
    })
      .then((response) => {
        if (response.ok) {
          this.reset();
          spinner.classList.add("hidden");
          const successMessage = document.getElementById(
            "success-message"
          );
          successMessage.classList.remove("hidden");
          setTimeout(() => {
            successMessage.classList.add("hidden");
          }, 5000);
        } else {
          spinner.classList.add("hidden");
          const errorMessage = document.getElementById(
            "error-message"
          );
          errorMessage.classList.remove("hidden");
          setTimeout(() => {
            errorMessage.classList.add("hidden");
          }, 5000);
          
          console.error("Error:", response.statusText);

        }
      })
      .catch((error) => {
        spinner.classList.add("hidden");
        console.error("Error:", error);
      });
  });
});

function closeSuccessNotification() {
  document.getElementById("success-message").classList.add("hidden");
}

function closeErrorNotification() {
  document.getElementById("error-message").classList.add("hidden");
}

function getCSRFToken() {
  let cookieValue = null;
  let cookies = document.cookie.split(';');

  cookies.forEach(cookie => {
      let trimmedCookie = cookie.trim();
      if (trimmedCookie.startsWith('csrftoken=')) {
          cookieValue = trimmedCookie.split('=')[1];
      }
  });

  return cookieValue;
}