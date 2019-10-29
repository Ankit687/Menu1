#!/usr/bin/python36
print("content-type: text/html")
print()
string = ""

print("Hello world")

print(""" 
<html>
    <body>
        <script>
            function voice_act(){
            var msg = new SpeechSynthesisUtterance('Hello World');
            window.speechSynthesis.speak(msg);
            document.write("1. Configure a web server on LAN<br>\
        2. Configure a web server on AWS<br>\
        3. Start a service<br>\
        4. Stop a service<br>\
        5. Launch firefox<br>\
        6. Launch gedit<br>\
        7. Create partitons on disk<br>\
        8. Create a logical volume<br>\
        9. Configure yum on local or remote machine<br>\
        10. Create a hadoop cluster<br>\
        11. Launch an EC2 instance<br>\
        12. Launch an S3 bucket<br>\
        13. Send an email<br>\
        14. Exit<br>");

        var msg = new SpeechSynthesisUtterance("Enter your command");
        window.speechSynthesis.speak(msg);
        var inp = document.createElement("input");
        inp.setAttribute("type", "text");
        inp.id = "command"
        var body = document.querySelector('body');
        body.appendChild(inp);
        document.getElementById('command').value = "Nandini";
        take_input();
        }

        
        function take_input(){

            window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
            let finalTranscript = '';
            let recognition = new window.SpeechRecognition();
            recognition.interimResults = true;
            recognition.maxAlternatives = 10;
            recognition.continuous = true;
            recognition.onresult = (event) => {
            let interimTranscript = '';
            for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
                let transcript = event.results[i][0].transcript;
                if (event.results[i].isFinal) {
                    finalTranscript += transcript;
                } else {
                    interimTranscript += transcript;
                }
            }
            // document.querySelector('body').innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</>';
            document.getElementById('command').value = finalTranscript + interimTranscript;
            }
            recognition.start();
        }
        </script>
        <button onclick="voice_act()">Show menu</button>
    </body>
</html>
""")

