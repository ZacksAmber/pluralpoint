<?php

  $id = $_GET['1'];
  // do some validation here to ensure id is safe

  $link = mysql_connect("mysql-xtr.c9d5goyg8g3a.us-east-1.rds.amazonaws.com", "admin", "myPassWord_123");
  mysql_select_db("xtrdb");
  $sql = "SELECT Photo FROM Employee WHERE `Employee ID`=$id";
  $result = mysql_query("$sql");
  $row = mysql_fetch_assoc($result);
  mysql_close($link);

  header("Content-type: image/jpeg");
  echo $row['Photo'];
?>