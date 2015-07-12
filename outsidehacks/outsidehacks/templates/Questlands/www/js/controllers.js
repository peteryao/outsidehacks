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
 $http.get('http://45.55.21.17:8000/zones/.json').
      success(function(data) {
          $scope.greeting = data;
          console.log($scope.greeting);
      });
  $scope.categories = [
    { title: 'Food', id: 1 },
    { title: 'Music', id: 2 },
    { title: 'Friendship', id: 3 },
    { title: 'Indie', id: 4 },
    { title: 'Solo', id: 5 },
    { title: 'Yolo', id: 6 }
  ];
})

.controller('oneCatCtrl', function($scope, $stateParams) {
 categories = [
    { title: 'Food', id: 1 },
    { title: 'Music', id: 2 },
    { title: 'Friendship', id: 3 },
    { title: 'Indie', id: 4 },
    { title: 'Solo', id: 5 },
    { title: 'Yolo', id: 6 }
  ];
  $scope.quests = [
    { title: 'quest 1', id: 1 },
    { title: 'quest 2', id: 2 },
    { title: 'quest 3', id: 3 },
    { title: 'quest 4', id: 4 },
    { title: 'quest 5', id: 5 },
    { title: 'quest 6', id: 6 }
  ]
  $scope.category = categories[$stateParams.categoryId-1];
})

.controller('QuestCtrl', function($scope, $stateParams) {
  console.log($stateParams)
});
