$( document ).ready(function () {    
    $('.btn').on('click', function () {
        var usernameValue = document.getElementById('username').value
        var pwValue = document.getElementById('password').value

        if (usernameValue == "seanandrisham" && pwValue == "hackmitproject") {
            window.open('home.html', '_self'); 
        } else {
            $('.message').addClass('alert alert-danger');
            $('.message').text("Incorrect username or password");
        }
    });
}); 