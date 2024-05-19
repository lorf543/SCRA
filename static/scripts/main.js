new DataTable('#scraList',{ 
  "autoWidth": true,
  "scrollX":true,
  "scrollY":600,
});

new DataTable('#trackerReturn',{ 
  "autoWidth": true,
  "scrollX":true,
  "scrollY":600,
});

new DataTable('#tableInbox',{ 
  "autoWidth": true,
  "scrollX":true,
  "scrollY":600,
});
new DataTable('#Pendinglist',{ 
  "autoWidth": true,
  "scrollX":true,
  "scrollY":600,
});

// new flatpickr("#test_id", {});

//Table for SCRA candidates
// $(document).ready(function() {
//   var table = $('#scraList').DataTable({
//       "paging": true,
//       "lengthChange": true,
//       "searching": true,
//       "ordering": true,
//       "info": true,
//       "autoWidth": true,
//       "scrollX": true,
//       "scrollY": 600,
//       "columnDefs": [
//           // Add any specific column definitions if needed
//       ]
//   });   
// });



window.addEventListener('DOMContentLoaded', event => {

  // Toggle the side navigation
  const sidebarToggle = document.body.querySelector('#sidebarToggle');
  if (sidebarToggle) {
      // Uncomment Below to persist sidebar toggle between refreshes
      // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
      //     document.body.classList.toggle('sb-sidenav-toggled');
      // }
      sidebarToggle.addEventListener('click', event => {
          event.preventDefault();
          document.body.classList.toggle('sb-sidenav-toggled');
          localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
      });
  };

 
    // Get all rows with the class 'customer-row'
    var customerRows = document.querySelectorAll('.customer-row');

    // Add a click event listener to each row
    customerRows.forEach(function(row) {
      row.addEventListener('click', function() {
        // Remove the 'selected' class from all rows
        customerRows.forEach(function(innerRow) {
          innerRow.classList.remove('selected');
        });
  
        // Add the 'selected' class to the clicked row
        row.classList.add('selected');
      });
    });
    
});


