<%inherit file="base.mako"/>

<%def name="body_content()">
    <div id="screen" class="fade">
    </div>
    <input id="fileupload" type="file" name="files[]" data-url="/webupload" multiple>
</%def>