
    alert('RUNNING');


$('button').click(function(){
    $('#main').attr("src", "images/brolly_shirt.png");
    alert('tyring again')}); 


$('#1').click(function(){
    $(this).attr("src", "images/brolly_shirt_0-0.jpeg")});               

$('#2').click(function(){
    $(this).attr("src", "images/brolly_shirt_1-0.jpeg")});

$('#3').click(function(){
    $(this).attr("src", "images/brolly_shirt_2-0.jpeg")});

$('#4').click(function(){
    $(this).attr("src", "images/brolly_shirt_3-0.jpeg")});

$('#5').click(function(){
    $(this).attr("src", "images/brolly_shirt_4-0.jpeg")});

$('#revert').click(function(){
    $('#1').attr("src", "images/brolly_0-0.jpeg");
    $('#2').attr("src", "images/brolly_1-0.jpeg");
    $('#3').attr("src", "images/brolly_2-0.jpeg");
    $('#4').attr("src", "images/brolly_3-0.jpeg");
    $('#5').attr("src", "images/brolly_4-0.jpeg");     
})

