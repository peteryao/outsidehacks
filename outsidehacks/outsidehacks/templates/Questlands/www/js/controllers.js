angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('CatsCtrl', function($scope, $http) {
 $http.get('http://127.0.0.1:8000/category/?format=json').
      success(function(data) {
          $scope.categories = data.results;
      });
})

.controller('oneCatCtrl', function($scope, $http, $stateParams) {
  var category_info = 'http://127.0.0.1:8000/category/' + $stateParams.categoryId + '/?format=json';
  $http.get(category_info).success(function(data) {
          $scope.category = data;
      });
  $http.get('http://127.0.0.1:8000/quests/?format=json').
      success(function(res) {
          $scope.quests = res.results;
      });
})

.controller('QuestCtrl', function($scope, $http, $stateParams) {
  var quest_info = 'http://127.0.0.1:8000/quests/' + $stateParams.questId + '/?format=json';
  console.log(quest_info);
  $http.get(quest_info).success(function(data) {
          $scope.quest = data;
      });
});
