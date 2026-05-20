async function checkPassword() {

    const password = document.getElementById("password").value;

    const response = await fetch("/check_password", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    document.getElementById("strength").innerText =
        "Strength: " + data.strength;

    document.getElementById("score").innerText =
        "Score: " + data.score;

    const feedbackList = document.getElementById("feedback");
    feedbackList.innerHTML = "";

    data.feedback.forEach(item => {
        const li = document.createElement("li");
        li.innerText = item;
        feedbackList.appendChild(li);
    });

    document.getElementById("suggestion").innerText =
        "Suggested Password: " + data.suggestion;
}
