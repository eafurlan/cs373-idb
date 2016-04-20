var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
}]);


sortApp.filter('bill_OR_search', function() {

    return function(data, search) {


            filtered_data = [];
            if (!search) {
                return filtered_data;
            }

            all_terms = search.split(' ')

            data.forEach(function(datum) {
                push_flag = false;
                all_terms.forEach(function(term) {
                    if (datum.name.includes(term)) {
                        push_flag = true;
                    }
                })
                if (push_flag) {
                    filtered_data.push(datum);
                }
            });

            return filtered_data;
        } //end inner func

});


sortApp.filter('bill_AND_search', function() {

    return function(data, search) {


            filtered_data = [];
            if (!search) {
                return filtered_data;
            }

            all_terms = search.split(' ');

            data.forEach(function(datum) {
                push_flag = true;
                all_terms.forEach(function(term) {
                    if (!datum.name.includes(term)) {
                        push_flag = false;
                    }
                })
                if (push_flag) {
                    filtered_data.push(datum);
                }

            });

            return filtered_data;
        } //end inner func

});


sortApp.controller('mainController', function($scope, $http, $location) {
    $scope.people = [];

    // Load people from our API
    $http({
        method: 'GET',
        url: 'http://0.0.0.0:8080/api/legislators'
    }).success(function(result) {
        $scope.people = result;
    });

    $http({
        method: 'GET',
        url: 'http://0.0.0.0:8080/api/bills'
    }).success(function(result) {
        $scope.bills = result;
    });


    // $scope.makeLink = function () {
    //  		// $scope.selected = this.roll;
    //    //     path_to_person = $scope.selected.id + "";
    //    //     window.location.replace("legislators/"+path_to_person);

    //    		$scope.selected = //SOMETHING
    //    		path_to_thing = $scope.selected.id + "";
    //    		if(/* The thing is a bill */){
    //    				window.location.replace("bills/"+path_to_person);
    //    		}
    //    		else if(/*The thing is a legislator*/){
    //    				window.location.replace("legislators/"+path_to_person);
    //    		}	

    // };

});