
jQuery(document).ready(function($) {
    $("button").click(function(){    
    	var $btn = $(this).button('Running...')

    	$.get("/test", function(data){
    		$("#unitTestAlert").text( data.test_text );
    	});

	    // output = "hello" + " world "; //call python function here
	    // $("#unitTestAlert").text(output);

	    $("#unitTestAlert").removeClass("alert-danger");
	    $("#unitTestAlert").removeClass("alert-success");
	  	if($("#unitTestAlert").text().includes("Failed")){
	  		$("#unitTestAlert").addClass("alert-danger");
	  	}
	  	else{
	  		$("#unitTestAlert").addClass("alert-success");
	  	}

    	$btn.button('reset')
  });
});