const buttons = document.querySelectorAll('.btn');
// const textarea = document.querySelector('textarea')
const senhaInput = document.getElementById('pass');
const btnLogin = document.getElementById('btn_login');
const delete_btn = document.querySelector('.delete');

let passwordChars = [];

buttons.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        passwordChars.push(btn.innerText);
        senhaInput.value = passwordChars.join('');
        senhaInput.dispatchEvent(new Event('input'));
        console.log(passwordChars)
        console.log(senhaInput.value)
    });
});

delete_btn.addEventListener('click', () =>{
    if (passwordChars.length > 0){
        passwordChars.pop()
        senhaInput.value = passwordChars.join('');
    }
    
});