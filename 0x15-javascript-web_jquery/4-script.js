/* Script that toggles the class of the <header> 
element when the user clicks on the tag DIV#toggle_header */
$(document).ready(function () {
	const divToggle_Header = $("div#toggle_header");
	$(divToggle_Header).click(function () {
		$("header").toggleClass("red green");
	});
});
