$.ajax({
    type: 'GET',
    url: '/practice_questions'
}).done(function(data) {
    console.log(data);
    $("#images_holder").html("<img src=" + data["url"] + " alt='placeholder' width='300px';>")
    $("#keywords").html("<h1 style='color: #000'><b>" + data["keyword"] + "</b></h1>");
    $("#questions").html("<h2>" + data["translated"] + "</h2>");
    $("#translation").html("<h2><b>Translated: </b>" + data["sentence"] + "</h2>");
    $("#audioslave").html("<source src=" + data["audio_path"] + " type='audio/wav'>");
});

function regenerate() {
  $.ajax({
      type: 'GET',
      url: '/practice_questions'
  }).done(function(data) {
      console.log(data);
      $("#images_holder").html("<img src=" + data["url"] + " alt='placeholder' width='300px';>")
      $("#keywords").html("<h1 style='color: #000'><b>" + data["keyword"] + "</b></h1>");
      $("#questions").html("<h2>" + data["translated"] + "</h2>");
      $("#translation").html("<h2><b>Translated: </b>" + data["sentence"] + "</h2>");
      $("#audioslave").html("<source src=" + data["audio_path"] + " type='audio/wav'>");
  });
}

var user1 = [];
var user2 = [];

var record = document.querySelector('.record');
var stop = document.querySelector('.stop');
var soundClips = document.querySelector('.sound-clips');

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    console.log('getUserMedia supported.');
    // constraints - only audio needed for this app
    navigator.mediaDevices.getUserMedia ({ audio: true })
    // Success callback
    .then(function(stream) {
      var mediaRecorder = new MediaRecorder(stream);

    record.onclick = function() {
      mediaRecorder.start();
      console.log(mediaRecorder.state);
      console.log("recorder started");
      record.style.background = "red";
      record.style.color = "black";
    }

    var chunks = [];

    mediaRecorder.ondataavailable = function(e) {
        chunks.push(e.data);
    }

    stop.onclick = function() {
        mediaRecorder.stop();
        console.log(mediaRecorder.state);
        console.log("recorder stopped");
        record.style.background = "";
        record.style.color = "";
    }

    mediaRecorder.onstop = function(e) {
        console.log("recorder stopped");

        var clipName = 'Enter a name for your sound clip';

        var blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
        chunks = [];

        var audioURL = window.URL.createObjectURL(blob);

        var form = new FormData();
        form.append('file', blob, clipName);
        form.append('title', "hi");

        $.ajax({
          type: 'POST',
          url: '/speech',
          data: form,
          cache: false,
          processData: false,
          contentType: false
        }).done(function(data) {

            var string1 = $("#questions").text().toUpperCase().trim().replace(/\./g, "");
            console.log("string1");
            console.log(string1);

            var string2 = JSON.stringify(data["user_voice"]).toUpperCase().trim().replace(/\"/g, "").replace(/\s+$/, "");
            console.log("string2");
            console.log(string2);

            var is_equal = (string1 === string2);
            console.log(is_equal);

            var kw = $("#keywords").text();

            if (is_equal == true) {

              user1.push(kw);

              if (user1.length === 1) {
                $("#user1 li").text(kw);
              } else {
                $("#user1").append("<li class='tick'>" + kw + "</li>");
              }

            } else {
              user2.push(kw);
            }

            console.log(user1);
            console.log(user2);

        });
    }

}).catch(function(err) { // Error callback
   console.log('The following gUM error occured: ' + err);
}); } else {
    console.log("lol");
}
