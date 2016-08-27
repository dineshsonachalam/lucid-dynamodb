<?php
$q = $_GET['q'];


$hostname = "localhost";
$username = "root";
$password = "";
$databaseName = "dianesis";
// connect to mysql
$connect = mysqli_connect($hostname, $username, $password, $databaseName);
session_start();
//echo $_SESSION['usr_id'];
/* mysql select query
$query = "SELECT * FROM enrollmentfact";
// result for method one

$result1 = mysqli_query($connect, $query);
// result for method two
//$result2 = mysqli_query($connect, $query);
$dataRow = "";
echo "got into getuser.php page";
*/
$sql="INSERT INTO `enrollmentfact`(`course_id`, `student_id`) VALUES ('".$q."','".$_SESSION['usr_id']."')";
if (mysqli_query($connect, $sql)) {

  //  alert("Enrolled successfully");
      echo "Enrolled successfully";
  //  echo "<html><body><p>New record created successfully</p></body></html>";
} else {
  //  echo "Error: " . $sql . "<br>" . mysqli_error($connect);
      echo "Enrollment failed";
}

mysqli_close($connect);


//$result2=mysqli_query($connect,"INSERT INTO `enrollmentfact`(`course_id`, `student_id`) VALUES ('".$q."','".$_SESSION['usr_id']."')");


?>
