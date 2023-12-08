document.getElementById("upload-form").addEventListener("submit",function(e){
    e.preventDefault();
    let formData = new FormData(this);

    let fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);

    fetch("/upload",{
        method:"POST",
        body:formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('predictionResult').innerHTML='Result: '+ data.result;
        })
    });
    


