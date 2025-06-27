function toSlide(id){
    document.querySelectorAll("div.s").forEach(e =>{
        e.classList.remove("visible")
        e.querySelectorAll("*").forEach(x => {
            x.tabIndex="-1"
        })
    })
    document.getElementById(id).classList.add("visible")
    document.getElementById(id).querySelectorAll("*").forEach(x => {
        x.tabIndex=""
    })
}

function toCodice(id){
    document.querySelectorAll("div.codici").forEach(e=>{
        e.querySelectorAll("button").forEach(x=>{
            x.classList.remove("sel")
        })
    })
    document.getElementById("b"+id).classList.add("sel")
    document.querySelectorAll("div.codi").forEach(e =>{
        e.classList.remove("visible")
        e.querySelectorAll("*").forEach(x => {
            x.tabIndex="-1"
        })
    })
    document.getElementById(id).classList.add("visible")
    document.getElementById(id).querySelectorAll("*").forEach(x => {
        x.tabIndex=""
    })
}

function codi(){
    toSlide('c')
    toCodice('esp')
}

function open(){
    window.location.href='forte.html';
}
