document.querySelector("#form").addEventListener("submit", submitFun);
function openForm() {
    document.getElementById("popup").style.display = "block";
  }
function submitFun(elme) {
    elme.preventDefault();
    username = document.querySelector("#name").value;
    password =  document.querySelector("#password").value;

    if (username == "harsh@gmail.com" && password == "123") {

        window.location.href = "index.html";
    } else {
        alert("Invalid username or password");
        document.querySelector("#form").reset();
    }

}
