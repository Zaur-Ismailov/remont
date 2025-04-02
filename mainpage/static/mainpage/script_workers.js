 
 function mainFunction(){
    console.log('Страница открывается');
    let st = "available"
    setTimeout(
        ()=>{
            to_from_server(st);

        }, 6000
    )
    // st = "Занят"
    // to_from_server(st)
}

function to_from_server(st){
    fetch(
        /worker_status/,
    ).then(
        (response) => {
            if(response.status == 200){
            return response.json()
        } else {
                throw 'Ответ от сервера плохой'
            }
        }
    ).then((my_data) => {
        console.log(my_data); 
        document.getElementById("Отделка").classList.remove("available");
        document.getElementById("Отделка").classList.remove("unavailable");
        document.getElementById("Отделка").classList.add(my_data["Отделка"]);
    
    }
        // (my_data) => add_to_page(my_data,st));}
    );
}

    








window.addEventListener(
    'load',
    mainFunction
);