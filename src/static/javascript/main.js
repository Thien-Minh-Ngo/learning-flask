 document.addEventListener("DOMContentLoaded", function(event)  {
    const dogs = document.getElementsByClassName("dogs");
    const cats = document.getElementsByClassName("cats");
    for (let dog of dogs) {
    fetch ('https://dog.ceo/api/breeds/image/random')
    .then((response)=>data=response.json())
    .then(
        (data)=> {
            dog.src=data.message;
        }
    )
    }
    for (let cat of cats) {
    fetch ('https://api.thecatapi.com/v1/images/search')
    .then(response=>response.json())
    .then(data => cat.src = data[0].url);
    }
    console.log("DOM fully loaded and parsed", dogs);
  });

 document.addEventListener("DOMContentLoaded2", function(event) {
  const resultsList = document.getElementById('results')
  new URLSearchParams(window.location.search).forEach((value, name) => {
    resultsList.append(`${name}: ${value}`)
    resultsList.append(document.createElement('br'))
  })
  });
