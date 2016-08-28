

<html>
<head>
<style type="text/css">
td
{
  padding:5px;
  border:1px solid #ccc;
}
</style>
</head>
<body>
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


//$query1=mysqli_query("select id, name, email from student");
echo "<table><tr><td>Name</td><td>email</td>";
while($r=mysqli_fetch_array($result1))
{
echo "<tr><td>".$r['name']."</td>";
echo "<td>".$r['email']."</td>";
echo "<td><a href='edit.php?id=".$r['id']."'>Edit</a></td>";
echo "<td><a href='delete.php?id=".$r['id']."'>x</a></td><tr>";
}
?>
</ol>
</table>
</body>
</html>
