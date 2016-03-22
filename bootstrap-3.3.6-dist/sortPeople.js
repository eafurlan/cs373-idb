angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // create the list of people - elements need not be ordered, but keys can't be in quotes.
  $scope.people = [{id: 400034, firstname: "Roy", lastname: "Blunt", title: "Senator", party: "Republican", start_date: "2011-01-05", state: "MO", website: "http://www.blunt.senate.gov", youtube: "SenatorBlunt", twitter: "RoyBlunt"},
    {id: 400040, twitter: "JohnBoozman", start_date: "2011-01-05", party: "Republican", title: "Senator", firstname: "John", lastname: "Boozman", state: "AR", website: "http://www.boozman.senate.gov", youtube: "BoozmanPressOffice"},
    {id: 400054, twitter: "SenatorBurr", start_date: "2011-01-05", party: "Republican", title: "Senator", firstname: "Richard", lastname: "Burr", state: "NC", website: "http://www.burr.senate.gov", youtube: "SenatorRichardBurr"}
  ];
});
