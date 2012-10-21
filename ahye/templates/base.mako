<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta charset="utf-8">
        <title>ah ye</title>
        ${self.head_css()}
        ${self.head_js()}
    </head>
    <body>
        <div id="header">
            ${self.body_header()}
        </div>
        <div id="page_container">
            ${self.body_content()}
        </div>
        <div id="footer">
            ${self.body_footer()}
        </div>
        ${self.footer_js()}
    </body>
</html>

<%def name="head_css()">
    <link rel="stylesheet" type="text/css" href="${url_for('static', filename='css/base.css')}" />
</%def>

<%def name="head_js()">
</%def>

<%def name="body_header()">
</%def>

<%def name="body_content()">
</%def>

<%def name="body_footer()">
</%def>

<%def name="footer_js()">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"></script>
    <script src="/static/js/jquery.ui.widget.js"></script>
    <script src="/static/js/jquery.iframe-transport.js"></script>
    <script src="/static/js/jquery.fileupload.js"></script>
    <script>
    $(function () {
        $('#fileupload').fileupload({
            dataType: 'json',
            singleFileUploads: false,
            done: function (e, data) {
                var html = '<div class="results">';
                $.each(data.result, function (index, file) {
                    html += '<div class="file">';
                    html += '<a href="'+file.url+'" target="_blank">';
                    html += '<img src="'+file.url+'" width="40px" height="40px"/>'
                    html += file.name+'</a>';
                    html += '</div>';
                });
                html += '</div>';
                var logodiv = $('#screen');
                logodiv.addClass('showing_results');
                logodiv.html(html);
            }
        });
    });
    </script>
</%def>