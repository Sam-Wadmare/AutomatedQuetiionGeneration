document.getElementById("next-btn").addEventListener("click", fetchQuestion);

function fetchQuestion() {
    fetch('/generate')
        .then(response => response.json())
        .then(data => {
            document.getElementById("question-box").innerText = data.question;

            const optionsList = document.getElementById("options-list");
            optionsList.innerHTML = "";
            data.options.forEach(option => {
                const li = document.createElement("li");
                li.innerText = option;
                optionsList.appendChild(li);
            });
        });
}

// Load first question on page load
fetchQuestion();
