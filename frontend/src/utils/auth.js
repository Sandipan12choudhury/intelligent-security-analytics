const TOKEN_KEY = "isap_auth_token";

export function getToken() {

    return localStorage.getItem(TOKEN_KEY);

}

export function setToken(token) {

    localStorage.setItem(TOKEN_KEY, token);

}

export function clearToken() {

    localStorage.removeItem(TOKEN_KEY);

}

function base64UrlDecode(str) {

    let base64 = str.replace(/-/g, "+").replace(/_/g, "/");

    while (base64.length % 4) {

        base64 += "=";

    }

    return atob(base64);

}

// Checks not just that a token exists, but that it hasn't expired.
// A JWT's payload (the middle segment) carries its own expiry ("exp")
// as a Unix timestamp - decoding it client-side lets us catch a
// stale/expired token immediately instead of only finding out when
// an API call comes back 401.

export function isAuthenticated() {

    const token = getToken();

    if (!token) {

        return false;

    }

    try {

        const payload = JSON.parse(base64UrlDecode(token.split(".")[1]));

        if (payload.exp && payload.exp * 1000 < Date.now()) {

            clearToken();

            return false;

        }

        return true;

    } catch {

        clearToken();

        return false;

    }

}

export function authHeaders() {

    const token = getToken();

    return token ? { Authorization: `Bearer ${token}` } : {};

}
