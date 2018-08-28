$(document).ready(function(){
	$('#dialog_topic').dialog({
		autoOpen: false,
		modal: true		
	}); // окончание dialog

	$('.block_topic').on('click', '.topic', function(evt) {
		evt.preventDefault();
		// var topic_href = $('.topic a').attr('href');
		var topic_href = evt.target;
		// topic_href = topic_href.slice(21);
		$('#dialog_topic p').text(topic_href);
		$('#dialog_topic').dialog('open');
	}); // окончание on_click
}); // окончание ready