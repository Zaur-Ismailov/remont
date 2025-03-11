// setInterval - поставить цикличную задачу
// setTimeout - поставить однократную задачу

// 1. При загрузке страницы получить все, что к этому моменту было
// 2. Поставить таймер, проверить не появилось ли что то новое.
// 3. Когда таймер истекает - отправляется запрос на сервер и ожидается ответ, который будет отработан клиентом.
function add_to_page(my_data,tm){
    console.log(my_data)
        let ol = document.getElementById('my_list');
        let li = document.createElement('li');
        li.textContent = tm + ': ' + my_data[tm]
        ol.appendChild(li);
        document.body.appendChild(ol);

}


function mainFunction(){
    console.log('Страница готова');
    let tm = 'утро';
    to_from_server(tm);
    tm = 'день';
    to_from_server(tm);
}

function to_from_server(tm){
    fetch(
        '/my_tasks/',
        {
            method: 'post',
            body: JSON.stringify ({
                'когда': tm
            }),
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        }
    ).then(
        (response) => {
            if(response.status == 200){
            return response.json()
        } else {
                throw 'Ответ от сервера плохой'
            }
        }
    ).then((my_data) => add_to_page(my_data,tm)
        

).catch((error) => {
    console.error(error);
    
});
    
}


window.addEventListener(
    'load',
    mainFunction
);