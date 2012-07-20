var movies = [];
var moviesRoot = "";
var pattern = "";

$(function() {
		initMovies();
		
		folderAutocomplete();
		patternAutocomplete();
		tabsSetup();
		mouseSetup();
		buttonsSetup();
	});