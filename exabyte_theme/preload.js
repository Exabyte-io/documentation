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
            // re-start the check again in 1 min
            setTimeout(checkLoginState, checkInterval);
        } else {
            // user is not loggedIn -> goto web app login
            window.location = mainAppLoginURL;
        }
    };
    // fire the check
    checkLoginState();
})();
