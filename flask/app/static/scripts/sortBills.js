angular.module('sortApp', [])

.controller('mainController', function($scope, $http) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // Load bills from our API
	$http({
		method: 'GET',
		url: '/api/bills'
	}).success(function (result){
		$scope.bills = result;
	});
  
});

