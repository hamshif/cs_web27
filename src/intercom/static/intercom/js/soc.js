

$('document').ready(function()
{
    var _uri = 'ws://e-10:8000/ws/foobar?subscribe-broadcast&publish-broadcast&echo';
    var _heart = '--heartbeat--';


    console.log('Fanjabee', _uri);

    var ws4redis = WS4Redis({
		uri: _uri,
		receive_message: receiveMessage,
		heartbeat_msg: _heart
	});

	    // attach this function to an event handler on your site
    function sendMessage() {
        ws4redis.send_message('A message');
    }

    // receive a message though the websocket from the server
    function receiveMessage(msg) {
        alert('Message from Websocket: ' + msg);
    }

});