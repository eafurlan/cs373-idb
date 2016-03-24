angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // create the list of bills - elements need not be ordered, but keys can't be in quotes.
  $scope.bills = [
    {id: 127129, name: "To amend the Internal Revenue Code of 1986 to exclude from gross income the qualified military benefits received by retired military personnel serving as administrators or instructors in the Junior Reserve Officers' Training Corps.",
    current_status: "referred", bill_type: "house", date: "1993-02-02"
    },
    {id: 127130, name: "Swain County Settlement Act of 1993", current_status: "referred", bill_type: "senate", date: "1993-01-26"
    },
    {id: 127131, name: "A bill to extend the existing suspension of duty on (6R,7R)-7-{(R)-2-Amino-phenylacetamido}-3-methyl-8-oxo-5-thia-1-azabicyclo{4.2.0}oct-2-ene-2-carboxylic acid disolvate.",
    current_status: "referred", bill_type: "senate", date: "1993-07-14"
    },
  ];
  
});

