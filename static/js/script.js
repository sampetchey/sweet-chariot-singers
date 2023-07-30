var options = {
    inDuration : 5000 
}

document.addEventListener('DOMContentLoaded', function() {
var elems = document.querySelectorAll('.modal', '.modal2');
var instances = M.Modal.init(elems, options);
});