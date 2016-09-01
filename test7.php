<?php



include_once 'dbconnect.php';
session_start();

//set validation error flag as false
$error = false;

//check if form is submitted
if (isset($_POST['signup'])) {
    $course_id = mysqli_real_escape_string($con, $_POST['course_id']);
    $course_name = mysqli_real_escape_string($con, $_POST['course_name']);
    $course_type = mysqli_real_escape_string($con, $_POST['course_type']);
    $dept = mysqli_real_escape_string($con, $_POST['dept']);
    $duration = mysqli_real_escape_string($con, $_POST['duration']);
    $course_url = mysqli_real_escape_string($con, $_POST['course_url']);

        if (!$error) {
        if(mysqli_query($con, "INSERT INTO course(course_id,course_name,course_type,dept,duration,course_url)
        VALUES('" . $course_id . "', '" . $course_name . "', '" . $course_type . "', '" . $dept . "','" . $duration . "','" .$course_url. "')"   ))
        {
            //$successmsg = "Successfully Registered! <a href='index.php'>Click here to Login</a>";
            echo "Successfully added to the course table";
        } else {
          //  $errormsg = "Error in registering...Please try again later!";
          echo "There is a problem in adding to the course table!";
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Add Courses</title>
    <script src="js/jquery-1.10.2.js"></script>
    <script src="js/bootstrap.min.js"></script>
</head>
<body>
  <div class="container">
      <div class="row">
          <div class="col-md-4 col-md-offset-4 well">
              <form role="form" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" >
                  <fieldset>
                      <legend>Add courses</legend>

                      <!--
                      <div class="form-group">
                          <label for="name">Name</label>
                          <input type="text" name="name" placeholder="Enter Full Name" required value="<?php if($error) echo $name; ?>" class="form-control" />
                          <span class="text-danger"><?php if (isset($name_error)) echo $name_error; ?></span>
                      </div>

                      <div class="form-group">
                          <label for="name">Email</label>
                          <input type="text" name="email" placeholder="Email" required value="<?php if($error) echo $email; ?>" class="form-control" />
                          <span class="text-danger"><?php if (isset($email_error)) echo $email_error; ?></span>
                      </div>

                      <div class="form-group">
                          <label for="name">Password</label>
                          <input type="password" name="password" placeholder="Password" required class="form-control" />
                          <span class="text-danger"><?php if (isset($password_error)) echo $password_error; ?></span>
                      </div>


                      --->

                        &nbsp;  Course ID:   &nbsp;   &nbsp;  &nbsp;   &nbsp;<input type="text" name="course_id" value="<?php echo $query2['course_id']; ?>" /><br />
                        &nbsp;  Course Name: <input type="text" name="course_name" value="<?php echo $query2['course_name']; ?>" /><br />
                        &nbsp;  Course Type: &nbsp; <input type="text" name="course_type" value="<?php echo $query2['course_type']; ?>" /><br />
                        &nbsp;  Department:  &nbsp;  &nbsp;<input type="text" name="dept" value="<?php echo $query2['dept']; ?>" /><br />
                        &nbsp;  Duration:  &nbsp;  &nbsp;  &nbsp;    &nbsp; &nbsp;<input type="text" name="duration" value="<?php echo $query2['duration']; ?>" /><br />
                        &nbsp;  Course URL:   &nbsp;  &nbsp;<input type="text" name="course_url" value="<?php echo $query2['course_url']; ?>" /><br />




                      <div class="form-group">
                          <input type="submit" name="signup" value="Add" class="btn btn-primary" />
                      </div>
                  </fieldset>
              </form>
              <span class="text-success"><?php if (isset($successmsg)) { echo $successmsg; } ?></span>
              <span class="text-danger"><?php if (isset($errormsg)) { echo $errormsg; } ?></span>
          </div>
      </div>

  </div>
</body>
</html>
