$(function() {
  $('a#calculate').bind('click', function() {
    /*$.getJSON('http://localhost:5000/_add_numbers', {
      a: $('input[name="a"]').val(),
      b: $('input[name="b"]').val()
    }, function(data) {
      $("#result").text(data.result);
    });
    return false;*/
    var reset_data = {
      a: $('input[name="a"]').val(),
      b: $('input[name="b"]').val()
    }
    $.ajax({
      type: "GET",
      url: "http://localhost:5000/_add_numbers",
      data: reset_data,
      success: function(res){
        $("#result").text(res.result);
      },
      error: function(err){
        console.log("error");
      },
    });
  });
  $('a#chiama_consegne').bind('click', function() {
    var reset_data = {}
    $.ajax({
      type: "GET",
      url: "http://localhost:5000/_consegne_vaccini",
      data: reset_data,
      success: function(res){
        console.log(res["fornitore"]);
        $("#consegne").text(res["fornitore"]);
      },
      error: function(err){
        console.log("error");
      },
    });
  });
});
