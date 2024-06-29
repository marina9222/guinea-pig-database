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

function validateMaterializeSelect() {
  let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
  let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
  let selectValidate = document.querySelector("select.validate");
  let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");

  if (!selectValidate || !selectWrapperInput) return; // Check if elements exist

  if (selectValidate.hasAttribute("required")) {
      selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
  }

  const validateSelection = (target) => {
      const ulSelectOptions = target.parentNode.childNodes[1].childNodes;
      let isValid = false;
      ulSelectOptions.forEach(option => {
          if (option.classList.contains("selected") && !option.hasAttribute("disabled")) {
              isValid = true;
          }
      });
      target.style.cssText = isValid ? classValid : classInvalid;
  };

  selectWrapperInput.addEventListener("focusin", (e) => {
      e.target.parentNode.addEventListener("change", () => {
          validateSelection(e.target);
      });
  });

  selectWrapperInput.addEventListener("click", (e) => {
      validateSelection(e.target);
  });

  selectWrapperInput.addEventListener("focusout", (e) => {
      if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
          if (e.target.style.borderBottom !== "1px solid rgb(76, 175, 80)") {
              e.target.style.cssText = classInvalid;
          }
      }
  });
}

validateMaterializeSelect();





