
jQuery(document).ready(function($) {
    $("button").click(function(){    
    	//var $btn = $(this).button('Running...');
    	$(this).html('Running ... ');
    	$("#unitTestAlert").removeClass("alert-success");
      $("#unitTestAlert").text("");
    	$.get("/test", function(data){
   			$("#unitTestAlert").html( data.test_text );
   			$(unitTestButton).html('Run');
   			$("#unitTestAlert").removeClass("alert-danger");
	    	$("#unitTestAlert").removeClass("alert-success");
		  	if($("#unitTestAlert").text().includes("Failed")){
		  		$("#unitTestAlert").addClass("alert-danger");
		  	}
		  	else{
		  		$("#unitTestAlert").addClass("alert-success");
		  	}

    });

	   

    	$btn.button('reset')
  });
});