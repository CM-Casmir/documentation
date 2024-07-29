document.addEventListener("DOMContentLoaded", function() {
    const dataTypeSelect = document.getElementById("data-type-select");
    const dataInputRow = document.getElementById("data-input-row");
    const submitButton = document.getElementById("submit-button");

    dataTypeSelect.addEventListener("change", function() {
        const selectedValue = dataTypeSelect.value;
        if (selectedValue === "varchar" || selectedValue === "int" || selectedValue === "date" || selectedValue === "timestamp") {
            dataInputRow.style.display = "block";
            submitButton.style.display = "inline-block";
        } else {
            dataInputRow.style.display = "none";
            submitButton.style.display = "none";
        }
    });

    const saveButton = document.getElementById("save-button");
    saveButton.addEventListener("click", function() {
        const selectedValue = dataTypeSelect.value;
        if (selectedValue === "varchar" || selectedValue === "int" || selectedValue === "date" || selectedValue === "timestamp") {
            dataInputRow.style.display = "block";
            submitButton.style.display = "inline-block";
        } else {
            dataInputRow.style.display = "none";
            submitButton.style.display = "none";
        }
    });
});