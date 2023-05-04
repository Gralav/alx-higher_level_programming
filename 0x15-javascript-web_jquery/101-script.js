/*JavaScript script that adds, removes and clears 
LI elements from a list when the user clicks */
$(document).ready(function () {
	$("DOMContentLoaded", function () {
		const mylist = $(".my_list");
		const addingLi = "<li>Item</li>";
		$("#add_item").click(function () {
			mylist.append(addingLi);
		});
		$("#remove_item").click(function () {
			$("ul.my_list li:last-child").remove();
		});
		$("#clear_list").click(function () {
			$(mylist).empty();
		});
	});
});
