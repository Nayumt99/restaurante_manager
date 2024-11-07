document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('pedido-form');
    const resultado = document.getElementById('resultado');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const data = new FormData(form);
        const jsonData = Object.fromEntries(data.entries());

        // Exibe uma mensagem de confirmação (simulação)
        resultado.textContent = `Pedido de ${jsonData.cliente_nome} foi criado com sucesso!`;

        // Exemplo de envio do pedido (descomente quando tiver API)
        /*
        const response = await fetch('/api/pedido', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        });

        if (response.ok) {
            resultado.textContent = `Pedido de ${jsonData.cliente_nome} criado com sucesso!`;
            form.reset();
        } else {
            resultado.textContent = 'Erro ao criar o pedido. Tente novamente.';
        }
        */
    });
});
