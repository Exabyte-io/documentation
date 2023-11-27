/** Create dictionary-like object of URL search params.
 * @returns {URLSearchParams}
 */
function getURLParams() {
    return new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
}

/** Check whether URL component is encoded already.
 * @see [MDN]{@link https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent}
 * @param {String} x
 * @returns {boolean}
 */
function containsEncodedComponents(x) {
  // ie ?,=,&,/ etc
  return (decodeURI(x) !== decodeURIComponent(x));
}

/** Execute mkdocs search from URL query
 * @param searchToken - query key (default: `'searchText'`)
 */
function injectSearchFromURL(searchToken = "searchText") {
    const query = getURLParams();
    if (!query[searchToken]) return;

    // decode search term if possible
    const searchTerm = containsEncodedComponents(query[searchToken])
        ? decodeURIComponent(query[searchToken])
        : query[searchToken];

    // enter value in search field
    let inputEl = document.querySelector("input.md-search__input");
    const searchIcon = document.querySelector("label.md-icon--search")
    inputEl.focus();
    inputEl.setAttribute("value", searchTerm);

    // trigger key event with a delay (it seems, the focus takes some time)
    const keyEvent = new KeyboardEvent("keyup");
    const clickEvent = new MouseEvent("click");
    searchIcon.dispatchEvent(clickEvent);
    setTimeout(() => {
            inputEl.dispatchEvent(keyEvent)
        },
        1000
    );
}

document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
        injectSearchFromURL();
    }
}
