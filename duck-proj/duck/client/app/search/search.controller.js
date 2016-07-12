(function() {
    'use strict';

    angular
        .module('app.search', [])
        .constant('defaultTitle', 'An elegant title...')
        .controller('SearchController', SearchController);

    /* @ngInject */
    function SearchController($scope, $rootScope, $state, defaultTitle, searchService) {
        $scope.title = defaultTitle;
        $scope.selected = {};
        $scope.loadFromState = loadFromState;
        $scope.search = search;

        $scope.targets = [
            {name: 'Foo'},
            {name: 'Bar'},
            {name: 'Buzz'}
        ];

        // When the state changes, the controller will be updated and a search will take place.
        $rootScope.$on('$stateChangeSuccess', function () {
            $scope.loadFromState();
        });

        // Load local variables from the state (the URL of the page).
        function loadFromState() {
            $scope.searchTerm = $rootScope.$stateParams.term || 'sir';
            searchService.query({'q': $scope.searchTerm}, function(data) {
                $scope.searchResults = data;
            });
        }

        function search(term) {
            $state.go('search.term', {term: term});
        }

    }

})();
