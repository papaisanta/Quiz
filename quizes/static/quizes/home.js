const class_dropdown = document.getElementById("class");
const subject_dropdown = document.getElementById("subject");
const chapter_dropdown = document.getElementById("chapter");

$.ajax({
    type: "GET",
    url: `${window.location.href}data/`,
    success: function (response) {
        console.log(response)
        const data = response.data;
        data.forEach(cls => {
            class_dropdown.innerHTML += `
                <option>${cls.name}</option>
            `
        });

        class_dropdown.addEventListener(
            "change",
            () => {
                var selected_class = class_dropdown.options[class_dropdown.selectedIndex];
                var class_text = selected_class.text;

                subject_dropdown.innerHTML = ""
                chapter_dropdown = ""
                
                data.forEach(cls => {
                    if (class_text === cls.name){
                        cls.subject.forEach(subject => {
                            var option = document.createElement("option");
                            option.textContent = subject.name;
                            subject_dropdown.add(option)
                        })
                    }
                })
            }
        )

        subject_dropdown.addEventListener(
            "change",
            () => {
                var selected_subject = subject_dropdown.options[subject_dropdown.selectedIndex];
                var subject_text = selected_subject.text;
                chapter_dropdown.innerHTML = ""

                data.forEach(cls => {
                    cls.subject.forEach(subject => {
                        if (subject_text === subject.name) {
                            subject.chapter.forEach(chapter => {
                                var option = document.createElement("option");
                                option.value = chapter.slug;
                                option.textContent = chapter.name
                                chapter_dropdown.appendChild(option)
                            })
                        }
                    })
                })
            }
        )
    },
    error: function (error) {
        console.log(error)
    }
});

// Start Quiz

const start_quiz = document.querySelector("button");

start_quiz.addEventListener(
    "click",
    () => {
        if (subject_dropdown.value == ""){
            alert("select Your Subject");
        }
        else if (chapter_dropdown.value == ""){
            alert("select Your Chapter")
        }
        else{
            window.location.href = `${window.location.href}${chapter_dropdown.value}/`;
        }
    }
)