<%inherit file="base.mako"/>

<%def name="extra_js()">
    <script src="/static/js/jquery.colorbox-min.js"></script>
    <script>
        var html = "<b>here's how to do it</b>"
        $("#mirror_helplink").colorbox({"html": $(".mirror_help_container").html()});
    </script>
</%def>

<%def name="extra_css()">
    <link rel="stylesheet" type="text/css" href="${url_for('static', filename='css/colorbox.css')}" />
</%def>

<%def name="body_content()">
    <div id="screen" class="fade">
        <div class="mirror_helplink"><a id="mirror_helplink" href="#">How do I mirror a file?</a></div>
    </div>
    <input id="fileupload" type="file" name="files[]" data-url="/webupload" multiple>
    <div class="mirror_help_container hidden">
        <div class="mirror_help">
            <h3>Mirroring</h3>
            <p>To mirror a file, simply append its URL to the ahye server's URL.</p>

            <p>For example, if you wanted to mirror the image at http://i.imgur.com/EHWlL.jpg, you would simply go to the url:</p>
            <p>${base_url}/http://i.imgur.com/EHWlL.jpg</p>
            <p>You'll then be automatically redirected to the mirrored version of the image!</p>
        </div>
    </div>
</%def>
