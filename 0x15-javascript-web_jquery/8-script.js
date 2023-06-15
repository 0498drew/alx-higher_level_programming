$(document).ready(function() {
  $('#list_movies').click(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      var movies = data.results;
      var movieList = $('#list_movies');
      movieList.empty(); // Clear any existing list items

      $.each(movies, function(index, movie) {
        var listItem = $('<li>').text(movie.title);
        movieList.append(listItem);
      });
    });
  });
});

