document.getElementById("predictionForm").addEventListener("submit", function(event) {

    event.preventDefault();

    const cgpa = document.getElementById("cgpa").value;
    const iq = document.getElementById("iq").value;

    fetch("/predict", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            cgpa: cgpa,
            iq: iq
        })
    })

    .then(response => response.json())

    .then(data => {

        if (data.prediction) {
            document.getElementById("result").innerText =
                "Result: " + data.prediction;
        }
        else if (data.error) {
            document.getElementById("result").innerText =
                "Error: " + data.error;
        }

    })

    .catch(error => {

        console.error(error);

        document.getElementById("result").innerText =
            "Error connecting to server";

    });

});