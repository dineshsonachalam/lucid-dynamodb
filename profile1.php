<?php
$hostname = "localhost";
$username = "root";
$password = "";
$databaseName = "dianesis";
// connect to mysql
$connect = mysqli_connect($hostname, $username, $password, $databaseName);
//session_start();
// mysql select query


// result for method one
session_start();
//$query ="SELECT * FROM `student` WHERE  id  =".$_SESSION['usr_id'].")";
$query = "(SELECT * FROM `student` WHERE  id  =".$_SESSION['usr_id'].")";
$result1 = mysqli_query($connect, $query);


echo "You are Welcome ". $_SESSION['usr_name'];

/*
$con=mysql_connect("localhost","root","");
if(!$con)
{
die("could not connect:".mysql_error());
}
mysql_select_db("manoj",$con);
*/
/*
$sql="select * from register where name = '".$_SESSION['user']."'";
$res=mysql_query($sql);
*/

 //echo "<tr> <th>User</th> <th>Records</th> <th>Last Name</th></tr>";
echo "<table border='0'>";
while($r=mysqli_fetch_array($result1))
{
  echo "<tr>"
    ."<td>"."Name :"."</td>"."<td>".$r['name'] ."</td>"
    ."<td>"."Email :"."</td>"."<td>".$r['email'] ."</td>"
    ."<td>"."Password :"."</td>"."<td>".$r['password'] ."</td>"
    ."<td>"."Department :"."</td>"."<td>".$r['dept'] ."</td>"
    ."<td>"."Date of Birth :"."</td>"."<td>".$r['dob'] ."</td>"
    ."<td>"."College :"."</td>"."<td>".$r['college'] ."</td>".
 "</tr>";
}
//echo"<tr>"."<td>"."Name :"."</td>"."<td>".$r['name'] ."</td>"."<td>"."Department :"."</td>"."<td>".$r['dept']."</td>"."<td>"."Email :"."</td>"."<td>".$r['email']."</td>"."</tr>";
//echo"<tr>"."<td>"."Department :"."</td>"."<td>".$r['dept']."</td>"."</tr>";
//echo"<tr>"."<td>"."Email :"."</td>"."<td>".$r['email']."</td>"."</tr>";
//echo"<tr>"."<td>"."Mobile Number :"."</td>"."<td>".$r['mobile']."</td>"."</tr>";
//echo"<tr>"."<td>"."Gender :"."</td>"."<td>".$r['sex']."</td>"."</tr>";
echo "</table>";
echo"<p align='right'><a href='logout.php'>Logout</a></p>";
mysqli_close($connect);
?>
