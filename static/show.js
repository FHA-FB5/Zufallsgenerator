let websocket = new WebSocket('ws://localhost:6666');

websocket.onmessage = function (event) {
    let message = JSON.parse(event.data);
    let stage = document.getElementById('stage');
    switch (message.type){
        case 'start':
            stage.textContent = 'Running';
            break;
        case 'stop':
            stage.textContent = 'Winner is ' + message.winner;
            break;
        default:
            console.error('Invalid message type')
    }
};