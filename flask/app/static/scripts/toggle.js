var showApp = angular.module('toggleApp', [])

.controller('mainController', function($scope) {

  $scope.sponsor_collapsed = true;
  $scope.cosponsor_collapsed = true;
  $scope.cosponsored_by_collapsed = true;
  
});