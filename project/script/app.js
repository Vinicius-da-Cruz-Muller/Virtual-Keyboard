const buttons = document.querySelectorAll('.btn');
// const textarea = document.querySelector('textarea')
const senhaInput = document.getElementById('senha');

const delete_btn = document.querySelector('.delete');
let passwordChars = [];

buttons.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        passwordChars.push(btn.innerText);
        senhaInput.value = passwordChars.join('');
        console.log(passwordChars)
    });
});

delete_btn.addEventListener('click', () =>{
    if (passwordChars.length > 0){
        passwordChars.pop()
        senhaInput.value = passwordChars.join('');
    }
    
});