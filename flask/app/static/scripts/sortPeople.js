angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // create the list of people - elements need not be ordered, but keys can't be in quotes.
  $scope.people = [
  	{"party": "Democrat", "twitter": null, "lastname": "Franken", "start_date": "2015-01-06", "firstname": "Alan", "description": "Junior Senator from Minnesota", "birthday": "1951-05-21", "id": 412378, "photo_link": "https://www.govtrack.us/data/photos/412378-200px.jpeg", "title": "Senator", "youtube": "SenatorFranken", "state": "MN", "website": "http://www.franken.senate.gov"}, 
  	{"party": "Democrat", "twitter": "SenWarren", "lastname": "Warren", "start_date": "2013-01-03", "firstname": "Elizabeth", "description": "Senior Senator from Massachusetts", "birthday": "1949-06-22", "id": 412542, "photo_link": "https://www.govtrack.us/data/photos/412542-200px.jpeg", "title": "Senator", "youtube": "senelizabethwarren", "state": "MA", "website": "http://www.warren.senate.gov"}, 
  	{"party": "Democrat", "twitter": "SenWhitehouse", "lastname": "Whitehouse", "start_date": "2013-01-03", "firstname": "Sheldon", "description": "Junior Senator from Rhode Island", "birthday": "1955-10-20", "id": 412247, "photo_link": "https://www.govtrack.us/data/photos/412247-200px.jpeg", "title": "Senator", "youtube": "SenatorWhitehouse", "state": "RI", "website": "http://www.whitehouse.senate.gov"}
  ];
});
