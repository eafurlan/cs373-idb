var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);

sortApp.filter('or',/*or*/function(){

	return function(input){
		/* Put search logic here */
	}

});

sortApp.controller('mainController', function($scope, $http, $location) {
 	$scope.people = [];
  	
  // Load people from our API
	$http({
		method: 'GET',
		url: '/api/legislators'
	}).success(function (result){
		$scope.people = result;
	});

	$http({
		method: 'GET',
		url: '/api/bills'
	}).success(function (result){
		$scope.bills = result;
	});


	//NO NEED FOR SORTING
	// $scope.sort = function(keyname){
	// 	$scope.sortKey     = keyname; // set the default sort type
 //  		$scope.reverse  = !$scope.reverse;  // set the default sort order
	// }

	$scope.makeLink = function () {
  		// $scope.selected = this.roll;
    //     path_to_person = $scope.selected.id + "";
    //     window.location.replace("legislators/"+path_to_person);

    		$scope.selected = //SOMETHING
    		path_to_thing = $scope.selected.id + "";
    		if(/* The thing is a bill */){
    				window.location.replace("bills/"+path_to_person);
    		}
    		else if(/*The thing is a legislator*/){
    				window.location.replace("legislators/"+path_to_person);
    		}	

	};
  
});

