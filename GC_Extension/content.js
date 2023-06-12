chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.method === "getVideoId") {
        const urlParams = new URLSearchParams(window.location.search);
        sendResponse({ videoId: urlParams.get('v') });
    }
});
