angular.module('sortApp', [])

.controller('mainController', function($scope) {
  $scope.sortType     = 'name'; // set the default sort type
  $scope.sortReverse  = false;  // set the default sort order
  
  // create the list of bills - elements need not be ordered, but keys can't be in quotes.
  $scope.bills = [
    {
      "name": "Pay Stub Disclosure Act",
      "bill_type": "senate_bill",
      "current_status": "referred",
      "sponsor": 412378,
      "date": "2016-03-03",
      "id": 343921
    },
    {
      "name": "Comprehensive Addiction and Recovery Act of 2016",
      "bill_type": "senate_bill",
      "current_status": "pass_over_senate",
      "sponsor": 412247,
      "date": "2015-02-12",
      "id": 336967
    },
    {
      "name": "Behavioral Health Coverage Transparency Act of 2016",
      "bill_type": "senate_bill",
      "current_status": "referred",
      "sponsor": 412542,
      "date": "2016-03-07",
      "id": 343960
    }
];
  
});

