var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);


sortApp.filter('bill_OR_search',function(){

	return function(data,search){


		filtered_data = []
		if(!search){
			return filtered_data
		}
		
		all_terms = search.split(' ')

		for ( var a = 0; a < all_terms.length; ++a){
			term = all_terms[a].toLowerCase();
			for ( var b = 0; b < data.length; ++b){
				datum = data[b];
				//checks each property for the value.
				if(datum.name.toLowerCase().includes(term) || datum.current_status.toLowerCase().includes(term)){
					//this data is cool
					filtered_data.push(datum);
				}

			}

		}
		return filtered_data;
	}//end inner func

});


sortApp.filter('bill_AND_search',function(){

	return function(data,search){

		filtered_data = [];
		if(!search){
			return filtered_data;
		}
		
		all_terms = search.split(' ')

		for(var data_ind = 0; data_ind < data.length; ++data_ind){
			datum = data[data_ind];
			flag = true;
			for(var term_ind = 0; term_ind < all_terms.length; ++term_ind){
				console.log("reaches here");
				term = all_terms[term_ind];
				if(datum.name.toLowerCase().includes(term) || datum.current_status.toLowerCase().includes(term)){
					console.log("It contains em!");
					break;
					//this data is cool
				}
				else{
					flag = false;
				}

			}
			if(flag)
				filtered_data.push(datum);
		}

		
		return filtered_data;
	}//end inner func

});


sortApp.controller('mainController', function($scope, $http, $location) {
 	$scope.people = [];
  	
  // Load people from our API
	$http({
		method: 'GET',
		url: 'http://0.0.0.0:8080/api/legislators'
	}).success(function (result){
		$scope.people = result;
	});

	$http({
		method: 'GET',
		url: 'http://0.0.0.0:8080/api/bills'
	}).success(function (result){
		$scope.bills = result;
	});

	
	// $scope.makeLink = function () {
 //  		// $scope.selected = this.roll;
 //    //     path_to_person = $scope.selected.id + "";
 //    //     window.location.replace("legislators/"+path_to_person);

 //    		$scope.selected = //SOMETHING
 //    		path_to_thing = $scope.selected.id + "";
 //    		if(/* The thing is a bill */){
 //    				window.location.replace("bills/"+path_to_person);
 //    		}
 //    		else if(/*The thing is a legislator*/){
 //    				window.location.replace("legislators/"+path_to_person);
 //    		}	

	// };
  
});

