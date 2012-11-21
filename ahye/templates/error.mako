<%inherit file="base.mako"/>

<%def name="body_content()">
    <div id="screen" class="blank">
        <div class="text_container">
            <div class="error_msg">
                The remote server returned a 
            </div>
            <div class="error_code">
                <a href="http://en.wikipedia.org/wiki/HTTP_${code}" target="_new">${code}</a>
            </div>
            <div class="error_msg">
                Sorry!
            </div>
        </div>
    </div>
</%def>