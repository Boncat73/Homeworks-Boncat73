const API_URL = 'http://127.0.0.1:5001/api';

async function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const typeSelect = document.getElementById('typeSelect');
    const statusMsg = document.getElementById('statusMessage');

    if (!fileInput.files[0]) {
        alert("Виберіть файл!");
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('type', typeSelect.value);

    try {
        statusMsg.innerText = "⏳ Завантаження...";
        const response = await fetch(`${API_URL}/upload`, { method: 'POST', body: formData });
        if (response.ok) {
            statusMsg.innerText = "✅ Готово!";
            fileInput.value = '';
            loadMedia();
        }
    } catch (error) {
        statusMsg.innerText = "❌ Помилка з'єднання";
    }
}

async function loadMedia() {
    const listDiv = document.getElementById('mediaList');
    try {
        const response = await fetch(`${API_URL}/media`);
        const data = await response.json();
        listDiv.innerHTML = '';

        data.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'media-item';
            itemDiv.innerHTML = `
                <div class="media-info">
                    <span>📁 ${item.name}</span>
                    <span class="tag">${item.type}</span>
                </div>
                <button class="btn-delete" onclick="deleteMedia(${item.id})">Видалити</button>
            `;
            listDiv.appendChild(itemDiv);
        });
    } catch (error) {
        listDiv.innerHTML = '<p>Помилка завантаження списку</p>';
    }
}

// Функція для видалення
async function deleteMedia(id) {
    if (!confirm("Ви впевнені, що хочете видалити цей файл?")) return;

    try {
        const response = await fetch(`${API_URL}/delete/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            loadMedia(); // Оновлюємо список після видалення
        } else {
            alert("Не вдалося видалити файл");
        }
    } catch (error) {
        console.error("Помилка:", error);
    }
}

document.addEventListener('DOMContentLoaded', loadMedia);