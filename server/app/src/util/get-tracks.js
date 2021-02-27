import { audioFolder } from './common/constants';

var trackArray = [
    { name: "Chasha646", link: "chasha646.mp3" },
    { name: "Moment", link: "moment.mp3" },
    { name: "Pereliot", link: "perelet.mp3" },
    { name: "Prostory", link: "prostori.mp3" },
    { name: "Chushaama Ashuch", link: "chushaama ashuch.mp3" },
    { name: "Liquid Loud Sky Stereo Deep Dream", link: "liquid loud sky stereo deep dream.mp3" }
];

var track = trackArray[0];

// $("div.tracks").html(function () {
//     var result = "";
//     trackArray.forEach(track => {
//         result += "<p>" + track.name + "</p>\n<audio src=\"" + audioFolder + track.link + "\" controls></audio>"
//     })
//     return result;
// });

function ViewTrackName() {
    return <p>{track.name}</p>
}

function ViewAudio(audioFolder, trackLink) {
    <audio src={audioFolder + trackLink} controls></audio>
}

const domContainer = document.querySelector('#tracks');
ReactDOM.render(ViewTrackName(), domContainer);