<?php
// php populate html table from mysql database
$hostname = "localhost";
$username = "root";
$password = "";
$databaseName = "dianesis";
// connect to mysql
$connect = mysqli_connect($hostname, $username, $password, $databaseName);
session_start();
// mysql select query
$query = "SELECT * FROM course";
// result for method one
$result1 = mysqli_query($connect, $query);
// result for method two
//$result2 = mysqli_query($connect, $query);
$dataRow = "";
while($row1 = mysqli_fetch_array($result1))
{
    $dataRow = $dataRow."<tr><td>$row1[0]</td><td>$row1[1]</td><td>$row1[2]</td><td>$row1[3]</td><td>$row1[4]</td><td><button class='button enroll_btn' data-courseid=$row1[0]>Enroll</button></td></tr>";
  //  echo "               ";
    echo "\r\n";
    echo "$row1[0]";
  //  print $row1['courseid'] . "<BR>";
}
/*
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>


$(document).ready(function(){
  $(".enroll_btn").click(function(){

  alert("Button was clicked and changed");
  var courseid = $(".enroll_btn").data("courseid");
  alert(courseid);
  });
});


</script>
*/



?>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>


    $(document).ready(function(){
      $(".enroll_btn").click(function(){

      alert("Button was clicked and changed");
      var courseid = $(".enroll_btn").data("courseid");
      alert(courseid);
      });
    });
    </script>
  </head>
  <body>

      <td>  <button class='enroll_btn' data-courseid="">Enroll</button></p> </td>


  </body>
</html>
