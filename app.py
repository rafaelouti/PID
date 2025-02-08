# Simulador de Controle PID em Python com Tkinter

Este projeto é uma simulação interativa de controle PID para **nível de tanque e temperatura** utilizando Python e Tkinter. Ideal para entender e visualizar o funcionamento de controladores PID em sistemas de automação.

## 📋 Funcionalidades
- **Controle PID Completo**: Ajuste dinâmico dos parâmetros Kp, Ki e Kd.
- **Simulação de Nível e Temperatura**:
  - Controle de nível de tanque com válvula (0% a 100%).
  - Simulação de temperatura com sensor virtual PT100, incluindo ruído.
  - Atraso térmico para resposta realista.
- **Interface Gráfica com Tkinter**:
  - Interface amigável com fundo amarelo e tanque visual.
  - Monitoramento em tempo real dos valores de processo (PV), abertura da válvula (MV) e temperatura.

## 🚀 Como Executar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/simulador-pid-python.git
    cd simulador-pid-python
    ```
2. Instale as dependências necessárias (se houver):
    ```bash
    pip install -r requirements.txt
    ```
3. Execute o script:
    ```bash
    python simulador_pid.py
    ```

## 🎨 Interface do Usuário
- **Set Point (SP)**: Defina o nível desejado do tanque.
- **Nível Atual (PV)**: Visualize o nível real do tanque.
- **Abertura da Válvula (MV)**: Controle automático via PID.
- **Temperatura (PT100)**: Veja a temperatura em tempo real com ruído.

## 🔧 Ajuste dos Parâmetros PID
- **Kp (Proporcional)**: Ajusta a resposta ao erro atual.
- **Ki (Integral)**: Compensa erros acumulados ao longo do tempo.
- **Kd (Derivativo)**: Suaviza a resposta para evitar oscilações.

## 📊 Exemplos de Aplicação
- Automação industrial (controle de nível, temperatura, vazão).
- Sistemas de aquecimento e refrigeração.
- Controle de motores e processos dinâmicos.

## 🛠️ Melhorias Futuras
- Adicionar gráficos para histórico de PV e MV.
- Implementar controle PID para múltiplas variáveis.
- Simular diferentes tipos de processos (temperatura, pressão).

## 🤝 Contribuindo
Contribuições são bem-vindas!  
1. Faça um fork do projeto.  
2. Crie uma branch com sua feature (`git checkout -b feature/nova-feature`).  
3. Faça o commit (`git commit -m 'Adiciona nova feature'`).  
4. Dê um push na branch (`git push origin feature/nova-feature`).  
5. Abra um Pull Request.  

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato
Criado por [Rafael Outi](https://linkedin.com/in/rafaelouti).  
Sinta-se à vontade para entrar em contato para dúvidas ou sugestões!

## ⭐ Agradecimentos
Se você achou este projeto útil, dê uma estrela ⭐ no GitHub! Isso ajuda a divulgar e motivar mais melhorias.
