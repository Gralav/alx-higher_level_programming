/* script that fetches and lists the title for all movies 
by using this URL: https://swapi-api.hbtn.io/api/films/?format=json */
$(document).ready(function () {
	$.getJSON(
		"https://swapi-api.hbtn.io/api/films/?format=json",
		function (data) {
			data.results.forEach((movie) => {
				$("ul#list_movies").append(`<li>${movie.title}</li>`);
			});
		}
	);
});
