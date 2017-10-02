/*Contact Card Exercise Using From and "return false" to move information to another part of page*/
$(document).ready(function(){
    alert("ready for business");
   

    $("form").submit(function(){
        var gov = $('#gov').val();
        var desc = $('#desc').val();
        console.log(gov);
       

        $('.right_side').append(`
        <div class="new_contact">
            <h2 class="full_name">${gov + " "}${desc}</h2>
            <p class="segwey">Click here to see description!!</p>
        </div>
        
        `);
        return false;  
    })
})
$(document).on("click",".new_contact",function(event){
    var notes = $("#notes").val();
    $(".segwey").click(function(event){
         $(this).hide();
         $('.new_contact').html(`
        <h2>${notes}</h2>`);return false;
        
       });event.stopPropagation()})        
    
    
    
        
        //   $(this).hide();
        //   $(this).siblings().show();
        //    $(this).siblings().css("color", "green")});
        //    })


// $(document).on("click",".contact-card",function(){
//     $('.swol').click(function(){
//       $(this).hide();
//       $(this).siblings().show();
//        $(this).siblings().css("color", "green")});
//        })