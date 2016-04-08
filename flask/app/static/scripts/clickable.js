
jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.document.location = $(this).data("href");
    });
});

// $(document).ready(function(){
//     $('.clickable-row').click(function(){
//     	href = $('.clickable-row' :first-child).text()
//         window.location = $(this).firstChild.('text');
//         return false;
//     });
// });