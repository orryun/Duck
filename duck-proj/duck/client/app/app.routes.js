(function() {
    'use strict';

    angular
        .module('app')
        .run(appRun);

    /* @ngInject */
    function appRun(routerHelper) {
        routerHelper.configureStates(getStates(), '/');
    }

    function getStates() {
        return [
            {
                state: 'hello',
                config: {
                    url: '/',
                    templateUrl: '/media/build/layout/hello.html'
                }
            },
            {
                state: 'search',
                config: {
                    url: '/search',
                    templateUrl: '/media/build/search/search.html',
                    controller: 'SearchController as searchVm'
                }
            },
            {
                state: 'search.term',
                config: {
                    url: '/{term:\\w*}',
                    templateUrl: '/media/build/search/search.html',
                    controller: 'SearchController as searchVm'
                }
            }
        ];
    }

})();
