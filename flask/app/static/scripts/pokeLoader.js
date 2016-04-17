var pokeApp = angular.module('pokeApp', ['ui.bootstrap']);

pokeApp.config(['$locationProvider', function($locationProvider) {
     $locationProvider.html5Mode(true);
}]);

pokeApp.controller('mainController', function($scope, $http, $location) {
 	$scope.pokemon = [];
 	$scope.pokemon_name = "";
 	$scope.pokemon_type = "";
 	$scope.pokemon_hp = 0;
 	$scope.pokemon_move_1 = [];
 	$scope.pokemon_move_2 = [];
 	imgUrl = 'https://b1c01bf8eafe786b36c877247c911d2fb8db34b3-www.googledrive.com/host/0Bwhv4pFNwLa8WVhmUmsxN1ExOVU/static/img/';

	// $http.jsonp('http://swecune.com/api/type')
	// .then(function(json) {
	// 	$scope.types = json.data.data;
	// 	$scope.typeNames = $scope.type.map(function(val){
	// 		return val["name"];
	// 	});
	// });

	$http.jsonp('http://swecune.com/api/pokemon?offset=0&pokemon_per_page=100')
	.then(function(json) {
		$scope.pokemon = json.data.data;
		console.log(json.data.data);
	});

	$scope.draw = function(){
		num = Math.floor(Math.random($scope.pokemon.length))
		pokemon = $scope.pokemon[num]
		$scope.pokemon_name = pokemon["name"]
	}

	$scope.getColor = function(type){
		switch(type){
			case 1://water
				$scope.color = "blue";
				break;
			default:
				$scope.color = "gray";
				break;
		}
	}
  
});

