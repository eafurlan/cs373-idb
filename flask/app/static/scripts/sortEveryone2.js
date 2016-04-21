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
            all_terms = search.toLowerCase().split(' ')

            data.forEach(function(datum) {
                push_flag = false;
                all_terms.forEach(function(term) {
                    if (datum.name.toLowerCase().includes(term)  || 
                    	datum.bill_type.toLowerCase().includes(term) || 
                    	datum.current_status.includes(term) || 
                    	datum.id === parseInt(term) || 
                    	datum.date.includes(term)) {
                        
                        push_flag = true;
                    }
                })
                if (push_flag) {
                    datum.link_type = 'Bill';
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
            var concatted =datum.name  + 
            	datum.bill_type + 
            	datum.current_status +  
            	datum.id + 
            	datum.date;

                push_flag = true;
                all_terms.forEach(function(term) {
                    if (!(concatted.includes(term))) {
                        push_flag = false;
                    }
                });
                if (push_flag) {
                    datum.link_type = 'Bill';
                    filtered_data.push(datum);
                }

            });

            return filtered_data;
        } //end inner func

});



sortApp.filter('people_AND_search', function() {

    return function(data, search) {

            filtered_data = [];
            if (!search) {
                return filtered_data;
            }

            all_terms = search.split(' ');

            data.forEach(function(datum) {
                push_flag = true;
                var concatted = datum.birthday + datum.description 
            						+ datum.lastname 
            						+ datum.firstname 
            						+ datum.party
									+ datum.start_date
									+ datum.state
									+ datum.title
									+ datum.twitter
									+ datum.youtube;
                all_terms.forEach(function(term) {
                    if (!(concatted.includes(term))) {
                        push_flag = false;
                    }
                })
                if (push_flag) {
                    datum.link_type = 'Person';
                    filtered_data.push(datum);
                }

            });

            return filtered_data;
        } //end inner func

});


sortApp.filter('people_OR_search', function() {

    return function(data, search) {

            filtered_data = [];
            if (!search) {
                return filtered_data;
            }

            all_terms = search.split(' ');

            data.forEach(function(datum) {
                push_flag = false;
                var concatted = datum.birthday + datum.description 
            						+ datum.lastname 
            						+ datum.firstname 
            						+ datum.party
									+ datum.start_date
									+ datum.state
									+ datum.title
									+ datum.twitter
									+ datum.youtube;
                all_terms.forEach(function(term) {
                    if (concatted.includes(term)) {
                        push_flag = true;
                    }
                })
                if (push_flag) {
                    datum.link_type = 'Person';
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

    function hasOwnProperty(obj, prop) {
    var proto = obj.__proto__ || obj.constructor.prototype;
    return (prop in obj) &&
        (!(prop in proto) || proto[prop] !== obj[prop]);
	}


    $scope.makeLink = function () {
     		// $scope.selected = this.roll;
       		// path_to_person = $scope.selected.id + "";
       		// window.location.replace("legislators/"+path_to_person);

       		$scope.selected = this.roll;
       		path_to_thing = $scope.selected.id + "";
       		if($scope.selected.link_type === 'Bill'){
       				window.location.replace("bills/"+path_to_thing);
       		}
       		else if($scope.selected.link_type === 'Person'){
       				window.location.replace("legislators/"+path_to_thing);
       		}	

    };

});