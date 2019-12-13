var app = angular.module("ResponseParsing", []);

app.controller("MainController", ["$scope", "$http", function MainController($scope, $http) {

    $scope.developerMode = false;

    $scope.expectedResponseType = "integer";

    $scope.allowLeadingZeros = false;
    $scope.mustHaveExplicitSign = false;
    $scope.sf1 = "";
    $scope.sf2 = "";
    $scope.nsf = "";
    $scope.dp1 = "";
    $scope.dp2 = "";
    $scope.ndp = "";
    $scope.currency = "USD";

    $scope.acceptOrRejectIsVisible = false;

    $scope.getValidationResponse = function () {

        var requestData = {
            "studentsResponse": $scope.studentsResponse,
            "expectedResponseType": $scope.expectedResponseType,
            "constraints": {
                "allowLeadingZeros": $scope.allowLeadingZeros,
                "mustHaveExplicitSign": $scope.mustHaveExplicitSign,
            }
        }

        if ($scope.sf1.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveAtLeastNSF = parseInt($scope.sf1);
        }

        if ($scope.sf2.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveNoMoreThanNSF = parseInt($scope.sf2);
        }

        if ($scope.nsf.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveExactlyNSF = parseInt($scope.nsf);
        }

        if ($scope.dp1.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveAtLeastNDP = parseInt($scope.dp1);
        }

        if ($scope.dp2.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveNoMoreThanNDP = parseInt($scope.dp2);
        }

        if ($scope.ndp.match(/^[0-9]+$/g)) {
            requestData.constraints.mustHaveExactlyNDP = parseInt($scope.ndp);
        }

        if ($scope.expectedResponseType == "currencyValue") {
            requestData.constraints.currency = $scope.currency;
        }

        if ($scope.developerMode) {
            console.log(requestData);
        }

        $http.post("/api/validate", requestData).then(function (response) {
            var responseData = response.data;

            if ($scope.developerMode) {
                console.log(responseData);
            }

            if (responseData.isAccepted) {
                $scope.isAccepted = "Accepted";
                $scope.isAcceptedColour = 120;
            }
            else {
                $scope.isAccepted = "Rejected";
                $scope.isAcceptedColour = 350;
            }

            $scope.acceptOrRejectIsVisible = true;
            $scope.messageText = responseData.messageText;
            $scope.normalisedStudentsResponse = responseData.normalisedStudentsResponse;
        });

    }

    $scope.reset = function () {
        $scope.isAccepted = "";
        $scope.isAcceptedColour = 350;

        $scope.acceptOrRejectIsVisible = false;
        $scope.messageText = "";
        $scope.normalisedStudentsResponse = "";
    }

    $scope.submit = function () {

        $scope.getValidationResponse();

    }

    $scope.$watchGroup(["studentsResponse",
        "expectedResponseType",
        "allowLeadingZeros",
        "mustHaveExplicitSign",
        "sf1",
        "sf2",
        "nsf",
        "dp1",
        "dp2",
        "ndp"], function (newValue, oldValue) {

            if ($scope.developerMode) {
                $scope.getValidationResponse();
            }
            else {
                $scope.reset();

            }

        });


    $scope.$watchGroup(["expectedResponseType",
        "allowLeadingZeros",
        "mustHaveExplicitSign"], function (newValue, oldValue) {

            if (!$scope.developerMode) {
                $scope.reset();
            }

        });

}]);