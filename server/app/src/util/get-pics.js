import { pictureUrl, imageFolder } from './common/constants';
import { httpGet } from './common/requests';

var imageArray = JSON.parse(httpGet(pictureUrl));

$("div.images").html(function () {
    var result = "";
    imageArray.forEach(image => {
        result += "<img src=\"" + imageFolder + image.link + "\" height=\"50%\" width=\"50%\" />"
    })
    return result;
});