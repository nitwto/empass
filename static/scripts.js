var idleTime = 0;

$(document).ready(function() {

	var idleInterval = setInterval(timerIncrement, 60000);

	$(this).mousemove(function(e) {
		idleTime = 0;
	});

	$(this).mousemove(function(e) {
		idleTime = 0;
	});
});

function timerIncrement() {
	idleTime += 1;

	console.log(idleTime);
	if(idleTime > 14) {
		alert("Session timed out. Login again.");

		window.location = '/register';
	}
} 