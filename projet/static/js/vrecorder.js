function toggleButton() {
    var fileInput = document.getElementById('audioInput');
    var submitButton = document.getElementById('submitButton');
    submitButton.disabled = !fileInput.value;
}

function showLoader() {
    var loaderOverlay = document.getElementById('loaderOverlay');
    loaderOverlay.style.display = 'flex';
}
//copie text transcris
document.getElementById('copyButton').addEventListener('click', function() {
var transcriptionText = document.getElementById('transcriptionText');
transcriptionText.select();
document.execCommand('copy');
});
//change  copy
function changeIcon() {
 var icon = document.getElementById('icone');
// var icon = copyButton.querySelector('i');

// Changer l'icône FontAwesome
icon.classList.remove('fa-copy');
icon.classList.add('fa-check');

// Revenir à l'icône initiale après 2 secondes
setTimeout(function() {
  icon.classList.remove('fa-check');
  icon.classList.add('fa-copy');
}, 2000);
}
window.addEventListener("DOMContentLoaded", function() {
  const button = document.getElementById('ct');
  // Remplacez ceci par le code approprié pour récupérer la valeur du serveur

  if (button.value!="") {
    button.style.display = "initial";
  }
});
//
function remove(){
   const a = document.getElementById('remove');
   var transcriptionText = document.getElementById('transcriptionText')
   transcriptionText.value="";
}