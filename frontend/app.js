// app.js – Handles UI interactions and talks to Flask backend

document.addEventListener('DOMContentLoaded', () => {
  const searchBtn = document.getElementById('search-btn');
  const productInput = document.getElementById('product-input');
  const resultsDiv = document.getElementById('results');
  const resultsBody = document.getElementById('results-body');
  const messageDiv = document.getElementById('message');

  const showMessage = (msg, isError = false) => {
    messageDiv.textContent = msg;
    messageDiv.style.background = isError ? '#ff6b6b' : '#ffeb3b';
    messageDiv.classList.remove('hidden');
    setTimeout(() => messageDiv.classList.add('hidden'), 4000);
  };

  const clearResults = () => {
    resultsBody.innerHTML = '';
    resultsDiv.classList.add('hidden');
  };

  const renderResults = (data) => {
    clearResults();
    if (!data.results || data.results.length === 0) {
      showMessage('No price data found.', false);
      return;
    }
    data.results.forEach((item) => {
      const tr = document.createElement('tr');
      const platformTd = document.createElement('td');
      platformTd.textContent = item.platform;
      const priceTd = document.createElement('td');
      priceTd.textContent = item.price;
      const linkTd = document.createElement('td');
      if (item.url) {
        const a = document.createElement('a');
        a.href = item.url;
        a.textContent = 'View';
        a.target = '_blank';
        linkTd.appendChild(a);
      } else {
        linkTd.textContent = '-';
      }
      tr.appendChild(platformTd);
      tr.appendChild(priceTd);
      tr.appendChild(linkTd);
      resultsBody.appendChild(tr);
    });
    resultsDiv.classList.remove('hidden');
  };

  searchBtn.addEventListener('click', async () => {
    const query = productInput.value.trim();

    if (!query) {
      showMessage('Please enter a product name or URL.', true);
      return;
    }

    clearResults();
    showMessage('Fetching prices…');

    try {
      const payload = { product: query };

      if (query.startsWith('http://') || query.startsWith('https://')) {
        payload.url = query;
      }

      const response = await fetch('http://127.0.0.1:5000/api/compare', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Server error ${response.status}`);
      }

      const data = await response.json();
      renderResults(data);

    } catch (err) {
      console.error(err);
      showMessage('Failed to fetch prices. See console for details.', true);
    }
  });
});