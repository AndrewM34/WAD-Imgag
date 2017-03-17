// activate and deactivate search field
function searchToggle(obj, evt) {
	var container = $(obj).closest('.search-wrapper');

	// if search is not active -> activate it
	if (!container.hasClass('active')) {
		container.addClass('active');
		// set cursor to search field
		container.find('.search-input').select();
		evt.preventDefault();
	}
	else if (container.hasClass('active') && $(obj).closest('.input-holder').length == 0) {
		container.removeClass('active');
		// clear input
		container.find('.search-input').val('');
		// clear and hide result container when we press close
		container.find('.result-container').fadeOut(100, function() {
			$(this).empty();
		});
	}
}
// do search
function submitFn(obj, evt) {
	// get the search string
	value = $(obj).find('.search-input').val();
	url = $(obj).attr('succeedurl');

	_html = "";
	var check = value.trim();
	value = value.replace(/\s+/g, '_');
	// check if the search is empty
	if (!check.length) {
		_html = "Bro, you try to search nothing?";
		$(obj).find('.result-container').html('<span>' + _html + '</span>');
		$(obj).find('.result-container').fadeIn(100);
		$(obj).find('.search-input').val("");
		$(obj).find('.search-input').attr("placeholder", "Type to search");
	}
	// otherwise go to search with value of the string
	else {
		window.location = url + value;
	}
	$(obj).find('.result-container').fadeIn(100);
	evt.preventDefault();
}