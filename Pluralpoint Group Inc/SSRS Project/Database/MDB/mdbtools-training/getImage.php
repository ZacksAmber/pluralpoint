<?php
  $servername = "mysql-xtr.c9d5goyg8g3a.us-east-1.rds.amazonaws.com";
  $username = "admin";
  $password = "myPassWord_123";
  $dbname = "xtrdb";
  
  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);

  // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully";

  #$id = $_GET['id'];
  $id = 1; 
  // do some validation here to ensure id is safe
  
  #$sql = "SELECT id, firstname, lastname FROM MyGuests";
  $sql = "SELECT Photo FROM Employee WHERE `Employee ID`=$id";
  
  $result = mysqli_query($conn, $sql);
  #$result = mysqli_query("$sql");
  
  $row = mysqli_fetch_assoc($result);
  mysqli_close($conn);

  #Header('Content-Type:image/bmp');
  #echo $row['Photo'];

  $im = $row;

  // Create a blank image and add some text
  $im = imagecreatetruecolor(120, 20);
  $text_color = imagecolorallocate($im, 233, 14, 91);
  imagestring($im, 1, 5, 5,  'A Simple Text String', $text_color);

  // Set the content type header - in this case image/vnd.wap.wbmp
  // Hint: see image_type_to_mime_type() for content-types
  header('Content-Type: image/vnd.wap.wbmp');

  // Output the image
  imagewbmp($im);
  echo imagewbmp($im);

  // Free up memory
  imagedestroy($im);

?>