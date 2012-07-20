function folderAutocomplete()
{
	$( "#folder" ).autocomplete({
		source: function(req, add){
			$.ajax({
				url: "/GetJSONMatchingPaths?initialPath=" + req.term,
				cache: true
			}).done(function(response) {
				add(jQuery.parseJSON(response));
			});
		}
	,
	
		select: function(event, ui) {
			$("#folder").val(ui.item.value);
			$("#folder").submit();
			moviesRoot = ui.item.value;
			RefreshMovies();
		}
	});
}

function patternAutocomplete(){
	$( "#pattern" ).autocomplete({
		source: function(req, add){
			add(req.term);
		},
		select: function(event, ui) {
			$("#pattern").val(ui.item.value);
			$("#pattern").submit();
			
			pattern = ui.item.value;
			RefreshMovies();
        }
	});
}