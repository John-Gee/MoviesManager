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
	});		