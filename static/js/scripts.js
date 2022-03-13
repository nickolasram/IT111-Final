$('#signup').click(function(e){
      $('#loginform').removeClass("hidden");
      $('#signupform').addClass("hidden");
      e.preventDefault()
  });

$('#login').click(function(e){
      $('#signupform').removeClass("hidden");
      $('#loginform').addClass("hidden");
      e.preventDefault()
  });

$('.uploadbutton').click(function(e){
      $('.uploadwrapper').removeClass("hidden");
      e.preventDefault()
  });

$('.close').click(function(e){
      $('.uploadwrapper').addClass("hidden");
      e.preventDefault()
  });

 $("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});