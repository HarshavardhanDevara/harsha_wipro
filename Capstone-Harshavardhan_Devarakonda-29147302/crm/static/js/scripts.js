async function searchCustomers() {
    const query = document.getElementById('search-bar').value; // Get the search query
    const response = await fetch(`/api/customers?search=${query}`); // Fetch filtered customers
    const customers = await response.json(); // Parse the JSON response

    const tableBody = document.querySelector('#customer-table tbody'); // Get the table body
    tableBody.innerHTML = ''; // Clear existing rows

    // Populate the table with filtered customers
    customers.forEach(customer => {
        const row = `
            <tr>
                <td>${customer.id}</td>
                <td>${customer.first_name}</td>
                <td>${customer.last_name}</td>
                <td>${customer.company}</td>
                <td>${customer.phone}</td>
                <td>${customer.email}</td>
                <td>
                    <a href="/customer-edit/${customer.id}" class="btn btn-warning btn-sm">Edit</a>
                    <form action="/customer-delete/${customer.id}" method="post" style="display:inline;">
                        <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                    </form>
                </td>
            </tr>
        `;
        tableBody.innerHTML += row; // Append the row to the table
    });
}

async function searchInteractions() {
    const query = document.getElementById('interaction-search-bar').value; // Get the search query
    const response = await fetch(`/api/interactions?search=${query}`); // Fetch filtered interactions
    const interactions = await response.json(); // Parse the JSON response

    const tableBody = document.querySelector('#interaction-table tbody'); // Get the table body
    tableBody.innerHTML = ''; // Clear existing rows

    // Populate the table with filtered interactions
    interactions.forEach(interaction => {
        const row = `
            <tr>
                <td>${interaction.customer_id}</td>
                <td>${interaction.date}</td>
                <td>${interaction.description}</td>
            </tr>
        `;
        tableBody.innerHTML += row; // Append the row to the table
    });
}

if (typeof io !== 'undefined') {
const socket = io();
socket.on('update_interactions', (data) => {
    console.log('New interaction:', data);

    // Dynamically add the new interaction to the table
    const tableBody = document.querySelector('#interaction-table tbody');
    const row = `
        <tr>
            <td>${data.customer_id}</td>
            <td>${data.date}</td>
            <td>${data.description}</td>
        </tr>
    `;
    tableBody.innerHTML += row; // Append the new row to the table
})};