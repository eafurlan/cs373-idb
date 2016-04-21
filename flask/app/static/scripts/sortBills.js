var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);

sortApp.controller('mainController', function($scope, $http, $location) {
 	$scope.bills = [];
 	$scope.loading = true;
  
  // Load bills from our API
	$http({
		method: 'GET',
		url: '/api/bills'
	}).success(function (result){
		$scope.bills = result;
		$scope.loading = false;
	});

	$scope.sort = function(keyname){
		$scope.sortKey     = keyname; // set the default sort type
  		$scope.reverse  = !$scope.reverse;  // set the default sort order
	}

	$scope.makeLink = function () {
  		$scope.selected = this.roll;
        path_to_bill = $scope.selected.id + "";
        window.location = "bills/"+path_to_bill;
	};
  
});

