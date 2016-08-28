
<html>
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script>
    $(document).ready(function(){
      $(".s_button").click(function(){
        alert("The value have been updated ");
      });
    });
  </script>
</head>
<body>
<?php
//include('config.php');

/*
if(isset($_SESSION['usr_id'])) {
    header("Location: index.php");
}
*/
include_once 'dbconnect.php';
//echo "connection is established <br />";
session_start();
//echo $_SESSION['usr_id'];

if(isset($_GET['id']))
{
  $id=$_GET['id'];
//  echo $id;

  if(isset($_POST['submit']))
  {
    $name=$_POST['name'];
    $email=$_POST['email'];
    $query3 = mysqli_query($con,"update student set name='$name', email='$email' where id='$id'");
  //  echo "successfully updated into the database";
    }
  $query1=mysqli_query($con,"select * from student where id='$id'");
  $query2=mysqli_fetch_array($query1);
?>
<form method="post" action="">
  Name:<input type="text" name="name" value="<?php echo $query2['name']; ?>" /><br />
  Age:<input type="text" name="email" value="<?php echo $query2['email']; ?>" /><br /><br />
  <br />
  <input type="submit" class="s_button" name="submit" value="update" />

</form>
<?php
}
?>
</body>
</html>
