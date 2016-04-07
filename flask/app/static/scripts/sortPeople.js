angular.module('sortApp', ['angularUtils.directives.dirPagination'])

.controller('mainController', function($scope, $http) {  
	$scope.people = [];
	
  	// Load legislators from our API
  	$http({
		method: 'GET',
		url: '/api/legislators'
	}).success(function (result){
		$scope.people = result;
	});

    $scope.sort = function(keyname){
        $scope.sortKey = keyname;   //set the sortKey to the param passed
        $scope.reverse = !$scope.reverse; //if true make it false and vice versa
    }

});
