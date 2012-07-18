$(function() {
		var folders = [
				"abc",
				"def"
		];
		
		$( "#folder" ).autocomplete({
			source: function(req, add){
			
				xmlhttp=new XMLHttpRequest();
				xmlhttp.onreadystatechange=function()
			    {
			        if (xmlhttp.readyState==4 && xmlhttp.status==200)
			        {
			        	var suggestions = jQuery.parseJSON(xmlhttp.responseText);
			        	add(suggestions)
			        }
		        }
		        
		        xmlhttp.open("GET","/GetJSONMatchingPaths?initialPath=" + req.term, true);
				xmlhttp.send();
			}
		,
		
			select: function(event, ui) {
				$("#folder").val(ui.item.value);
				$("#folder").submit();
				
				xmlhttp=new XMLHttpRequest();
				xmlhttp.onreadystatechange=function()
			    {
			        if (xmlhttp.readyState==4 && xmlhttp.status==200)
			        {
			        	var suggestions = jQuery.parseJSON(xmlhttp.responseText);
			        	var folders = suggestions[0];
			        	var exception = suggestions[1];
			        	if(exception.length == 0)
			        		msg = "";
		        		else
		        			msg = "An error happened: " + exception;
			        	
			        	document.getElementById("exception").innerHTML = msg;
			    		
			    		foldersHTML = ""
			    		jQuery.each(folders, function(i, l) {
			    			foldersHTML = foldersHTML + "<br/>" + l;
			    		})
			    		
			    		document.getElementById("folders").innerHTML = foldersHTML;
			        	//add(suggestions)
			        }
		        }
		        
		        xmlhttp.open("GET","/JSONInputFolder?folder=" + ui.item.value + "&pattern=.*", true);
				xmlhttp.send();
			}
		});
		
		$( "#pattern" ).autocomplete({
			source: function(req, add){
				add(req.term);
			},
			select: function(event, ui) {
				$("#pattern").val(ui.item.value);
				$("#pattern").submit();
				
				xmlhttp=new XMLHttpRequest();
				xmlhttp.onreadystatechange=function()
			    {
			        if (xmlhttp.readyState==4 && xmlhttp.status==200)
			        {
			        	var suggestions = jQuery.parseJSON(xmlhttp.responseText);
			        	var folders = suggestions[0];
			        	var exception = suggestions[1];
			        	if(exception.length == 0)
			        		msg = "";
		        		else
		        			msg = "An error happened: " + exception;
			        	
			        	document.getElementById("exception").innerHTML = msg;
			    		
			    		foldersHTML = ""
			    		jQuery.each(folders, function(i, l) {
			    			foldersHTML = foldersHTML + "<br/>" + l;
			    		})
			    		
			    		document.getElementById("pattern").innerHTML = foldersHTML;
			        	//add(suggestions)
			        }
		        }
		        
		        xmlhttp.open("GET","/JSONInputFolder?folder=" + $("#folder").val() + "&pattern=" + ui.item.value, true);
				xmlhttp.send();
			}
		});
	});
$(function() {
	$( "#tabs" ).tabs();
});

var $items = $('#vtab>ul>li');
$items.mouseover(function() {
    $items.removeClass('selected');
    $(this).addClass('selected');

    var index = $items.index($(this));
    $('#vtab>div').hide().eq(index).show();
}).eq(1).mouseover();