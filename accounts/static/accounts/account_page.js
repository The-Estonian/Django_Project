console.log("Account page connected!");

const backdrop = document.querySelector(".backdrop")
const accountInfo = document.querySelector(".account-info")
const cancelButton = document.querySelectorAll(".change__label__choices__cancel")

const username = document.querySelector(".username-change")
const usernameTrigger = document.querySelector("#username")

const password = document.querySelector(".password-change")
const passwordTrigger = document.querySelector("#password")

const email = document.querySelector(".email-change")
const emailTrigger = document.querySelector("#email")

const firstName = document.querySelector(".first-name-change")
const firstNameTrigger = document.querySelector("#first-name")

const lastName = document.querySelector(".last-name-change")
const lastNameTrigger = document.querySelector("#last-name")

const formRefresh = document.querySelector(".account-form")

usernameTrigger.addEventListener("click", function() {
    backdrop.style.display = "block"
    username.style.display = "block"
    accountInfo.style.display = "none"
})

passwordTrigger.addEventListener("click", function() {
    backdrop.style.display = "block"
    password.style.display = "block"
    accountInfo.style.display = "none"
})

emailTrigger.addEventListener("click", function() {
    backdrop.style.display = "block"
    email.style.display = "block"
    accountInfo.style.display = "none"
})

firstNameTrigger.addEventListener("click", function() {
    backdrop.style.display = "block"
    firstName.style.display = "block"
    accountInfo.style.display = "none"
})

lastNameTrigger.addEventListener("click", function() {
    backdrop.style.display = "block"
    lastName.style.display = "block"
    accountInfo.style.display = "none"
})

for (let i = 0; i < cancelButton.length; i++) {
    cancelButton[i].addEventListener("click", function() {
        backdrop.style.display = ""
        username.style.display = ""
        password.style.display = ""
        email.style.display = ""
        firstName.style.display = ""
        lastName.style.display = ""
        accountInfo.style.display = "flex"
    })
}

// formRefresh.addEventListener("submit", function() {

//     location.reload();
// })

backdrop.addEventListener("click", function() {
    backdrop.style.display = ""
    username.style.display = ""
    password.style.display = ""
    email.style.display = ""
    firstName.style.display = ""
    lastName.style.display = ""
    accountInfo.style.display = "flex"
})
