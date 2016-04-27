var pokeApp = angular.module('pokeApp', ['ngRoute']);

pokeApp.controller('mainController', function($scope, $http) { 	

 	img_url = 'https://b1c01bf8eafe786b36c877247c911d2fb8db34b3-www.googledrive.com/host/0Bwhv4pFNwLa8WVhmUmsxN1ExOVU/static/img/';
 	
 	getPokemonImg = function(num){
 		return img_url + "pokemon/pokemon_"+num+".png";
 	}

 	getTypeImg = function(num){
		return img_url + "type_"+num+".png";
	}

 	$scope.data;

 	$scope.pokemon; 
 	$scope.pokemon_name;
 	$scope.pokemon_type;
 	$scope.pokemon_type_img;
 	$scope.pokemon_hp;
 	$scope.move_1;
 	$scope.move_1_name;
 	$scope.move_1_power;
 	$scope.move_1_type;
 	$scope.move_1_type_img;
 	$scope.move_2;
 	$scope.move_2_name;
 	$scope.move_2_power;
 	$scope.move_2_type;
 	$scope.move_2_type_img;
 	$scope.move_3;
 	$scope.move_3_name;
 	$scope.move_3_power;
 	$scope.move_3_type;
 	$scope.move_3_type_img;
 	$scope.pokemon_color;
 	$scope.pokemon_img;

	$scope.draw = function(){
		num = Math.ceil(Math.random() * (721 - 1) + 1);

		$http({
			method: 'GET',
			url: '/api/pokemon/'+num
		}).success(function (result){
			renderCard(result);
		});

	};

	$scope.init = function(){
		$scope.draw();
	};

	renderCard = function(json_stuff){

		$scope.pokemon_name = json_stuff[0].name;
		$scope.pokemon_type = json_stuff[0].primary_type;
		$scope.pokemon_type_img = getTypeImg(json_stuff[0].primary_type);
		$scope.pokemon_img = getPokemonImg(json_stuff[0].id);
		$scope.pokemon_hp = json_stuff[0].stats[1].base_stat;
		
		$scope.move_1 = json_stuff[1];
		$scope.move_1_name = json_stuff[1].name;
		$scope.move_1_power = json_stuff[1].power;
		$scope.move_1_type = json_stuff[1].move_type;
		$scope.move_1_type_img = getTypeImg(json_stuff[1].move_type);

		$scope.move_2 = json_stuff[2];
		$scope.move_2_name = $scope.move_2.name;
		$scope.move_2_power = $scope.move_2.power;
		$scope.move_2_type = $scope.move_2.move_type;
		$scope.move_2_type_img = getTypeImg($scope.move_2_type);

		$scope.move_3 = json_stuff[3];
		$scope.move_3_name = $scope.move_3.name;
		$scope.move_3_power = $scope.move_3.power;
		$scope.move_3_type = $scope.move_3.move_type;
		$scope.move_3_type_img = getTypeImg($scope.move_3_type);

		populateTypeBasedInfo(json_stuff[0].primary_type);
		console.log($scope.pokemon_color);
	};	

	populateTypeBasedInfo = function(type){
		switch(type){
			case 1://normal
				$scope.pokemon_color = "#B39292";
				break;
			case 2://fighting
				$scope.pokemon_color = "#ff6633";
				break;
			case 3://flying
				$scope.pokemon_color = "#1C5DA8";
				break;
			case 4://poison
				$scope.pokemon_color = "#885FAE";
				break;
			case 5://ground
				$scope.pokemon_color = "#BC8059";
				break;
			case 6://rock
				$scope.pokemon_color = "#c68c53";
				break;
			case 7://bug
				$scope.pokemon_color = "#33995B";
				break;
			case 8://ghost
				$scope.pokemon_color = "#7F51AD";
				break;
			case 9://steel
				$scope.pokemon_color = "#869A93";
				break;
			case 10://fire
				$scope.pokemon_color = "#ff884d";
				break;
			case 11://water
				$scope.pokemon_color = "#5FB7E2";
				break;
			case 12://grass
				$scope.pokemon_color = "#41A641";
				break;
			case 13://electric
				$scope.pokemon_color = "#F0F569";
				break;
			case 14://psychic
				$scope.pokemon_color = "#ff80aa";
				break;
			case 15://ice
				$scope.pokemon_color = "#8FF4F7";
				break;
			case 16://dragon
				$scope.pokemon_color = "#2B878A";
				break;
			case 17://dark
				$scope.pokemon_color = "#7575a3";
				break;
			case 18://fairy
				$scope.pokemon_color = "#DD7DA6";
				break;
			default:
				$scope.pokemon_color = "gray";
				break;
		}
	};
  
});
