$(document).ready(function() {
    $('.has-popover').popover({'trigger':'hover'});
});

$('form #id_home_link, form #id_away_link').change(function() {
    get_rating(); // where ajax magic happens
});

function get_rating() {
    var id_home_val = 0;
    var id_away_val = 0;
    console.log("in get_rating()"); // sanity check
    // check that both form fields are filled
    if ($('#id_home_link').val() !== "" && $('#id_away_link').val() !== "") {
        id_home_val = $('#id_home_link').val();
        id_away_val = $('#id_away_link').val();
        console.log("let's call ajax magic"); // sanity check
    $.ajax({
        type : "POST", // http method
        data : {
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
            id_home : id_home_val,
            id_away : id_away_val,
            }, // data sent with the post request
        // handle a successful response (json object from views.new_method())
        success : function(response) {
            $('#id_home').val(response.home);
            $('#id_away').val(response.away);
            console.log("Team " + response.home + " has rating " + response.home_rating); // log the returned json to the console
            console.log("Team " + response.away + " has rating " + response.away_rating); // log the returned json to the console
            // is div already visible?
            var home_rating_response = parseFloat(response.home_rating);
            if ($('#rating_div').length > 0) {
                if ($('#cb').is(':checked')) {
                    home_rating_response += 3.0;
                };
                $('#id_home_rating_before').val(home_rating_response);
                $('#id_away_rating_before').val(response.away_rating);
            } else {
                // if not, let's create a new one
            $("<div style='margin-top: 140px; float: right; width: 200px; height: 120px; background-color: #BBBBBB' id='rating_div'></div>").insertAfter("h3");
            $('<input />', { type: 'checkbox', id: 'cb' }).appendTo($('#rating_div'));
            $('<label />', { 'for': 'cb', text: "Применять бонус домашнего поля?" }).appendTo($('#rating_div'));
            $('<br>').appendTo($('#rating_div'));
            $('<input />', { type: 'checkbox', id: 'manual-edit-cb' }).appendTo($('#rating_div'));
            $('<label />', { 'for': 'manual-edit-cb', text: "Редактировать вручную?" }).appendTo($('#rating_div'));
            $('<br><span id="rating_diff"></span>').appendTo($('#rating_div'));
            };

            // and fill hidden fields
            $('#id_home_rating_before').val(home_rating_response);
            $('#id_away_rating_before').val(response.away_rating);

            // only after one ajax call we put an event on checkbox
            $('#cb').unbind('change').change(function() {
                var home_rating = parseFloat($('#id_home_rating_before').val());
                console.log("home_rating in #cb event: " + home_rating)
                var away_rating = parseFloat($('#id_home_rating_before').val());
                if ($('#cb').is(':checked')) {
                    home_rating += 3.0;
                    console.log("home_rating in #cb checked: " + home_rating)
                    $('#id_home_rating_before').val(home_rating);
                } else {
                    // remove bonus if cb is not checked
                    home_rating -= 3.0;
                    //console.log("home_rating in #cb non-checked: " + home_rating)
                    $('#id_home_rating_before').val(home_rating);
                };
                // maybe there's already scores presented? checkbox call
                if ($('#id_home_score').val() != "" && $('#id_away_score').val() != "") {
                    check_diff();
                };
            });

            // what if this match is non-rating? checkbox call
            $('#manual-edit-cb').unbind('change').change(function() {
                if ($('#manual-edit-cb').is(':checked')) {
                    console.log("fire!")
                    $('#id_home_rating_before')[0].readOnly = false;
                    $('#id_home_rating_after')[0].readOnly = false;
                    $('#id_away_rating_before')[0].readOnly = false;
                    $('#id_away_rating_after')[0].readOnly = false;
                };
            });

            // maybe there's already scores presented? ajax response call
            if ($('#id_home_score').val() != "" && $('#id_away_score').val() != "") {
                check_diff();
            };
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    };
};

$('#id_home_score, #id_away_score').change(function() {
    check_diff();
});

function check_diff() {
    console.log('in check_diff()') // sanity check
    // let's get current ratings
    var home_rating = parseFloat($('#id_home_rating_before').val());
    var away_rating = parseFloat($('#id_away_rating_before').val());
    // time to get to know a favorite
    var score = get_score();
    var rating_diff;
    if (home_rating >= away_rating) {
        console.log('favorite is ' + $('#id_home').val())
        var fav_score = score.home;
        var run_score = score.away;
        rating_diff = home_rating - away_rating;
        rating_result = rating(fav_score, run_score, rating_diff);
        put_rating(home_rating + rating_result.fav, away_rating + rating_result.run, rating_result.fav);
    } else {
        console.log('favorite is ' + $('#id_away').val())
        var fav_score = score.away;
        var run_score = score.home;
        rating_diff = away_rating - home_rating;
        rating_result = rating(fav_score, run_score, rating_diff);
        put_rating(home_rating + rating_result.run, away_rating + rating_result.fav, rating_result.fav);
    };
};

function rating(fav_score, run_score, rating_diff){
    var diff;
    if (fav_score > run_score) {
        // favorite won the game
        if (rating_diff > 10) {
            // rating was to big to exchange
            diff = 0;
        } else {
            diff = (1 - rating_diff / 10);
            if (fav_score - run_score > 15) {
                diff = diff * 1.5;
            };
        };
        return {'fav': Math.round(diff * 100) / 100, 'run': Math.round((0-diff) * 100) / 100}
    } else if (fav_score < run_score) {
        // favorite lost the game
        if (rating_diff > 10) {
            diff = 2;
        } else {
            diff = 1 + rating_diff / 10;
        };
        if (run_score - fav_score > 15) {
            diff = diff * 1.5;
        };
        return {'fav': Math.round((0-diff) * 100) / 100, 'run': Math.round(diff * 100) / 100}
    } else {
        // the game was drawn
        if (rating_diff > 10) {
            diff = 1;
        } else {
            diff = Math.round((rating_diff / 10) * 100) / 100;
        };
        return {'fav': Math.round((0-diff) * 100) / 100, 'run': Math.round(diff * 100) / 100}
    };
};

function get_score() {
    // get initial values if the form already has scores
    var home_score = $('#id_home_score').val();
    var away_score = $('#id_away_score').val();
    return {home: parseInt(home_score), away: parseInt(away_score)};
};

function put_rating(home, away, diff) {
    var home_rating = home;
    if ($('#cb').is(':checked')) {
        home_rating -= 3.0;
        var home_rating_before = parseFloat($('#id_home_rating_before').val());
        $('#id_home_rating_before').val(home_rating_before - 3.0)
    };
    $('#id_home_rating_after').val(Math.round(home_rating * 100) / 100);
    $('#id_away_rating_after').val(Math.round(away * 100) / 100);

    $("#rating_diff").text("Обмен баллами составил " + Math.round(diff * 100) / 100);
};
