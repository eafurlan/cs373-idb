angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // create the list of sushi rolls 
  $scope.bills = [
    {ID: 127129, Title: "To amend the Internal Revenue Code of 1986 to exclude from gross income the qualified military benefits received by retired military personnel serving as administrators or instructors in the Junior Reserve Officers' Training Corps.",
    Status: "referred", Type: "house", Date_Introduced: "1993-02-02"
    },
    {ID: 127130, Title: "Swain County Settlement Act of 1993", Status: "referred", Type: "senate", Date_Introduced: "1993-01-26"
    },
    {ID: 127131, Title: "A bill to extend the existing suspension of duty on (6R,7R)-7-{(R)-2-Amino-phenylacetamido}-3-methyl-8-oxo-5-thia-1-azabicyclo{4.2.0}oct-2-ene-2-carboxylic acid disolvate.",
    Status: "referred", Type: "senate", Date_Introduced: "1993-07-14"
    },
  ];
  
});

