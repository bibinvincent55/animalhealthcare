<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body>
{% include "p2.html" %}
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <!--DWLayoutTable-->
  <tr>
    <td width="243" height="27">&nbsp;</td>
    <td width="760">&nbsp;</td>
    <td width="324">&nbsp;</td>
  </tr>
  <tr>
    <td height="319">&nbsp;</td>
    <td valign="top"><p><strong>Hospital Registration</strong></p>
      <form name="form1" method="post" action="hospitalreg2">
	  {% csrf_token %}
        <table width="398" border="0">
          <tr>
            <td width="172">Location</td>
            <td width="210">{{s1}}</td>
          </tr>
          <tr>
            <td>Place</td>
            <td>{{s1}}</td>
          </tr>
          <tr>
            <td>Pin</td>
            <td>{{s1}}</td>
          </tr>
          <tr>
            <td>Phone</td>
            <td>{{s1}}</td>
          </tr>
          <tr>
            <td>District</td>
            <td>{{s1}}</td>
          </tr>
          <tr>
            <td>Hospital Type </td>
            <td>{{s1}}</td>
          </tr>
          <tr>
            <td colspan="2"><strong>Successfuly Registered...The Staff ID is </strong>{{hospid}}</td>
          </tr>
        </table>
      </form>      <p>&nbsp; </p></td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="30">&nbsp;</td>
    <td>&nbsp;</td>
    <td>&nbsp;</td>
  </tr>
</table>
</body>
</html>
