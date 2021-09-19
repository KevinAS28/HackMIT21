$( document ).ready(function () {    
    var moods = "Fear"
    var randomSong = ""
    var currentSongURL = ""
    
    var angryList = ["mafia", "babel"]
    var happyList = ["coffee", "colorful", "inspiration", "jazzy", "spring"]
    var surpriseList = ["cookies", "magical", "marionette", "morning", "reunion", "simple"]
    var sadList = ["preview", "raindrops", "stone"]
    var fearList = ["impulse", "logic", "silent", "takehimout", "thrilling"]

    var audio = document.getElementById("myAudio")

    function moodToSong(mainMood) {
        if (mainMood == "Angry") {
            randomSong = "music/angry/" + angryList[Math.floor(Math.random() * 2)] + ".mp3"
        }
        else if (mainMood == "Happy") {
            randomSong = "music/happy/" + happyList[Math.floor(Math.random() * 5)] + ".mp3"     
        }
        else if (mainMood == "Surprise") {
            randomSong = "music/surprise/" + surpriseList[Math.floor(Math.random() * 6)] + ".mp3"
        }
        else if (mainMood == "Sad") {
            randomSong = "music/sad/" + sadList[Math.floor(Math.random() * 3)] + ".mp3"  
        }
        else if (mainMood == "Fear") {
            randomSong = "music/fear/" + fearList[Math.floor(Math.random() * 5)] + ".mp3"    
        }
        audio.setAttribute("src", randomSong)
    }

    // $('.fa-backward').on('click', function() {
    //     audio.pause();
    //     audio.play();
    // });

    $('.fa-play-circle').on('click', function() {
        audio.play();
    });

    $('.fa-pause-circle').on('click', function() {
        audio.pause();
    });

    audio.onended = function() {
        moodToSong(moods)
        audio.play()
    };

    // $('.fa-play-forward').on('click', function() {
    //     audio.pause()
    //     moodToSong(moods)
    //     audio.play()
    // });

    moodToSong(moods)

});