console.log("To Do List is Connected");
const allForms = document.querySelectorAll("#todoForm")

for (let i = 0; i < allForms.length; i++) {
    allForms[i].addEventListener("submit", (e) => {
        e.preventDefault();
        formName = allForms[i].children[1].children[0].name;
        formValue = allForms[i].children[1].children[0].value;
        formId = allForms[i].children[1].children[0].id;
        console.log("-------------------------------------------");
        console.log(formName);
        console.log(formValue);
        console.log(formId);
        if (formValue == "notDone") {
            allForms[i].children[1].children[1].classList.add("anim-yes")
            allForms[i].children[1].children[1].classList.remove("task-notDone")
            setTimeout(function(){
                allForms[i].children[1].children[1].classList.remove("anim-yes")
                allForms[i].children[1].children[1].classList.add("task-done")
            }, 1000)

        } else if (formValue == "Done") {
            allForms[i].children[1].children[1].classList.add("anim-no")
            allForms[i].children[1].children[1].classList.remove("task-done")
            setTimeout(function(){
                allForms[i].children[1].children[1].classList.remove("anim-no")
                allForms[i].children[1].children[1].classList.add("task-notDone")
            }, 1000)
        }



        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        let xmlhttp = new XMLHttpRequest();
        let formStream = new FormData();
        formStream.append(formName, formId);

        xmlhttp.open("POST", /to_do_list/, true);
        xmlhttp.setRequestHeader('X-CSRFToken',csrftoken)
        xmlhttp.send(formStream)
        
    })
}



