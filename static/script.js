async function correctText() {
    const text = document.getElementById('inputText').value;
    
    const response = await fetch('/correct', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });
    
    const result = await response.json();
    document.getElementById('output').innerText = result.corrected_text;
}

async function getSuggestions() {
    const text = document.getElementById('inputText').value;

    const response = await fetch('/suggest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });

    const result = await response.json();
    document.getElementById('output').innerText += '\nSuggestions:\n' + result.suggestions.join('\n');
}

async function enhanceContent() {
    const text = document.getElementById('inputText').value;

    const response = await fetch('/enhance', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });

    const result = await response.json();
    document.getElementById('output').innerText += '\nEnhanced Content:\n' + result.enhanced_text;
}
