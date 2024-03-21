const hamBurger = document.querySelector(".toggle-btn");

hamBurger.addEventListener("click", function () {
  document.querySelector("#sidebar").classList.toggle("expand");
});



new DataTable('#scraList',{ 
  "autoWidth": true,
  "scrollX":true,
  "scrollY":600,
});


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


