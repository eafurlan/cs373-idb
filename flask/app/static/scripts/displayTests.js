
jQuery(document).ready(function($) {
    $("button").click(function(){    
    	var $btn = $(this).button('Running...')
	    output = "hello" + " world "; //call python function here
	    $("#unitTestAlert").text(output);

	    $("#unitTestAlert").removeClass("alert-danger");
	    $("#unitTestAlert").removeClass("alert-success");
	  	if(output.includes("Failed")){
	  		$("#unitTestAlert").addClass("alert-danger");
	  	}
	  	else{
	  		$("#unitTestAlert").addClass("alert-success");
	  	}

    	$btn.button('reset')
  });
});