$(function() {

	$('.push-form').on('submit', function(res) {
		var data = {
			'csrfmiddlewaretoken' : window.CSRF_TOKEN,
			'action'              : $(this).data('action'),
		};
		$.post('/templates/gener_push',data, function(response) {
			console.log(response);
		});
		return false;
	});

});