console.log("To Do List is Connected");
const allForms = document.querySelectorAll("#todoForm")

for (let i = 0; i < allForms.length; i++) {
    allForms[i].addEventListener("submit", (e) => {
        e.preventDefault();
        formName = allForms[i].children[1].children[0].name;
        formValue = allForms[i].children[1].children[0].value;
        // console.log(formName);
        // console.log(formValue);

        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let xmlhttp = new XMLHttpRequest();
        let formStream = new FormData();
        formStream.append(formName, formValue);

        xmlhttp.open("POST", /to_do_list/, true);
        xmlhttp.setRequestHeader('X-CSRFToken',csrftoken)
        xmlhttp.send(formStream)
        
    })
}



