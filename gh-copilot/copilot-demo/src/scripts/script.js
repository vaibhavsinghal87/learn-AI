document.addEventListener("DOMContentLoaded", function () {
    // Initialize the chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [{
                label: 'Sales',
                data: [0, 0, 0, 0, 0, 0, 0], // Initial data
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(201, 203, 207, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Add event listener to the Calculate button
    document.getElementById('calculate-btn').addEventListener('click', function () {
        // Get input values
        const monday = parseFloat(document.getElementById('monday').value) || 0;
        const tuesday = parseFloat(document.getElementById('tuesday').value) || 0;
        const wednesday = parseFloat(document.getElementById('wednesday').value) || 0;
        const thursday = parseFloat(document.getElementById('thursday').value) || 0;
        const friday = parseFloat(document.getElementById('friday').value) || 0;
        const saturday = parseFloat(document.getElementById('saturday').value) || 0;
        const sunday = parseFloat(document.getElementById('sunday').value) || 0;

        // Update chart data
        myChart.data.datasets[0].data = [monday, tuesday, wednesday, thursday, friday, saturday, sunday];
        myChart.update(); // Refresh the chart
    });

    // Add event listener to the Copy to Clipboard button
    document.getElementById('copy-chart-btn').addEventListener('click', function () {
        // Get the canvas element
        const canvas = document.getElementById('myChart');
    
        // Convert the canvas to a data URL (base64 image)
        const imageDataURL = canvas.toDataURL('image/png');
    
        // Create a Blob from the data URL
        const byteString = atob(imageDataURL.split(',')[1]);
        const mimeString = imageDataURL.split(',')[0].split(':')[1].split(';')[0];
        const arrayBuffer = new ArrayBuffer(byteString.length);
        const uintArray = new Uint8Array(arrayBuffer);
    
        for (let i = 0; i < byteString.length; i++) {
            uintArray[i] = byteString.charCodeAt(i);
        }
    
        const blob = new Blob([uintArray], { type: mimeString });
    
        // Create a temporary link element
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'chart-image.png'; // File name for the download
        link.click();
    
        // Clean up the URL object
        URL.revokeObjectURL(link.href);
    });
});