function initMovies() {
	for (i = 0; i < letters.length; ++i)
	{
		movies[letters[i]] = [];
	}
}
function RefreshMovies(){
	$.ajax({
		url: "/JSONInputFolder?folder=" + moviesRoot + "&pattern=" + pattern,
		cache: true
	}).done(function(response){
		var suggestions = jQuery.parseJSON(response);
    	var moviefolders = suggestions[0];
    	var exception = suggestions[1];
    	if(exception.length == 0)
    		msg = "";
		else
			msg = "An error happened: " + exception;
    	
    	initMovies();
    	
    	document.getElementById("exception").innerHTML = msg;
    	jQuery.each(moviefolders, function(i, movieFolder) {
    		
    		var letter = undefined;
    		var upperMovieFolder = movieFolder.toUpperCase();
    		
    		for(i = 0; i < upperMovieFolder.length; ++i)
			{
    			if(upperMovieFolder[i].match(/[A-Z]/))
			    {
    				letter = upperMovieFolder[i];
    				break;
		        }
    			else if(upperMovieFolder[i].match(/[0-9]/))
    			{
    				letter = "num";
    				break;
    			}
			}
    		
    		if (letter == undefined)
			{
    			letter = "num";
			}
    		
			movies[letter].push(movieFolder);
			movies["All"].push(movieFolder);
		});
    	
    	
    	for(i = 0; i < letters.length; ++i)
		{
    		//$("div#movies-" + letters).text =
    		var letter = letters[i];
    		var id = "movies-" + letter;
    		
    		var moviesList = "";
    		
    		jQuery.each(movies[letter], function(i, movie) {
    			moviesList = moviesList + "<br/>" + movie;
    		})
    		
    		
    		document.getElementById(id).innerHTML = moviesList;
		}
	});
}