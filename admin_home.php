<?php
//session_start();
//This page is the admin home page. All contents related to admin are stored in course table

//include_once 'dbconnect.php';
$DB_NAME = 'dianesis';

/* Database Host */
$DB_HOST = 'localhost';

/* Your Database User Name and Passowrd */

$DB_USER = 'root';
$DB_PASS = '';

$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
session_start();

if (mysqli_connect_errno()) {
  printf("Connect failed: %s\n", mysqli_connect_error());
  exit();
}

 /* select all the weekly tasks from the table googlechart */
$enroll_result = $mysqli->query('SELECT course.course_name,COUNT(enrollmentfact.student_id) AS enrollment_count FROM course INNER JOIN enrollmentfact ON course.course_id = enrollmentfact.course_id GROUP BY course.course_name');
$course_result = $mysqli->query('SELECT dept,COUNT(course_name) AS course_count FROM course GROUP BY dept');

/*
    ---------------------------
    example data: Table (googlechart)
    --------------------------
    Weekly_Task     percentage
    Sleep           30
    Watching Movie  10
    job             40
    Exercise        20
*/



$rows = array();
$table = array();

$rows_course = array();
$table_course = array();
$table['cols'] = array(

  // Labels for your chart, these represent the column titles.
  /*
      note that one column is in "string" format and another one is in "number" format
      as pie chart only required "numbers" for calculating percentage
      and string will be used for Slice title
  */

  array('label' => 'Course', 'type' => 'string'),
  array('label' => 'No of Enrollments', 'type' => 'number')

);
$table_course['cols'] = array(

 // Labels for your chart, these represent the column titles.
 /*
     note that one column is in "string" format and another one is in "number" format
     as pie chart only required "numbers" for calculating percentage
     and string will be used for Slice title
 */

 array('label' => 'Department', 'type' => 'string'),
 array('label' => 'No of Courses', 'type' => 'number')

);
  /* Extract the information from $result */
  foreach($enroll_result as $r) {
 //   echo $r['course_name'];

    $temp = array();

    // The following line will be used to slice the Pie chart

    $temp[] = array('v' => (string) $r['course_name']);

    // Values of the each slice

    $temp[] = array('v' => (int) $r['enrollment_count']);
    $rows[] = array('c' => $temp);
  }

  foreach($course_result as $r) {
   // echo $r['course_name'];
    $temp_course = array();

    // The following line will be used to slice the Pie chart
 //   echo $r['dept'];

    $temp_course[] = array('v' => (string) $r['dept']);

    // Values of the each slice
 //   echo  $r['course_count'];

    $temp_course[] = array('v' => (int) $r['course_count']);
    $rows_course[] = array('c' => $temp_course);
  }

$table['rows'] = $rows;
$table_course['rows'] = $rows_course;

// convert data into JSON format
$jsonTable = json_encode($table);
$jsonTable_course = json_encode($table_course);
//echo $jsonTable;



?>
<!DOCTYPE html>
<html>
<head>
  <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script type="text/javascript">

  // Load the Visualization API and the piechart package.
  google.load('visualization', '1', {'packages':['corechart']});

  // Set a callback to run when the Google Visualization API is loaded.
  google.setOnLoadCallback(drawChart);

  function drawChart() {

    // Create our data table out of JSON data loaded from server.
     var data = new google.visualization.DataTable(<?php echo $jsonTable?>);
     var data_course = new google.visualization.DataTable(<?php echo $jsonTable_course?>);
    var options = {
         title: 'Enrollment count from each course',
        is3D: 'true',
        width: 500,
        height: 500
      };
      var options_course = {
           title: 'No of available courses in each Department',
          is3D: 'true',
          width: 500,
          height: 500
        };
    // Instantiate and draw our chart, passing in some options.
    // Do not forget to check your div ID
    var chart = new google.visualization.ColumnChart(document.getElementById('Enrollment'));
    var chart_course = new google.visualization.PieChart(document.getElementById('Courses'));

   // var chart = new google.charts.Bar(document.getElementById('chart_div'));
 //   var chart = new google.charts.Bar(document.getElementById('chart_div'));
   chart.draw(data, options);
   chart_course.draw(data_course, options_course);
  }
  </script>

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

                  <!-- php current session after login -->
                <?php if (isset($_SESSION['usr_id'])) { ?>

                <li><p class="navbar-text">Signed in as <?php echo $_SESSION['usr_name']; ?></p></li>
                <li><a href="admin_home.php">Home</a></li>
                <li><a href="courses_add.php">Add Courses</a></li>
                <li><a href="admin_profile.php">Profile</a></li>

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
<h3>Visualization of Users data</h3>
</div>


<div class="section">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div id="Enrollment"></div>
            <h2>Enrollment for each courses:</h2>
            <p></p>
            <p>The student registration count for each of the courses,
              <br>that are available as a part of enrollment.
            </p>
            <p></p>
          </div>
          <div class="col-md-6">
            <div id='Courses'></div>
            <h2>Avaiable Courses:</h2>
            <p></p>
            <p>The no of available courses from each department,
              <br>that are present as a part of courses.
            </p>
            <p></p>
          </div>
        </div>
      </div>
    </div


<script src="js/jquery-1.10.2.js"></script>
<script src="js/bootstrap.min.js"></script>
</body>
</html>
