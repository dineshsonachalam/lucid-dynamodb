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

$DB_NAME = 'chart';

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
 $result = $mysqli->query('SELECT * FROM googlechart');

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
 $table['cols'] = array(

   // Labels for your chart, these represent the column titles.
   /*
       note that one column is in "string" format and another one is in "number" format
       as pie chart only required "numbers" for calculating percentage
       and string will be used for Slice title
   */

   array('label' => 'Weekly Task', 'type' => 'string'),
   array('label' => 'Percentage', 'type' => 'number')

);
   /* Extract the information from $result */
   foreach($result as $r) {

     $temp = array();

     // The following line will be used to slice the Pie chart

     $temp[] = array('v' => (string) $r['weekly_task']);

     // Values of the each slice

     $temp[] = array('v' => (int) $r['percentage']);
     $rows[] = array('c' => $temp);
   }

$table['rows'] = $rows;

// convert data into JSON format
$jsonTable = json_encode($table);
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
     var options = {
          title: 'My Weekly Plan',
         is3D: 'true',
         width: 800,
         height: 600
       };
     // Instantiate and draw our chart, passing in some options.
     // Do not forget to check your div ID
     var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
     chart.draw(data, options);
   }
   </script>
 </head>

 <body>
   <!--this is the div that will hold the pie chart-->
   <div id="chart_div"></div>
 </body>
</html>
