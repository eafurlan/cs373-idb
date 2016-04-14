var sortApp = angular.module('pokeApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);

sortApp.controller('mainController', function($scope, $http, $location) {
 	$scope.types = [];
 	$scope.typeNames = [];
 	$scope.pokemon_collection = [];
  
  // Load bills from our API
	$http({
		method: 'GET',
		url: 'http://swecune.com/api/v1/type'
	}).success(function (result){
		$scope.types = result;
		$scope.typeNames = [x["name"] for x in $scope.types] //LOL, no python
	});

	$scope.getPokemon = function(typeID){
		$scope.pokemon_collection = $scope.types[typeID]["pokemon"]
	}

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

