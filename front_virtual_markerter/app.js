
const API_KEY = 'YOUR_API_KEY';
const submitButton = document.querySelector('#submit');
const outputElement = document.querySelector('#output')
const inputElement = document.querySelector('#input')
const historyElement = document.querySelector('.history')
const buttonElement = document.querySelector('button')

function changeInput(text){
    document.querySelector('input').value = text
}
async function getMessage(){
    console.log('Clicked')
    console.log(inputElement.value)
    const options = {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${API_KEY}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [{role: "user", content: inputElement.value}],
            max_tokens: 25,
        })
    }
    try{
        const response = await fetch('https://api.openai.com/v1/chat/completions',options)
        const data = await response.json()
        console.log(data)
        outputElement.textContent = data.choices[0].message.content
        if(data.choices[0].message.content && inputElement.value){
            const pElement = document.createElement('p')
            pElement.textContent = inputElement.value
            pElement.addEventListener('click', () => changeInput(pElement.textContent))
            historyElement.append(pElement)
        }
    }
    catch (error){
       console.error(error)
    }
}

function clearInput(){
    inputElement.value = ''
}

submitButton.addEventListener('click', getMessage)
buttonElement.addEventListener('click', clearInput)