// ===============================
// Tea Machine Dashboard JS
// ===============================

// Runtime Chart
const runtimeCtx = document.getElementById("runtimeChart");

if (runtimeCtx) {
    new Chart(runtimeCtx, {
        type: "line",
        data: {
            labels: ["9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM"],
            datasets: [{
                label: "Running Hours",
                data: [20, 40, 35, 60, 80, 90],
                borderColor: "#22c55e",
                backgroundColor: "rgba(34,197,94,0.2)",
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "white"
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "white"
                    }
                },
                y: {
                    ticks: {
                        color: "white"
                    }
                }
            }
        }
    });
}

// Blade Chart
const bladeCtx = document.getElementById("bladeChart");

if (bladeCtx) {
    new Chart(bladeCtx, {
        type: "bar",
        data: {
            labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
            datasets: [{
                label: "Blade Stops",
                data: [3, 5, 2, 4, 1],
                backgroundColor: [
                    "#3b82f6",
                    "#22c55e",
                    "#f59e0b",
                    "#ef4444",
                    "#9333ea"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "white"
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: "white"
                    }
                },
                y: {
                    ticks: {
                        color: "white"
                    }
                }
            }
        }
    });
}


// Live Data Update
async function loadData() {

    try {

        const response = await fetch("/api/data");

        const data = await response.json();

        document.querySelector(".green h2").innerText = data.machine_status;
        document.querySelector(".blue h2").innerText = data.blade_status;
        document.querySelector(".orange h2").innerText = data.running_time;
        document.querySelector(".red h2").innerText = data.machine_on_time;
        document.querySelector(".purple h2").innerText = data.machine_off_time;
        document.querySelector(".cyan h2").innerText = data.last_sync;

    }

    catch(error){

        console.log(error);

    }

}

loadData();

setInterval(loadData,2000);