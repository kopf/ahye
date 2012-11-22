<%inherit file="base.mako"/>
<%def name="body_content()">
    <div id="screen" class="blank">
        <div class="text_container">
            <div class="error_msg">
                % if error.get('code'):
                    The remote server returned a 
                % elif error.get('msgs'):
                    ${'<br>'.join(error['msgs'])}
                % else:
                    An unknown error occured.
                % endif
            </div>
            % if error.get('code'):
                <div class="error_code">
                    <a href="http://en.wikipedia.org/wiki/HTTP_${error['code']}" target="_new">${error['code']}</a>
                </div>
                <div class="error_msg">
                    Sorry!
                </div>
            % endif
        </div>
    </div>
</%def>
