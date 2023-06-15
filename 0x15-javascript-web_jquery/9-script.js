$(function() {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function() {
      $('#hello').text('An error occurred');
    }
  });
});

