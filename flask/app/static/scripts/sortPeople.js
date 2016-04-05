angular.module('sortApp', [])

.controller('mainController', function($scope,) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // Load legislators from our API
  	$http({
		method: 'GET',
		url: '/api/people'
	}).success(function (result){
		$scope.people = result;
	});
});
