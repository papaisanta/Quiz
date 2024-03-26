const quiz_box = document.getElementById("quiz-box");


// Show Questions and Answers
$.ajax({
    type: "GET",
    url: `${window.location.href}data/`,
    success: function (response) {
        const data = response.data

        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)){
                quiz_box.innerHTML += `<hr><h4>${question}</h4>`

                answers.forEach(answer => {
                    quiz_box.innerHTML += `
                        <input type="radio" class="answer" name="${question}" value="${answer}">
                        <label for=${question}>${answer}</label>
                    `
                })
            }
        })
    }
});

// Post Questions and Answers
const quiz_form = document.querySelector("form");
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const result_box = document.getElementById("result-box");

quiz_form.addEventListener(
    "submit",
    (event) => {
        sendData()
        event.preventDefault()
    }
);

const sendData = () => {
    const elements = document.querySelectorAll("input");
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;

    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value;
        } else {
            if (!data[el.name]) {
                data[el.name] = null;
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: `${window.location.href}save/`,
        data: data,
        success: function (response){
            const results = response.results
            quiz_form.style.display = "none";


            result_box.innerHTML += `${response.passed ? 'Congratulations!' : 'ups!'} Your result is ${response.score.toFixed(2)}`

            results.forEach(result => {
                const res_div = document.createElement("div");
                
                for (const [question, answer] of Object.entries(result)){
                    res_div.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h5']
                    res_div.classList.add(...cls)

                    if (answer == "not answered") {
                        res_div.innerHTML += "  | not answered"
                        res_div.classList.add('bg-danger')
                    }else{
                        const answered = answer['answered']
                        const correct_answer = answer['correct'];

                        if (answered == correct_answer) {
                            res_div.classList.add('bg-success');
                            res_div.innerHTML += `  | answered: ${answered}`;
                        } else {
                            res_div.classList.add('bg-danger');
                            res_div.innerHTML += `  | correct answer: ${correct_answer}`
                            res_div.innerHTML += `  | answerd: ${answered}`
                        }
                    }
                }
                document.body.append(res_div);
            })
        }
    })
}