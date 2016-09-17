var PRIVATE_URLS = [
    // "getting-started/run-first-simulation",
    // "getting-started/ui-overview",

    // "materials/creating-structures",
    // "materials/upload-and-import",
    // "materials/characteristic-properties",
    "materials/comparing-materials",
    "materials/combinatorial-sets",

    // "models/overview",
    // "models/advanced-characteristics",
    "models/convergence-algorithms",
    "models/structural-relaxation",
    "models/combinatorial-set-input",
    // "models/density-functional-theory",
    // "models/simulation-workflows",
    // "models/example-simulations",

    // "compute/overview",
    "compute/queues",
    "compute/benchmarks-and-scalability",
    "compute/connection-options",
    "compute/setting-parameters",

    // "collaboration/organizations",
    "collaboration/create-organization",
    "collaboration/invite-friends",

    // "cli/overview",
    "cli/login",
    "cli/accounting",
    "cli/modules-environment",
    "cli/jobs",
    "cli/storage-system",
    "cli/extra",

    // "tutorials/band-structure",
    "tutorials/band-gap",
    "tutorials/density-of-states",
    "tutorials/zero-point-energy",
    "tutorials/formation-energy",
    "tutorials/relaxation",
    "tutorials/kpt-convergence",
    "tutorials/combinatorial-screening",
    "tutorials/custom-input-workflow",
    "tutorials/electronic-density-mesh",
    "tutorials/fermi-surface",
    "tutorials/remote-desktop",
    "tutorials/cli-job",
    "tutorials/cli-job-import",

    "billing/settings-and-profile",
    "billing/billing-and-payments",
    // "billing/pricing-and-service-levels",
    "billing/storage-quota",
    "billing/add-credit-card",
    "billing/check-balance-quota",
    "billing/increase-balance",
    "billing/increase-quota",
    "billing/upgrade-service-level",

    "security/security-overview",
    "security/privacy-statement",
    // "security/data-security-in-transfer",
    // "security/data-security-at-rest",
    // "security/cli-users-permissions",
    // "security/data-ownership-and-visibility",

    "other/registration",
    // "other/roadmap",
    // "other/support",
    "other/faq",

    "terminology/simulations"
];

(function () {
    var checkInterval = 60000; // check login state every min
    var mainAppLoginURL = "https://platform.exabyte.io/login"; // non-logged-in go here
    /*
     * @summary Login state sharing with the main web application through cookies
     *          Expects webapp to have exabyte:login-state package installed.
     *          Checks for the presence of login-state cookie every minute.
     */
    var checkLoginState = function() {
        /**
         * @summary Gets cookie content by its name from the browser.
         *          Parses full cookies content.
         * @private
         * @param {String} name Cookie name, eg. for cookie `a=b` the name is `a`
         * @returns {String} Cookie content
         */
        function _getCookie(name) {
            var name = name + "=",
                cookies = document.cookie.split(';'),
                result = '';
            // loop over all cookies
            for (var i = 0; i < cookies.length; i++) {
                var c = cookies[i];
                while (c.charAt(0) == ' ') c = c.substring(1);
                if (c.indexOf(name) != -1) result = c.substring(name.length, c.length);
            }
            return result;
        }
        /**
         * @summary Returns cookie content or `false` depending on whether
         *          the entry for cookieName is present. The entry is expected
         *          to be set on login and removed on logout.
         * @public
         * @param {String} cookieName Cookie name, eg. for cookie `a=b` the name is `a`
         * @returns {Boolean} login state
         */
        function _getLoginState(cookieName) {
            var loginState = _getCookie(cookieName);
            if (loginState) {
                return JSON.parse(decodeURIComponent(loginState));
            } else {
                return false;
            }
        };
        // retrieve the login state
        var loginState = _getLoginState("logged-in-to-exabyte.io");
        if (loginState) {
            // the user is logged in into the web app
            return true;
        } else {
            // user is not loggedIn
            return false;
        }
    };
    /**
     * @summary Redirect to a login page if the url is private
     *          Parses url.
     * @private
     * @param {String} url
     * @param {jQuery event} event - used to get click target
     */
    function _redirectIfPrivate(url, event) {
        var _loggedIn = checkLoginState();
        if (new RegExp(PRIVATE_URLS.join("|")).test(url)) {
            event && event.preventDefault();
            // Only redirect in production:
            if (!window.location.hostname.includes("localhost") && !_loggedIn) {
                window.location.href = "/restricted";
            } else {
                console.log("Redirect statement ignored on localhost. Login status: ", _loggedIn);
            }
        }
    }
    // fire the check on document ready
    $(document).ready(function() {
        _redirectIfPrivate(window.location);
        $('body').click(function (event) {
            var target = $(event.target);
            if ( target.is( "a" ) ) {
                _redirectIfPrivate($(target).attr('href'), event);
                console.log($(target).attr('href'));
            }
        });
    });
})();

