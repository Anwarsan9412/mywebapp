// $(window).scroll(function () {
//   var scroll = $(window).scrollTop();

//   document.getElementById("myBody").style.marginTop =
//     200 - 0.5 * scroll + "px";

// //   if (scroll >= 100) {
// //     $("#myBody").addClass('position','fixed').css('top','0');
// //   } else {
// //     $("#myBody").removeClass('position','fixed').css('top','0');
// //   }
// });

var elementPosition = $('.col-sm sticky-top').offset();

$(window).scroll(function(){
        if($(window).scrollTop() > elementPosition.top){
              $('.col-sm sticky-top').css('position','fixed').css('top','0').css('class','col-sm sticky-top');
        } else {
            $('.col-sm sticky-top').css('position','static');
        }    
});


// document.getElementById('basicAlert').addEventListener('click', function () {
//     Swal.fire(
//         'Basic alert',
//         'You clicked the button!'
//     )
// });
