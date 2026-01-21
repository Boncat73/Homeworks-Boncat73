// 1. Функція для отримання та відображення списку
async function fetchUsers() {
    const response = await fetch('/users');
    const users = await response.json();
    
    const list = document.getElementById('usersList');
    list.innerHTML = ''; // Очищуємо перед оновленням

    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = `${user.username}, ${user.age} р. (місто: ${user.city})`;
        list.appendChild(li);
    });
}

// 2. Реєстрація нового користувача
document.getElementById('regForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        age: parseInt(document.getElementById('age').value),
        city: document.getElementById('city').value
    };

    const response = await fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    });

    const result = await response.json();
    document.getElementById('responseMsg').innerText = result.message || result.error;
    
    if (response.ok) fetchUsers(); // Оновлюємо список відразу після реєстрації
});

// Кнопка оновлення
document.getElementById('loadUsers').addEventListener('click', fetchUsers);

// Автоматичне завантаження при відкритті сторінки
window.addEventListener('DOMContentLoaded', fetchUsers);