$(document).ready(function(){
    alert('Get It Done');

    $('form').submit(function(){
         var choice = $('#city_choice').val();
                console.log(choice);
                $.get(`http://api.openweathermap.org/data/2.5/weather?q=${choice},usk&&appid=a66e0a045769f23dca72b6f78195d41d`, function(res){
                    var temp = res.main.temp
                    console.log(res);
                    console.log(res.main.temp);
                    $('#results').text('Temperature equals: '+ temp)
                }, 
                "json")
        return false
    })
    $(document).on('submit', 'form', function(){
        console.log(res.main.temp)

    /*$('form').submit(function() {
        // your code here (build up your url)
        alert('searching for weather');       
        })  
            // your code here
        // don't forget to return false so the page doesn't refresh
        return false;*/
    });

//http://api.openweathermap.org/data/2.5/weather?q=NewYork,usk&&appid=a66e0a045769f23dca72b6f78195d41d



/*a66e0a045769f23dca72b6f78195d41d
api.openweathermap.org/data/2.5/weather?q=

http://api.openweathermap.org/data/2.5/weather?q=NewYork,usk&&appid=a66e0a045769f23dca72b6f78195d41d
3827409*/
})