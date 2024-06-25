document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var options = {
        edge: 'right',
    }

    var instances = M.Sidenav.init(elems, options);
  });


  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    
    var instances = M.Collapsible.init(elems, {
      
      });
      
    
  });
          