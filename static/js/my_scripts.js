$(document).ready(function(){
	$('#dialog_topic').dialog({
		autoOpen: false,
		modal: true		
	}); // окончание dialog

	$('.topic').click(function(evt) {
		evt.preventDefault();
		$('#dialog_topic').dialog('open');
	}); // окончание click
}); // окончание ready