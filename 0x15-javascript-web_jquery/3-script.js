/* Script that adds the class red to the <header> 
element when the user clicks on the tag DIV#red_header */
$(document).ready(function () {
	const divRedHeader = $("div#red_header");
	divRedHeader.click(function () {
		$("header").addClass("red");
	});
});
