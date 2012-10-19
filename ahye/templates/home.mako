<%inherit file="base.mako"/>

<%def name="body_content()">
    <img src="${url_for('static', filename='img/logo.png')}" id="logo"/>
    <h2 id="subtext">drag images here to upload!</h2>
</%def>