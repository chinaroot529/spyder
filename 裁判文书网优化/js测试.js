function n(a, b) {
    return new n.fn.init(a, b)
}
var DES3 = {
    iv: function() {
        return $.WebSite.formatDate(new Date(), "yyyyMMdd");
    }
};

function decrypt(b, c, a) {
    const CryptoJS = require('crypto-js');
    if (c) {
        return CryptoJS.enc.Utf8.stringify(CryptoJS.TripleDES.decrypt(b, CryptoJS.enc.Utf8.parse(c), {
            iv: CryptoJS.enc.Utf8.parse(a || DES3.iv()),
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        })).toString();
    }
    return "";
}

