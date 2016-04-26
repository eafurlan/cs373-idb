var pokeApp = angular.module('pokeApp', ['ngRoute']);

pokeApp.controller('mainController', function($scope, $http) {
 	//Grabbed dummy data for Ivysaur to test webpage - didn't work :( 
 	

 	img_url = 'https://b1c01bf8eafe786b36c877247c911d2fb8db34b3-www.googledrive.com/host/0Bwhv4pFNwLa8WVhmUmsxN1ExOVU/static/img/';
 	
 	getPokemonImg = function(num){
 		return img_url + "pokemon/pokemon_"+num+".png";
 	}

 	getTypeImg = function(num){
		return img_url + "type_"+num+".png";
	}

 	$scope.data;

 	$scope.pokemon; //jQuery.parseJSON('{"id": 2, "name": "Ivysaur", "stats": [{"base_stat": 60, "name": "speed"}, {"base_stat": 80, "name": "special_defense"}, {"base_stat": 80, "name": "special_attack"}, {"base_stat": 63, "name": "defense"}, {"base_stat": 62, "name": "attack"}, {"base_stat": 60, "name": "hp"}], "primary_type": 12, "secondary_type": 4, "average_stats": 67, "moves": [14, 15, 20, 22, 29, 33, 34, 36, 38, 45, 70, 72, 73, 74, 75, 76, 77, 79, 81, 92, 99, 102, 104, 111, 113, 115, 117, 148, 156, 164, 173, 174, 182, 188, 189, 202, 203, 207, 210, 213, 214, 216, 218, 219, 230, 235, 237, 241, 249, 263, 267, 282, 290, 331, 363, 388, 402, 412, 445, 447, 474, 496, 497, 520, 590]}');
 	$scope.pokemon_name = "Name";
 	$scope.pokemon_type = 1;
 	$scope.pokemon_type_img = getTypeImg(1);
 	$scope.pokemon_hp = 50;
 	$scope.move_1 = 5;
 	$scope.move_1_name = "";
 	$scope.move_1_power = 0;
 	$scope.move_1_type = 1;
 	$scope.move_1_type_img = getTypeImg(1);
 	$scope.move_2 = 10;
 	$scope.move_2_name = "";
 	$scope.move_2_power = 0;
 	$scope.move_2_type = 2;
 	$scope.move_2_type_img = getTypeImg(1);
 	$scope.move_3;
 	$scope.move_3_name = "";
 	$scope.move_3_power = 0;
 	$scope.move_3_type = 1;
 	$scope.move_3_type_img = getTypeImg(1);
 	$scope.pokemon_color = "gray";
 	$scope.pokemon_img = getPokemonImg(1);
 	//url for all the pictures - go here to see a list of image names. Has type and pokemon .png's

 	// jsonp_url - "http://ildb.me/get/?url=<swecune.com/api/pokemon/"+num+">&callback=?'"
	renderCard = function(json_stuff){

		$scope.data = json_stuff;

		console.log($scope.pokemon_name);
		$scope.pokemon = $scope.data[0];
		$scope.pokemon_name = $scope.pokemon.name;
		$scope.pokemon_type = $scope.pokemon.primary_type;
		$scope.pokemon_type_img = getTypeImg($scope.pokemon.type);
		$scope.pokemon_hp = $scope.pokemon.stats[1].base_stat;
		
		$scope.move_1 = $scope.data[1];
		$scope.move_1_name = $scope.move_1.name;
		$scope.move_1_power = $scope.move_1.power;
		$scope.move_1_type = $scope.move_1.move_type;
		$scope.move_1_type_img = getTypeImg($scope.move_1_type);

		$scope.move_2 = $scope.data[2];
		$scope.move_2_name = $scope.move_2.name;
		$scope.move_2_power = $scope.move_2.power;
		$scope.move_2_type = $scope.move_2.move_type;
		$scope.move_2_type_img = getTypeImg($scope.move_2_type);

		$scope.move_3 = $scope.data[3];
		$scope.move_3_name = $scope.move_3.name;
		$scope.move_3_power = $scope.move_3.power;
		$scope.move_3_type = $scope.move_3.move_type;
		$scope.move_3_type_img = getTypeImg($scope.move_3_type);

		populateTypeBasedInfo($scope.pokemon_type);
	};	

	$scope.draw = function(){
		//Get a random pokemon's id number (pokemon id numbers go from 1 to 721)
		num = Math.ceil(Math.random(721))

	// Load pokemon from API


	$http({
		method: 'GET',
		url: '/api/pokemon/'+num
	}).success(function (result){
		console.log(num)
		renderCard(result);
		// $scope.data = result;
		// console.log($scope.data);
		// console.log($scope.data[0].name);
		// renderCard($scope.data)
	});
		// //One possible way of getting the api data - currently not working
		// $http.get('/api/pokemon/'+num)
		// .then(function(res)
		// {
		// 	console.log(res.data);
		// 	$scope.data= JSON.parse(res.data);
		// 	console.log($scope.pokemon);
		// 	console.log($scope.pokemon.name);
		// 	$scope.move_1 = jQuery.parseJSON(res.data[1]);
		// 	$scope.move_2 = jQuery.parseJSON(res.data[2]);
		// });
		// // Another possible way - not working too. Need to look into the callback field in the url.
		// // $.ajax({
		// //   url: "http://ildb.me/get/?url=<swecune.com/api/pokemon/"+num+">&callback=?JSON_CALLBACK",
		// //   dataType: 'jsonp',
		// //   scriptCharset: 'UTF-8',
		// //   success: function(data) {
		// //     console.log(data);
		// // }});
		// //Assigning variables that will be used in the html



		// $scope.move_2_name = $scope.move_2.name;
		// $scope.move_2_power = $scope.move_2.power;
		// $scope.move_2_type = $scope.move_2.type;
		// $scope.move_2_type_img = getTypeImg($scope.move_2.type);
		// // move_1 = $scope.pokemon.moves[1];
		// //SHOULD be getting the move info to fill in the variables
		// // $http.jsonp('http://swecune.com/api/move/'+move_1)
		// // .then(function(res){
		// // 	$scope.move_1_name = res.data.name;
		// // 	$scope.move_1_power = res.data.power;
		// // 	$scope.move_1_type = img_url+"type_"+res.data.move_type+".png";
		// // });
		// // move_2 = $scope.pokemon.moves[2];
		// //Again, SHOULD be getting move data
		// // $http.jsonp('http://swecune.com/api/move/'+move_2)
		// // .then(function(res){
		// // 	$scope.move_2_name = res.data.name;
		// // 	$scope.move_2_power = res.data.power;
		// // 	$scope.move_2_type = img_url+"type_"+res.data.move_type+".png";
		// // });
		// //Get type-based info - may need to add weaknesses in this function?
		// populateTypeBasedInfo($scope.pokemon.primary_type)
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

