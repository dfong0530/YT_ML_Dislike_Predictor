function convertToShorthand(number) {
    var absNumber = Math.abs(number);
    var shorthand;

    if (absNumber >= 1000000) {
        shorthand = (number / 1000000).toFixed(1).replace('.0', '') + "m";
    } else if (absNumber >= 1000) {
        shorthand = (number / 1000).toFixed(1).replace('.0', '') + "k";
    } else {
        shorthand = number.toString();
    }

    return shorthand;
}



function main() {
    // Send a message to the content script asking for the video ID
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { method: "getVideoId" }, function (response) {
            if (response.videoId) {
                fetch('https://ml-yt-api.fly.dev/get_video_data/' + response.videoId)
                    .then(res => res.json())
                    .then(data => {
                        let dislikeCount = document.getElementById('dislikeCount');
                        let dislikes = convertToShorthand(data["dislike_count"]);

                        dislikeCount.textContent = dislikes;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        let dislikeCount = document.getElementById('dislikeCount');
                        dislikeCount.textContent = 'Error retrieving dislike count';
                    });
            } else {
                let dislikeCount = document.getElementById('dislikeCount');
                dislikeCount.textContent = 'Not a YouTube video page';
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', main);



