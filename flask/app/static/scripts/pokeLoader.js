var pokeApp = angular.module('pokeApp', []);

pokeApp.controller('mainController', function($scope, $http) {
 	$scope.pokemon;
 	$scope.pokemon_name = "";
 	$scope.pokemon_type = "";
 	$scope.pokemon_hp = 0;
 	$scope.pokemon_move_1_name = "";
 	$scope.pokemon_move_1_power = 0;
 	$scope.pokemon_move_1_type = 0;
 	$scope.pokemon_move_2_name = "";
 	$scope.pokemon_move_2_power = 0;
 	$scope.pokemon_move_2_type = 0;
 	$scope.pokemon_color = "gray";
 	$scope.pokemon_img = "";
 	img_url = 'https://b1c01bf8eafe786b36c877247c911d2fb8db34b3-www.googledrive.com/host/0Bwhv4pFNwLa8WVhmUmsxN1ExOVU/static/img/';

	$scope.draw = function(){
		num = Math.ceil(Math.random(721))
		console.log("trying to get pokemon number"+num)
		$http.jsonp('http://swecune.com/api/pokemon/'+num)
		.then(function(res){
			console.log(res);
			$scope.pokemon = res;
		});
		console.log($scope.pokemon);
		$scope.pokemon_name = $scope.pokemon["name"];
		$scope.pokemon_type = img_url+"type_"+$scope.pokemon["primary_type"]+".png";
		$scope.pokemon_hp = $scope.pokemon["stats"][1]["base_stat"];
		move_1 = $scope.pokemon["moves"][1];
		$http.jsonp('http://swecune.com/api/move/'+move_1)
		.then(function(res){
			$scope.pokemon_move_1_name = res["name"];
			$scope.pokemon_move_1_power = res["power"];
			$scope.pokemon_move_1_type = img_url+"type_"+res["move_type"]+".png";
		});
		move_2 = $scope.pokemon["moves"][2];
		$http.jsonp('http://swecune.com/api/move/'+move_2)
		.then(function(res){
			$scope.pokemon_move_2_name = res["name"];
			$scope.pokemon_move_2_power = res["power"];
			$scope.pokemon_move_2_type = img_url+"type_"+res["move_type"]+".png";
		});
		populateTypeBasedInfo($scope.pokemon["primary_type"])
	}

	populateTypeBasedInfo = function(type){
		switch(type){
			case 1://normal
				$scope.pokemon_color = "9F6A4F";
				break;
			case 2://fighting
				$scope.pokemon_color = "A81C2A";
				break;
			case 3://flying
				$scope.pokemon_color = "1C5DA8";
				break;
			case 4://poison
				$scope.pokemon_color = "8130A4";
				break;
			case 5://ground
				$scope.pokemon_color = "BC8059";
				break;
			case 6://rock
				$scope.pokemon_color = "652C07";
				break;
			case 7://bug
				$scope.pokemon_color = "058D3C";
				break;
			case 8://ghost
				$scope.pokemon_color = "8B37DF";
				break;
			case 9://steel
				$scope.pokemon_color = "869A93";
				break;
			case 10://fire
				$scope.pokemon_color = "F25120";
				break;
			case 11://water
				$scope.pokemon_color = "5FB7E2";
				break;
			case 12://grass
				$scope.pokemon_color = "41A641";
				break;
			case 13://electric
				$scope.pokemon_color = "F0F569";
				break;
			case 14://psychic
				$scope.pokemon_color = "E61C74";
				break;
			case 15://ice
				$scope.pokemon_color = "8FF4F7";
				break;
			case 16://dragon
				$scope.pokemon_color = "2B878A";
				break;
			case 17://dark
				$scope.pokemon_color = "2A0936";
				break;
			case 18://fairy
				$scope.pokemon_color = "BF2568";
				break;
			default:
				$scope.pokemon_color = "gray";
				break;
		}
	}
  
});

