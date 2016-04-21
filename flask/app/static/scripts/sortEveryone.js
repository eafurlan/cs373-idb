var sortApp = angular.module('sortApp', ['angularUtils.directives.dirPagination']);

sortApp.config(['$locationProvider', function($locationProvider) {
    $locationProvider.html5Mode(true);
}]);



/*
    TEEN DRINKING AND CODE REPLICATION ARE VERY VERY BAD
    I STILL GOT A FAKE SEARCH DOE
*/
var butt = function(data,search){
        
        filtered_data = [];
        data_and = [];
        data_or = [];

        //Null and length check
        if (!search || search.length < 2) {
                return filtered_data;
            }

        all_terms = search.split(' ');

        data.forEach(function(datum){
            
            var all_attribs = "";
            var push_flag = false;
            var and_flag = true;

            if(datum._category === 'Bill'){
                all_attribs = datum.name  
                                + datum.bill_type 
                                + datum.current_status 
                                + datum.id 
                                + datum.date;
            }

            if(datum._category === 'Person'){
                all_attribs = datum.birthday 
                                + datum.lastname 
                                + datum.firstname 
                                + datum.party
                                + datum.start_date
                                + datum.state
                                + datum.title;
                                
            }

            /*Goes through every search term.
                every term present = AND
                some terms present = OR
                no terms present = no push
            */
            all_terms.forEach(function(term){
                if(!all_attribs.includes(term)){
                    //at least one attribute is not included
                    and_flag = false;
                }
                else{
                    //at least one attribute is included so pushing is okay
                    push_flag = true;
                }
            });

            if(and_flag){
                datum._query_type = 'AND';
            }
            else{
                datum._query_type = 'OR';
            }

            if(push_flag)
            {
                if(datum._query_type == 'AND'){
                    data_and.push(datum);
                }else{
                    data_or.push(datum)
                }
                //filtered_data.push(datum);
            }

        });
        
        filtered_data = data_and.concat(data_or);
        return filtered_data;
    }




sortApp.controller('mainController', function($scope, $http, $location) {
    $scope.people = [];
    $scope.everyone = [];
    $scope.filtered = [];
    $scope.loading = true;
    $http({
        method: 'GET',
        url: '/api/legislators'
    }).success(function(result) {
        $scope.people = result;
        $scope.people.forEach(function(person){
            person._category = 'Person';
        });
        $scope.everyone = $scope.everyone.concat($scope.people);
    });

    $http({
        method: 'GET',
        url: '/api/bills'
    }).success(function(result) {
        $scope.bills = result;
        $scope.bills.forEach(function(bill){
            bill._category = 'Bill';
        });
        $scope.everyone = $scope.everyone.concat($scope.bills);
        document.getElementById('search-bar').disabled = false;
        $scope.loading = false;
        document.getElementById('search-bar').placeholder = "INPUT SEARCH";
    });


    $scope.run_highlighter = function(search){
        $scope.filtered =  butt($scope.everyone,document.getElementById("search-bar").value);
        //document.getElementById("hide_panel").style.visibility = "visible";
        //console.log(document.getElementById("content"));
        setTimeout(function(){var myHilitor = new Hilitor("content");
        myHilitor.setMatchType("left");
        myHilitor.apply(document.getElementById("search-bar").value);},500);

    }

    $scope.hide_everything = function(){
        document.getElementById("hide_panel").style.visibility = "hidden";
    }

    $scope.makeLink = function () {
     		
       		$scope.selected = this.roll;
       		path_to_thing = $scope.selected.id + "";
       		if($scope.selected._category === 'Bill'){
       				window.location.replace("bills/"+path_to_thing);
       		}
       		else if($scope.selected._category === 'Person'){
       				window.location.replace("legislators/"+path_to_thing);
       		}	

    };

});