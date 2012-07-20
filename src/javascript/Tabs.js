function tabsSetup() {
	$( "#tabs" ).tabs();
    var $items = $('#vtab>ul>li');
    $items.click(function() {
		$items.removeClass('selected');
		$(this).addClass('selected');
	
		var index = $items.index($(this));
		$('#vtab>div').hide().eq(index).show();
    }).eq(1).click();
}