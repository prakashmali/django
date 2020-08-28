(function($) {
  "use strict"; // Start of use strict

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
    
    // Toggle the side navigation when window is resized below 480px
    if ($(window).width() < 480 && !$(".sidebar").hasClass("toggled")) {
      $("body").addClass("sidebar-toggled");
      $(".sidebar").addClass("toggled");
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });



//   $("#edit").click(function(e) {
//     $.ajax({
//       type:'POST',
//       url: '/edit/{{ obj.id }}/',
//       data:{
//         csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
          
//   },
//   datatype:'json',
//   success: function(response){
//     if(response.success==true){
//       console.log('redirecting')
//       window.location.replace("verification?mobile=" + response.mobile);
//     }
//     else{

//     }

//  }             
//  });
//   });



})(jQuery); // End of use strict

$( document ).ready(function() {
  var cart={}

$(".cart").click(function(){
           
  var id=this.id.toString()
  if(cart[id]!=undefined){
    cart[id]=cart[id]+1;
    $("#p"+id).html(cart[id]);

  }else{
    cart[id]=1
    $("#p"+id).html(cart[id]);
  }
     });

     $("#submit").click(function(e){
      
      e.preventDefault()
      var res_id=$("input[name=res_id]").val();
      cart['res_id']=res_id;
      console.log(cart)
      cart['csrfmiddlewaretoken']=$('input[name=csrfmiddlewaretoken]').val();
      console.log(cart)
      $.ajax({
        type:'POST',
        url: '/dises/billdata/',
        
        data:cart,
    datatype:'json',
    success: function(response){
        console.log(response)
        var i=1;
        var total=0;
        $('.cart').prop('disabled', true);
        $('#submit').prop('disabled', true);
        $('#rest').css("display", "block");
        for (let key in response) {
          // document.getElementById("Content").innerHTML += "<tr><td>"+key+"</td><td>"+response[key][0]+"</td><td>"+response[key][1]+"</td><td>"+response[key][0]*response[key][1]+"</td></tr>";

          var rows = "";
        
            rows += "<tr><td>" + i + "</td><td>" + key + "</td><td>" + response[key][1] + "</td><td>" + response[key][0] + "</td><td>" + response[key][0]*response[key][1] + "</td></tr>";
            i+=1;
            total+=response[key][0]*response[key][1];
          $( rows ).appendTo( "#itemList tbody" );

        }
        document.getElementById("total").innerHTML +=total;
        
        
        
        }             
        });



     });
     var doc = new jsPDF();
      var specialElementHandlers = {
          '#editor': function (element, renderer) {
              return true;
          }
      };
      $('#pdf').click(function () {
        doc.fromHTML($('#Content').html(), 15, 15, {
            'width': 170,
                'elementHandlers': specialElementHandlers
        });
        doc.save('invoice.pdf');
    });

});


