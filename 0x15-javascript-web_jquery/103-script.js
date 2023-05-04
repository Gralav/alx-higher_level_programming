/*JavaScript script that fetches and prints 
how to say “Hello” depending on the language */

$(document).ready(function () {
	$("DOMContentLoaded", function () {
		const translate = function () {
			const languaje_code = $("#language_code").val();
			const url = "https://fourtonfish.com/hellosalut/?lang=" + languaje_code;
			$.getJSON(url, function (data) {
				$("#hello").text(data.hello);
			});
		};
		$("#language_code").keypress(function (event) {
			const keycode = event.keyCode ? event.keyCode : event.which;
			if (keycode == "13") {
				translate();
			}
		});

		$("#btn_translate").click(function () {
			translate();
		});
	});
});
