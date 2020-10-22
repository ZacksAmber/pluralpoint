<?php
$servername = "mysql-xtr.c9d5goyg8g3a.us-east-1.rds.amazonaws.com";
$username = "admin";
$password = "myPassWord_123";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>

