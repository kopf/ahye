<%inherit file="base.mako"/>

<%def name="extra_js()">
    <script src="/static/js/jquery.colorbox-min.js"></script>
    <script>
        var html = "<b>here's how to do it</b>"
        $("#mirror_helplink").colorbox({
            "html": $(".mirror_help_container").html(),
            "width": "440px",
            "height": "445px",
            "close": "<img src='${url_for('static', filename='img/colorbox/close.png')}' />"
        });
    </script>
</%def>

<%def name="extra_css()">
    <link rel="stylesheet" type="text/css" href="${url_for('static', filename='css/colorbox.css')}" />
</%def>

<%def name="body_content()">
    <div id="screen" class="fade">
        <div class="mirror_helplink text_shadow">
            <a id="mirror_helplink" href="#">How do I mirror a file?</a>
        </div>
    </div>
    <input id="fileupload" type="file" name="files[]" data-url="/webupload" multiple>
    <div class="mirror_help_container hidden">
        <div class="mirror_help text_shadow">
            <h2>Mirroring</h2>
            <p>To mirror a file, simply append its URL to the ahye server's URL.</p>

            <p>For example, if you wanted to mirror the image at <a href="http://i.imgur.com/EHWlL.jpg" target="_new">http://i.imgur.com/EHWlL.jpg</a>, you would simply go to the url:</p>
            <p class="example_url"><a href="${base_url}/http://i.imgur.com/EHWlL.jpg" target="_new">${base_url}/http://i.imgur.com/EHWlL.jpg</a></p>
            <p>You'll then be automatically redirected to the mirrored version of the image!</p>
        </div>
    </div>
</%def>
