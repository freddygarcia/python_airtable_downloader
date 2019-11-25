
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

    var file_list_group = $('.file-list-group');

    for (document_type in response) {
        var documents = response[document_type];
        var list_group = $(
            '<div class="list-group list-group-flush my-5"> \
                <a class="list-group-item list-group-item-secondary">' + document_type + '</a>\
            </div>');

        var arr = []

        for (document_id in documents) {
            var doc = documents[document_id];
            arr.push({ 'name': doc.name, id: document_id })
        }

        // sort array by filename 
        arr = arr.sort(function (a, b) {
            if (a.name > b.name) {
                return -1;
            }
            if (b.name > a.name) {
                return 1;
            }
            return 0;
        });

        arr.forEach(function (doc) {
            list_group.append($(
                '<a href="/file/' + doc.id + '" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center ">' + doc.name +
                    '<span class="badge badge-secondary badge-pill"><i class="fas fa-download"></i></span>' +
                '</a>'
            ))
        })
        file_list_group.append(list_group);
    }
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