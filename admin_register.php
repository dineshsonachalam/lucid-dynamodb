<?php
session_start();

if(isset($_SESSION['usr_id'])) {
    header("Location: admin.php");
}

include_once 'dbconnect.php';

//set validation error flag as false
$error = false;

//check if form is submitted
if (isset($_POST['signup'])) {
    $name = mysqli_real_escape_string($con, $_POST['name']);
    $email = mysqli_real_escape_string($con, $_POST['email']);
    $password = mysqli_real_escape_string($con, $_POST['password']);
    $cpassword = mysqli_real_escape_string($con, $_POST['cpassword']);

      $dept = mysqli_real_escape_string($con, $_POST['dept']);
        $dob = mysqli_real_escape_string($con, $_POST['dob']);
          $college = mysqli_real_escape_string($con, $_POST['college']);
          $gender = mysqli_real_escape_string($con, $_POST['gender']);
          $is_admin = 1;


    //name can contain only alpha characters and space
    if (!preg_match("/^[a-zA-Z ]+$/",$name)) {
        $error = true;
        $name_error = "Name must contain only alphabets and space";
    }
    if(!filter_var($email,FILTER_VALIDATE_EMAIL)) {
        $error = true;
        $email_error = "Please Enter Valid Email ID";
    }
    if(strlen($password) < 6) {
        $error = true;
        $password_error = "Password must be minimum of 6 characters";
    }
    if($password != $cpassword) {
        $error = true;
        $cpassword_error = "Password and Confirm Password doesn't match";
    }
    if (!$error) {
        if(mysqli_query($con, "INSERT INTO student(name,email,password,dept,dob,college,gender,is_admin) VALUES('" . $name . "', '" . $email . "', '" . md5($password) . "', '" . $dept . "','" . $dob . "','" .$college. "','" . $gender . "','".$is_admin."')"   )) {
            $successmsg = "Successfully Registered! <a href='index.php'>Click here to Login</a>";
        } else {
            $errormsg = "Error in registering...Please try again later!";
        }
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
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
    </style></head>
<body>

<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <!-- add header -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar1">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.php">Dianesis a place to learn better!</a>
        </div>
        <!-- menu items -->
        <div class="collapse navbar-collapse" id="navbar1">
            <ul class="nav navbar-nav navbar-right">
                <li><a href="index.php">Login</a></li>
                <li class="active"><a href="register.php">Sign Up</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4 well">
            <form role="form" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" name="signupform">
                <fieldset>
                    <legend>Sign Up</legend>

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

                    <div class="form-group">
                        <label for="name">Confirm Password</label>
                        <input type="password" name="cpassword" placeholder="Confirm Password" required class="form-control" />
                        <span class="text-danger"><?php if (isset($cpassword_error)) echo $cpassword_error; ?></span>
                    </div>

                    <div class="form-group">
                        <label for="name">Department</label>
                    <!--    <input type="text" name="dept" placeholder="Enter Department Name" required value="<?php if($error) echo $dept; ?>" class="form-control" /> -->
                    <br>
                    <select name="dept" class="form-control">
                      <option name="dept" value="ece"   required value="<?php if($error) echo $dept; ?>">ECE</option>
                      <option name="dept" value="cse"  required value="<?php if($error) echo $dept; ?>">CSE</option>
                      <option name="dept" value="eee"   required value="<?php if($error) echo $dept; ?>">EEE</option>
                      <option name="dept" value="it" required value="<?php if($error) echo $dept; ?>">IT</option>
                    </select>


                    </div>

                    <div class="form-group">
                        <label for="name">Date of Birth</label>
                        <input type="date" name="dob" placeholder="Enter Date-of-Birth" required value="<?php if($error) echo $dob; ?>" class="form-control" />


                    </div>
                    <div class="form-group">
                        <label for="name">College</label>
                        <input type="text" name="college" placeholder="Enter College" required value="<?php if($error) echo $college; ?>" class="form-control" />

                    </div>
                    <div class="form-group">
                        <label for="name">Gender</label>
                        <br>
                        <input type="radio" name="gender" value="male" checked> Male<br>
                        <input type="radio" name="gender" value="female"> Female<br>


                    </div>



                    <div class="form-group">
                        <input type="submit" name="signup" value="Sign Up" class="btn btn-primary" />
                    </div>
                </fieldset>
            </form>
            <span class="text-success"><?php if (isset($successmsg)) { echo $successmsg; } ?></span>
            <span class="text-danger"><?php if (isset($errormsg)) { echo $errormsg; } ?></span>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4 col-md-offset-4 text-center">
        Already Registered? <a  style="color:white" href="admin.php">Login Here</a>
        </div>
    </div>
</div>
<script src="js/jquery-1.10.2.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
