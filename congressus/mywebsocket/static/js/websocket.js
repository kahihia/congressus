(function() {
    var ws = window.ws = {};
    ws.socket = null;
    ws.cbs = $.Callbacks();

    ws.init = function(server) {
        var protocol = "ws:";
        if (window.location.protocol === "https:") {
            protocol = "wss:";
        }

        ws.socket = new WebSocket(protocol + "//" + server);
        ws.socket.onmessage = function(ev) {
            var data = JSON.parse(ev.data);
            if (data.action) {
                ws.cbs.fire(data.action, data);
            } else {
                ws.cbs.fire('msg', ev);
            }
        };
        ws.socket.onopen = function (ev) { ws.cbs.fire('open', ev); };
        ws.socket.onclose = function (ev) {
            console.log("websocket closed");
            console.log(ev);
            ws.cbs.fire('close', ev);

            //reloading
            setTimeout(function() { ws.init(server); }, 1000);
        };
        ws.socket.onerror = function (ev) {
            console.log("websocket error");
            console.log(ev);
            ws.cbs.fire('error', ev);
        };
    };

    ws.send = function(msg) {
        try {
            ws.socket.send(msg);
        } catch (e) {
            // no websocket, continuing anyway
            console.log("Can't send messasge to websocket");
        }
    };
}).call(this);
