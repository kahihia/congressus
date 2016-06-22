function check_warning(w, sessions) {
    if (w.type == 'req') {
        var firstFound = true;
        var secondFound = true;
        var ss = [];
        w.sessions1.forEach(function(s1) { ss.push(s1); });
        w.sessions2.forEach(function(s2) { ss.push(s2); });

        for (var i=0; i<w.sessions1.length; i++) {
            if (sessions.indexOf(w.sessions1[i]) < 0) {
                firstFound = false;
            }
        }
        for (var i=0; i<w.sessions2.length; i++) {
            if (sessions.indexOf(w.sessions2[i]) < 0) {
                secondFound = false;
            }
        }

        if (firstFound && !secondFound) {
            return true;
        }

        return false;
    }
}

function seat_droped(session, layout, seat) {
    var selector = '#' + session + '_' + layout + '_' + seat;
    $(selector).addClass("seat-L");
    $(selector).removeClass("seat-H");
    $(selector).unbind("click").click(function() {
        SeatMap.clickSeat($(this));
    });
}

function seat_holded(session, layout, seat) {
    var selector = '#' + session + '_' + layout + '_' + seat;

    if ($(selector).hasClass("seat-selected")) {
        return;
    }

    $(selector).addClass("seat-H");
    $(selector).removeClass("seat-L");
    $(selector).unbind("click");
}

function seat_reserved(session, layout, seat) {
    var selector = '#' + session + '_' + layout + '_' + seat;
    $(selector).addClass("seat-R");
    $(selector).removeClass("seat-L");
    $(selector).removeClass("seat-H");
    $(selector).unbind("click");
}

function websocketCB(ev, data) {
    if (ev == 'hold') {
        var seat = data.row + '_' + data.col;
        seat_holded(data.session, data.layout, seat);
    } else if (ev == 'drop') {
        var seat = data.row + '_' + data.col;
        seat_droped(data.session, data.layout, seat);
    } else if (ev == 'confirm') {
        var seat = data.row + '_' + data.col;
        seat_reserved(data.session, data.layout, seat);
    }
}

function seatCB(ev, seat) {
    var row = seat.data("row");
    var col = seat.data("col");
    var session = seat.data("session");
    var layout = seat.data("layout");

    var current = [];
    var currentval = $("#seats-"+session).val();
    if (currentval) {
        current = currentval.split(",");
    }

    var str = layout + '_' + row + '_' + col;

    args = session;
    args += ' ' + layout;
    args += ' ' + row;
    args += ' ' + col;
    args += ' ' + client;

    if (ev == 'select') {
        current.push(str);
        ws.send('hold_seat ' + args);
    } else if (ev == 'unselect') {
        var idx = current.indexOf(str);
        if (idx >= 0) {
            current.splice(idx, 1);
        }
        ws.send('drop_seat ' + args);
    }

    $("#seats-"+session).val(current.join(","));
    $("#"+session).val(current.length);

    updateBadges(session, layout);

    $("#"+session).change();
}

function updateBadges(session, layout) {
    //updating the label with the number of selected seats
    var currentval = $("#seats-"+session).val();
    var current = currentval.split(",");
    var n = 0;
    current.forEach(function(element) {
        if (element.startsWith(layout + '_')) {
            n++;
        }
    });
    badge = $("#badge-"+session+"-"+layout);
    badge.text(n);
    if (n) {
        badge.addClass("label-success");
        badge.removeClass("label-default");
    } else {
        badge.removeClass("label-success");
        badge.addClass("label-default");
    }
}

function recalcSums(obj) {
    var session = obj.attr("id");
    var val = parseInt(obj.val(), 10);
    var price = parseFloat(obj.data("price"));
    $("#"+session+"-subtotal-price").html(val * price);
}

function recalcTotal() {
    var sum = 0;
    $(".sessioninput").each(function() {
        var n = parseInt($(this).val(), 10);
        var price = parseFloat($(this).data("price"));
        sum += price * n;
    });
    $("#total").html(sum);
}

function fillSelectedSeats(obj) {
    // obj should be a .seats-input
    var session = obj.data('session');
    var v = obj.val();
    if (v) {
        var current = [];
        current = v.split(",");
        $("#"+session).val(current.length);
        $("#"+session).change();

        function recursiveSelection(arr, finish) {
            var c = arr.pop();
            var selector = '#' + session + '_' + c;
            var layout = c.split('_')[0];
            var l = $('.layout-'+session+'-'+layout);
            var obj = $('.display-'+session+'-'+layout);

            SeatMap.preloadLayout(l, obj, function() {
                $(selector).addClass("seat-selected");
                if (arr.length) {
                    recursiveSelection(arr, finish);
                } else {
                    finish();
                }
            });
        }

        recursiveSelection(current.slice(0), function() {
            current.forEach(function(c) {
                var layout = c.split('_')[0];
                updateBadges(session, layout);
            });
        });
    }
}

function autoSelectSeat(s, n) {
    autoSeats(s, n).then(function(autoseats) {
        var value = [];
        autoseats.forEach(function(obj) {
            value.push(obj.layout+"_"+obj.row+"_"+obj.col);

            args = s;
            args += ' ' + obj.layout;
            args += ' ' + obj.row;
            args += ' ' + obj.col;
            args += ' ' + client;
            ws.send('hold_seat ' + args);
        });
        $("#seats-"+s).val(value.join(","));
        fillSelectedSeats($("#seats-"+s));
    });
}

function seatsChange() {
    // this should be a .sessioninput
    recalcSums($(this));
    recalcTotal();

    // if no name in the input, it's a numbered session
    // we do here the seat auto selection
    if (!$(this).attr("name")) {
        var val = $(this).val();
        var s = $(this).data('session');
        var v = $("#seats-"+s).val();
        if (!v) {
            autoSelectSeat(s, val);
        } else {
            var current = [];
            current = v.split(",");
            if (current.length != val) {
                // unselecting all selected
                current.forEach(function(c) {
                    selector = '#' + s + '_' + c;
                    $(selector).removeClass('seat-selected');

                    a = c.split('_');
                    args = s;
                    args += ' ' + a[0];
                    args += ' ' + a[1];
                    args += ' ' + a[2];
                    args += ' ' + client;
                    ws.send('drop_seat ' + args);
                });
                $("#seats-"+s).val("");

                autoSelectSeat(s, val);
            }
        }
    }
}

$(document).ready(function() {
    $("form").submit(function() {
        var warnings = [];
        var sessions = [];

        $('.sessioninput').each(function() {
            val = parseInt($(this).val(), 10);
            id = $(this).attr("id");
            if (val) {
                sessions.push(id);
            }
        });

        $('.warning').each(function() {
            var warning = {};
            warning.name = $(this).data('name');
            warning.sessions1 = String($(this).data('sessions1')).split(',');
            warning.sessions2 = String($(this).data('sessions2')).split(',');
            warning.type = $(this).data('type');
            warning.message = $(this).data('message');
            warnings.push(warning);
        });

        for(var i=0; i<warnings.length; i++) {
            var w = warnings[i];
            if (check_warning(w, sessions)) {
                return confirm(w.message);
            }
        }

        return true;
    });

    $('.withtooltip').tooltip();

    $(".seatmap").each(function() {
        var session = $(this).data('session');
        var obj = $("#modal-" + session);
        SeatMap.bindLayout(obj);
    });

    SeatMap.cbs.add(seatCB);
    ws.cbs.add(websocketCB);

    $(".seats-input").each(function() {
        fillSelectedSeats($(this));
    });

    // calculating sums
    $('.sessioninput').change(seatsChange);
    $('.sessioninput').keyup(seatsChange);
    recalcTotal();

    $('.sessioninput').each(function() {
        recalcSums($(this));
        $(this).click(function() { $(this).select(); });
    });
});
