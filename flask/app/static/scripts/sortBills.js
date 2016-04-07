angular.module('sortApp', ['angularUtils.directives.dirPagination'])

.controller('mainController', function($scope, $http) {
 	$scope.bills = [];
  
  // Load bills from our API
	$http({
		method: 'GET',
		url: '/api/bills'
	}).success(function (result){
		$scope.bills = result;
	});

	$scope.sort = function(keyname){
		$scope.sortKey     = keyname; // set the default sort type
  		$scope.reverse  = !$scope.reverse;  // set the default sort order
	}
  
});

