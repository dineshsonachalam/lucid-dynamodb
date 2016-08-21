<?php
session_start();

if(isset($_SESSION['usr_id'])!="") {
    header("Location: home.php");
}

include_once 'dbconnect.php';

//check if form is submitted
if (isset($_POST['index'])) {

    $email = mysqli_real_escape_string($con, $_POST['email']);
    $password = mysqli_real_escape_string($con, $_POST['password']);
    $result = mysqli_query($con, "SELECT * FROM student WHERE email = '" . $email. "' and password = '" . md5($password) . "'");

    if ($row = mysqli_fetch_array($result)) {
        $_SESSION['usr_id'] = $row['id'];
        $_SESSION['usr_name'] = $row['name'];
        header("Location: home.php");
    } else {
        $errormsg = "Incorrect Email or Password!!!";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
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
    </style>
</head>
<body>


<nav class="navbar navbar-default"  role="navigation">
    <div class="container-fluid">
        <!-- add header -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar1">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.php" >Learning new stuff is fun!</a>
        </div>
        <!-- menu items -->
        <div class="collapse navbar-collapse" id="navbar1" >
            <ul class="nav navbar-nav navbar-right">
                <li class="active"><a href="index.php">Login</a></li>
                <li><a href="register.php">Sign Up</a></li>
            </ul>
        </div>
    </div>
</nav>
<center><h2>Welcome to online course reservation system!</h2></center>
<br>

<div class="container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4 well">
            <form role="form" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" name="loginform">
                <fieldset>
                    <legend>Login</legend>

                    <div class="form-group">
                        <label for="name">Email</label>
                        <input type="text" name="email" placeholder="Your Email" required class="form-control" />
                    </div>

                    <div class="form-group">
                        <label for="name">Password</label>
                        <input type="password" name="password" placeholder="Your Password" required class="form-control" />
                    </div>

                    <div class="form-group">
                        <input type="submit" name="index" value="index" class="btn btn-primary" />
                    </div>
                </fieldset>
            </form>
            <span class="text-danger"><?php if (isset($errormsg)) { echo $errormsg; } ?></span>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4 col-md-offset-4 text-center">
        New User? <a style="color:white" href="register.php">Sign Up Here</a>
        </div>
    </div>
</div>

<script src="js/jquery-1.10.2.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
