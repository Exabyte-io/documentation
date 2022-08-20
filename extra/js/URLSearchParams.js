function getURLParams() {
    return new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
}

// from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent
function containsEncodedComponents(x) {
  // ie ?,=,&,/ etc
  return (decodeURI(x) !== decodeURIComponent(x));
}

function injectSearchfromURL(searchToken = "searchText") {
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
        500
    );
}

document.onreadystatechange = () => {
    if (document.readyState === 'complete') {
        injectSearchfromURL();
    }
}


