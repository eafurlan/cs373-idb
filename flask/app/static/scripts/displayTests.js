
jQuery(document).ready(function($) {
    $("button").click(function(){    
    	//var $btn = $(this).button('Running...');
    	$('#unitTestButton').val() = 'Running ... '
    	$("#unitTestAlert").removeClass("alert-success");
    	$.get("/test", function(data){
   			$("#unitTestAlert").html( data.test_text );
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