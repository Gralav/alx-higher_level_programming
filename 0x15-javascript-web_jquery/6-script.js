/* Script that updates the text of the <header> element to 
New Header!!! when the user clicks on DIV#update_header */
$(document).ready(function () {
	const divUpdateHeader = $("div#update_header");
	$(divUpdateHeader).click(function () {
		$(divUpdateHeader).text("New Header!!!");
	});
});
