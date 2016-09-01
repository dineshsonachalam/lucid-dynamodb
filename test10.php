<?php
/*
Script  : PHP-JSON-MySQLi-GoogleChart
Author  : Enam Hossain
version : 1.0

*/

/*
--------------------------------------------------------------------
Usage:
--------------------------------------------------------------------

Requirements: PHP, Apache and MySQL

Installation:

 --- Create a database by using phpMyAdmin and name it "chart"
 --- Create a table by using phpMyAdmin and name it "googlechart" and make sure table has only two columns as I have used two columns. However, you can use more than 2 columns if you like but you have to change the code a little bit for that
 --- Specify column names as follows: "weekly_task" and "percentage"
 --- Insert some data into the table
 --- For the percentage column only use a number

     ---------------------------------
     example data: Table (googlechart)
     ---------------------------------

     weekly_task     percentage
     -----------     ----------

     Sleep           30
     Watching Movie  10
     job             40
     Exercise        20


*/

/* Your Database Name */

$DB_NAME = 'dianesis';

/* Database Host */
$DB_HOST = 'localhost';

/* Your Database User Name and Passowrd */
$DB_USER = 'root';
$DB_PASS = '';





 /* Establish the database connection */
 $mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

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


<html>
 <head>
   <!--Load the Ajax API-->
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
         width: 800,
         height: 600
       };
       var options_course = {
            title: 'No of available courses in each Department',
           is3D: 'true',
           width: 800,
           height: 600
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
 </head>

 <body>
   <!--this is the div that will hold the pie chart-->
   <div id="Enrollment"></div>
   <div id='Courses'></div>
 </body>
</html>
