<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
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
    <link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:700' rel='stylesheet' type='text/css'>
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
</%def>