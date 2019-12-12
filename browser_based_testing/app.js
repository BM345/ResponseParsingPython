var app = angular.module("ResponseParsing", []);

app.controller("MainController", ["$scope", "$http", function MainController($scope, $http) {

    $scope.$watch("studentsResponse", function (newValue, oldValue) {

        var requestData = {
            "studentsResponse": newValue,
            "expectedResponseType": "integer",
            "constraints": {}
        }

        $http.post("/api/validate", requestData).then(function (response) {
            var responseData = response.data;

            if (responseData.isAccepted) {
                $scope.isAccepted = "Accepted";
                $scope.isAcceptedColour = 120;
            }
            else {
                $scope.isAccepted = "Rejected";
                $scope.isAcceptedColour = 350;
            }

            $scope.messageText = responseData.messageText;
        });

    });

}]);