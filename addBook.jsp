<%@ page language="java" import="java.util.*" pageEncoding="gb2312"%>
<%@page import="mybean.model.bookBean" %>   
<jsp:useBean id="login" class="mybean.model.loginBean" scope="session"/>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'addBook.jsp' starting page</title>
    
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<link href="css/layout.css" rel="stylesheet" type="text/css" />
  </head>
    <body>
    <div id="container">
  <div id="header"><%@include file="bodyFile/head.txt" %></div>
  <div id="mainContent">
    <div id="sidebar" align="center">
    <img src="image/2.gif"  align="left" width=50 height=50 padding-right=2px />
    <img src="image/2.gif"  align="right" width=50 height=50 padding-right=2px />
      <p><font size=2 ><%="ID:"+login.getLoginName() %> </font></p> 
        <%@include file="bodyFile/left1.txt" %>
    </div>
    <div id="content">
      <div align="center"><p>&nbsp;</p>
        <font size=4 color=blue>
                             新书入库
        </font>
        <p>
        <form  method="post" name=form action="adminAddBook" >
        <p>
                             图书书号：
           <input type="text"  onkeyup="this.value=this.value.replace(/[, ]/g,'')" name="bookID" size="26"  />
             <font size="2" color="red"> *请输入有效书号</font>
        <p>
                            图书书名：
           <input name="bookName" type="text" size="27" /> 
           <font size="2" color="red"> *请输入有效书名</font>
        <p>     
                            图书作者：
           <input name="bookAuthor" type="text" size="27" />
           <font size="2" color="red"> *请输入有效人名</font>
        <p>
                             出版社名：
           <input name="bookPublish" type="text" size="27" />
          <font size="2" color="red"> *请输入有效社名</font>
         <p>  
                               图书类别：
           <input name="bookType" type="text" size="27" />
           <font size="2" color="red"> *请输入有效类别</font>
         <p> 
                            库存数量：
                <input name="bookNum" maxlength="3" onkeyup="value=value.replace(/[^\d]/g,'') "onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\d]/g,''))" type="text" size="27" />
         <font size="2" color="red"> *请输入 库存数量</font>
         <p>
        <input type="submit" name="submit" value="添加" />
        </form>
        <%
          if(session.getAttribute("reader")!=null){
        %>
        <jsp:useBean id="addbook"  scope="session" class="mybean.model.bookBean"/>
        <font size=2 color=red>
         
         <jsp:getProperty name="addbook" property="resultMessage"/>  
        </font>
        <%} %>
       </div>
    </div>
  </div>
  <div id="footer"><%@include file="bodyFile/footer.txt" %></div>
</div>
  </body>
</html>
