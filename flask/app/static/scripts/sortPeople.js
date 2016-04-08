var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);

sortApp.controller('mainController', function($scope, $http, $location) {
 	$scope.people = [];
  
  // Load people from our API
	$http({
		method: 'GET',
		url: '/api/legislators'
	}).success(function (result){
		$scope.people = result;
	});

	$scope.sort = function(keyname){
		$scope.sortKey     = keyname; // set the default sort type
  		$scope.reverse  = !$scope.reverse;  // set the default sort order
	}

	$scope.makeLink = function () {
  		$scope.selected = this.roll;
        path_to_person = $scope.selected.id + "";
        window.location = "legislators/"+path_to_person;
	};
  
});

