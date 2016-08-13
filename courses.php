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
    $dataRow = $dataRow."<tr><td>$row1[0]</td><td>$row1[1]</td><td>$row1[2]</td><td>$row1[3]</td><td>$row1[4]</td></tr>";
}

?>





<html lang="en">
<head>
	<meta charset="utf-8" />
	<title>Courses</title>
	<meta name="viewport" content="initial-scale=1.0; maximum-scale=1.0; width=device-width;">

  <meta content="width=device-width, initial-scale=1.0" name="viewport" >
  <link rel="stylesheet" href="css/bootstrap.min.css" type="text/css" />
  <style>
  @import url(http://fonts.googleapis.com/css?family=Roboto:400,500,700,300,100);
  .navbar-default .navbar-brand {
  color: #3e94ec;
                                }
.navbar-default .navbar-nav>.active>a, .navbar-default .navbar-nav>.active>a:hover, .navbar-default .navbar-nav>.active>a:focus {
color: #f5f5f5;
background-color: #3e94ec;
                            }
                            .navbar-default .navbar-nav>li>a:hover, .navbar-default .navbar-nav>li>a:focus {
                            color: #f5f5f5;
                            background-color: transparent;
                        }

body {
  background-color: #3e94ec;
  font-family: "Roboto", helvetica, arial, sans-serif;
  font-size: 16px;
  font-weight: 400;
  text-rendering: optimizeLegibility;
}
  .navbar-default{background-color:black;}
  table {
    max-width: 100%;
    background-color: #f5f5f5;
}
  </style>
</head>


<body>
  <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
          <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar1">
                  <span class="sr-only">Toggle navigation</span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.php">Dianesis:Learning new stuff is fun!</a>
          </div>

          <div class="collapse navbar-collapse" id="navbar1">
              <ul class="nav navbar-nav navbar-right">
                  <?php if (isset($_SESSION['usr_id'])) { ?>

                  <li><p class="navbar-text">Signed in as <?php echo $_SESSION['usr_name']; ?></p></li>
                  <li><a href="index.php">Home</a></li>
                  <li><a href="courses.php">Courses</a></li>
                  <li><a href="profile.php">Profile</a></li>

                  <li><a href="logout.php">Log Out</a></li>
                  <?php } else { ?>
                  <li><a href="login.php">Login</a></li>
                  <li><a href="register.php">Sign Up</a></li>
                  <?php } ?>
              </ul>
          </div>
      </div>
  </nav>



<div class="table-title">
<h3>Course table</h3>
</div>
<table class="table table-hover">
<thead>
<tr>
<th class="text-left">Course Id</th>
<th class="text-left">Course Name</th>
<th class="text-left">Course Type</th>
<th class="text-left">Department</th>
<th class="text-left">Duration</th>

</tr>
</thead>
<tbody class="table-hover">

  <?php while($row1 = mysqli_fetch_array($result1)):;?>
     <tr>
         <td><?php echo $row1[0];?></td>
         <td><?php echo $row1[1];?></td>
         <td><?php echo $row1[2];?></td>
         <td><?php echo $row1[3];?></td>
         <td><?php echo $row1[4];?></td>
     </tr>
  <?php endwhile;?>

</tbody>
<br><br>


<!-- Table Two -->

    <?php echo $dataRow;?>
</table>


</body>
</html>
