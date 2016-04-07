
jQuery(document).ready(function($) {
    $("#unitTestAlert").hide();
    $("button").click(function(){    
    	var $btn = $(this).button('Running...');

    	
    	$("#unitTestAlert").slideToggle( "slow",function(){

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