//grabs cookie and checks it?
function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
//Start CRUD
    var activeItem = null
    var list_snapshot = []

    buildList()

    function buildList(){
        var wrapper = document.getElementById('list-wrapper')
        //wrapper.innerHTML = ''

        var url = '/project2/todo-list/'
        //fetch data and stick in list?
        fetch(url)
        .then((resp) => resp.json())
        .then(function(data){
            console.log('Data:', data)

            var list = data
            for (var i in list){

                try{
                document.getElementById(`data-row-${i}`).remove()
                }catch(err){

                }

            <!--This is the render-->
            //variable 'title' equals the html string
                var title = `<div style="flex:7">
                <span class="title">${list[i].list_item}</span>
                </div>`
                //if list item complete, display as blue
                if (list[i].complete == true){
                    title = `<div class="rounded bg-primary text-white" style="flex:7">
                    <span class="title" style>${list[i].list_item}</span>
                    </div>`
                }
                // This displays the edit and delete buttons
                var item = `
                    <div id="data-row-${i}" class="task-wrapper flex-wrapper ">
                            ${title}
                       <div style="flex:1">
                            <button class="btn btn-sm btn-outline-info edit">Edit</button>
                        </div>
                        <div style="flex:1">
                            <button class="btn btn-sm btn-outline-dark delete">-</button>
                        </div>
                    </div>
                `
                //not sure what this does. maybe adds buttons to end of list item?
                wrapper.innerHTML += item


            }

            if (list_snapshot.length > list.length){
                for(var i = list.length; i < list_snapshot.length; i++){
                    document.getElementById(`data-row-${i}`).remove()
                }
            }

            list_snapshot = list
        // adds functionality to all the buttons
        for (var i in list){
            var editBtn = document.getElementsByClassName('edit')[i]
            var deleteBtn = document.getElementsByClassName('delete')[i]
            var title = document.getElementsByClassName('title')[i]

            editBtn.addEventListener('click', (function(item){
                return function(){
                    editItem(item)
                }
            })(list[i]))

            deleteBtn.addEventListener('click', (function(item){
                return function(){
                    deleteItem(item)
                }
            })(list[i]))

            title.addEventListener('click', (function(item){
                return function(){
                    completeItem(item)
                }
            })(list[i]))

        }
        })
    }
    var form = document.getElementById('form-wrapper')
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form Submitted')
        var url = '/project2/todo-create/'
        if (activeItem != null){
            var url = `/project2/todo-update/${activeItem.id}/`
            activeItem = null
        }

        var title = document.getElementById('title').value
        fetch(url, {
            method:'POST',
            headers:{
                'Content-type': 'application/json',
                'x-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'list_item':title})
        }
        ).then(function(response){
            buildList()
            document.getElementById('form').reset()

        })
    })

    function editItem(item){
        console.log('Item Clicked', item)
        activeItem = item
        document.getElementById('title').value = activeItem.list_item
    }
    function deleteItem(item){
        console.log('Delete clicked')
        fetch(`/project2/todo-delete/${item.id}/`, {
            method: 'DELETE',
            headers:{
                'Content-type': 'application/json',
                'x-CSRFToken': csrftoken,
            }
        }).then((response) => {
            buildList()
        })
    }

    function completeItem(item){
        console.log('Completed clicked')
        item.complete = !item.complete
        fetch(`/project2/todo-update/${item.id}/`, {
            method: 'POST',
            headers:{
                'Content-type': 'application/json',
                'x-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'list_item': item.list_item, 'complete': item.complete})
        }).then((response) => {
            buildList()
        })
    }
