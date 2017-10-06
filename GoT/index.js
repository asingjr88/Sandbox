$(document).ready(function(){
  $(document).on('click', 'img', function(){
    let id = this.id

    $.get(`https://www.anapioficeandfire.com/api/houses/${id}`, function(res){
      console.log(res)
      $('#name').html(`Name: ${res.name}`)
      $('#words').html(`Words: ${res.words}`)
      $('#titles').html(`Titles: ${res.titles}`)
    },"json")
  })
})
