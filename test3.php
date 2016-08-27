<html>
  <head>
    <script>
    $('table').on('click', '.updateRow', function() {
  var myTD = $(this).closest('tr').find('td:eq(1)'); // gets second table cell in the clicked row

  // Now do whatever to myTD, such as:
  $('td').removeClass('selected'); // remove any previous selections
  myTD.addClass('selected');
});
    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <style>
      table {border-collapse:collapse}
      td {border:1px solid}
      .selected {background-color: red}
      .updateRow {color: #00F; text-decoration:underline}
    </style>
  </head>
  <body>
    <table>
      <tr><td class="updateRow">Edit:</td><td>A     </td><td>B  </td><td>C     </td><td>Easy as</td></tr>
      <tr><td class="updateRow">Edit:</td><td>One   </td><td>Two</td><td>Three </td><td>Or simple as</td></tr>
      <tr><td class="updateRow">Edit:</td><td>do    </td><td>re </td><td>me    </td><td>baby</td></tr>
      <tr><td class="updateRow">Edit:</td><td>That's</td><td>how</td><td>simple</td><td>love can be</td></tr>
    </table>
  </body>
</html>
