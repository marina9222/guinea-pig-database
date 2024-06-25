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

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {
      
    });
  });
          
  function validateAge() {
    const age = document.getElementById('pet_age').value;
    if (age < 0) {
        alert('Age cannot be negative');
        return false;
    }
    return true;
}
