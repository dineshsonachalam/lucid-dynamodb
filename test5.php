<?php
session_start();
include_once 'dbconnect.php';
/*
$query = "SELECT DISTINCT course.course_name,enrollmentfact.enroll_date
FROM enrollmentfact
INNER JOIN course
ON enrollmentfact.course_id=course.course_id AND enrollmentfact.student_id=".$_SESSION['usr_id']; */
// result for method one
$query = "(SELECT * FROM `student` WHERE  id  =".$_SESSION['usr_id'].")";
$result1 = mysqli_query($con, $query);
//$result1 = mysqli_query($con, $query);
// result for method two
//$result2 = mysqli_query($connect, $query);
$dataRow = "";
/*
while($row1 = mysqli_fetch_array($result1))
{
    $dataRow = $dataRow."<tr><td>$row1[0]</td><td>$row1[1]</td></tr>";
}
*/
//echo $_SESSION['usr_id'];
?>
<!DOCTYPE html>
<html>
<head>

    <title>Home | Dianesis:Learning new stuff is fun!</title>
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

        .alert{
    display: none;
}
        </style>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script src="js/bootstrap.min.js"></script>

        <script>
        $(document).ready(function(){
          $(".s_button").click(function(){
      alert("The course have been successfully added!:)");
  });
});
        </script>

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

                  <!-- php current session after login -->
                <?php if (isset($_SESSION['usr_id'])) { ?>

                <li><p class="navbar-text">Signed in as <?php echo $_SESSION['usr_name']; ?></p></li>
                <li><a href="index.php">Home</a></li>
                <li><a href="courses.php">Courses</a></li>
                <li><a href="profile2.php">Profile</a></li>

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
<h3>Add courses</h3>
</div>

</div>
<?php
//echo $_SESSION['usr_id'];
if(isset($_SESSION['usr_id']))
{
  $id=$_SESSION['usr_id'];
//  echo $id;
  if(isset($_POST['submit']))
  {
/*
    $name=$_POST['name'];
    $email=$_POST['email'];
    $dept=$_POST['dept'];
    $dob=$_POST['dob'];
    $college=$_POST['college'];
    $gender=$_POST['gender'];
    $query3 = mysqli_query($con,"update student set name='$name', email='$email',dept='$dept',dob='$dob',college='$college',gender='$gender' where id='$id'");
  //  echo "successfully updated into the database";
*/
$course_id=$_POST['course_id'];
$course_name=$_POST['course_name'];
$course_type=$_POST['course_type'];
$dept=$_POST['dept'];
$duration=$_POST['duration'];
$course_url=$_POST['course_url'];
$query3 = mysqli_query($con,"INSERT INTO `course`(`course_id`, `course_name`, `course_type`, `dept`, `duration`, `course_url`)
 VALUES ('$course_id','$course_name','$course_type','$dept','$duration','$course_url')");

    }
  $query1=mysqli_query($con,"select * from course");
  $query2=mysqli_fetch_array($query1);
 ?>


<div id="edit_details">

  <form method="post" action="">
  &nbsp;  Course ID:   &nbsp;   &nbsp;  &nbsp;   &nbsp;<input type="text" name="course_id" value="<?php echo $query2['course_id']; ?>" /><br />
  &nbsp;  Course Name: <input type="text" name="course_name" value="<?php echo $query2['course_name']; ?>" /><br />
  &nbsp;  Course Type: &nbsp; <input type="text" name="course_type" value="<?php echo $query2['course_type']; ?>" /><br />
  &nbsp;  Department:  &nbsp;  &nbsp;<input type="text" name="dept" value="<?php echo $query2['dept']; ?>" /><br />
  &nbsp;  Duration:  &nbsp;  &nbsp;  &nbsp;    &nbsp; &nbsp;<input type="text" name="duration" value="<?php echo $query2['duration']; ?>" /><br />
  &nbsp;  Course URL:   &nbsp;  &nbsp;<input type="text" name="course_url" value="<?php echo $query2['course_url']; ?>" /><br />

    <br />
    <br />





   &nbsp; <input type="submit" class="s_button" name="submit" value="Add"   />

  </form>
  <?php
  }
  ?>
</div>

</body>
</html>