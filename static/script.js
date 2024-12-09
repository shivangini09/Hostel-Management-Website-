document.querySelectorAll('.room').forEach(room => {
    room.addEventListener('click', async () => {
      const roomNo = room.dataset.room;
  
      if (room.classList.contains('occupied')) {
        // Fetch room details from the server
        const response = await fetch(`/room/${roomNo}`);
        const data = await response.json();
        alert(`Room ${roomNo} is occupied by ${data.student.name} (${data.student.year}).`);
      } else {
        // Open form for vacant room
        const formHTML = `
          <form method="POST" action="/room/${roomNo}">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="year">Year:</label>
            <input type="text" id="year" name="year" required>
            <button type="submit">Save</button>
          </form>
        `;
        // Optional: Open a modal or display the form dynamically
        document.body.innerHTML += `<div class="modal">${formHTML}</div>`;
      }
    });
  });
  