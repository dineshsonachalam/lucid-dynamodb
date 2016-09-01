<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <script src="js/jquery-1.10.2.js"></script>
  <script src="js/bootstrap.min.js"></script>
    <script>
  bootstrap_alert = function() {}
  bootstrap_alert.warning = function(message) {
              $('#alert_placeholder').html('<div class="alert alert-success alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><span>'+message+'</span></div>')
          }


  $('#clickme').on('click', function() {
              bootstrap_alert.warning('Your text goes here');
  });
  </script>
</head>
<body>

  <input type = "button" id = "clickme" value="Click me!"/>
<div id = "alert_placeholder"></div>
</body>
</html>
