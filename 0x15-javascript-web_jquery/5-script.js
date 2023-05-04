/* Script that adds a <li> element to a list when 
the user clicks on the tag DIV#add_item: */
$(document).ready(function () {
	const divAddItem = $("div#add_item");
	$(divAddItem).click(function () {
		$(".my_list").append("<li>Item</li>");
	});
});
