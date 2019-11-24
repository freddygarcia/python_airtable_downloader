
var spinner = (function () {
    return {
        show: function () {
            $('.spinner').removeClass('d-none');
            $('form submit').attr('disabled', true)
        },
        hide: function () {
            $('.spinner').addClass('d-none')
            $('form submit').attr('disabled', false)
        }
    }
})()

function clean() {
    $('.alert-panel').remove();
    $('.list-group-item').remove();
}

function successResponse(response) {

    var list_group = $('.list-group');
    var arr = []

    for (document_id in response) {
        var document = response[document_id];
        arr.push({ 'name': document, id: document_id })
    }

    arr = arr.sort(function (a, b) {
        if (a.name > b.name) {
            return -1;
        }
        if (b.name > a.name) {
            return 1;
        }
        return 0;
    });
    arr.forEach(function (document) {
        list_group.append($(
            '<a href="/file/' + document.id + '" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">' + document.name +
                '<span class="badge badge-primary badge-pill"><i class="fas fa-download"></i></span>' +
            '</a>'
        )
        )
    })
}

function badResponse(response) {

    var text = response.content;
    if (response.code == 404) text = 'BASE ID was not found';
    var section = $('section');
    var alert = $(
        '<div class="alert-panel col-md-12 mt-5">' +
            '<div class="alert alert-warning" role="alert">' +
                '<strong class="">Code: ' + response.code + '</strong> ' +
                text +
            '</div>' +
        '</div>'
    )
    section.append(alert);
}

function getDocuments() {
    var form = $('form');

    form.submit(function (e) {
        e.preventDefault();
        clean();

        var key = $('#key').val();
        var base = $('#base').val();

        var payload = {
            key: key,
            base: base
        };

        spinner.show();

        $.post('/files', payload, function (response, cc) {
            successResponse(response)
        }).fail(function (response) {
            var res = {
                content: response.responseText,
                code: response.status,
            }
            badResponse(res)
        }).always(function () {
            spinner.hide();
        })
    })
}

$(document).ready(getDocuments)