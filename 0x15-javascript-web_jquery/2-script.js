/* Script that updates the text color of the <header> element to red 
(#FF0000) when the user clicks on the tag DIV#red_header */
$(document).ready(function () {
	const divRedHeader = $("div#red_header");
	divRedHeader.click(function () {
		divRedHeader.css("color", "#FF0000");
	});
});
