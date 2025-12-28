const express = require('express');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;

// Simple HTML page
const html = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo Deploy Test</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            border-radius: 16px;
            padding: 48px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            text-align: center;
            max-width: 500px;
        }
        .success-icon {
            width: 80px;
            height: 80px;
            background: #10b981;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
        }
        .success-icon svg {
            width: 40px;
            height: 40px;
            fill: white;
        }
        h1 {
            color: #1f2937;
            font-size: 28px;
            margin-bottom: 12px;
        }
        .subtitle {
            color: #6b7280;
            font-size: 16px;
            margin-bottom: 32px;
        }
        .info-grid {
            display: grid;
            gap: 16px;
            text-align: left;
        }
        .info-item {
            background: #f9fafb;
            padding: 16px;
            border-radius: 8px;
            border: 1px solid #e5e7eb;
        }
        .info-label {
            font-size: 12px;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 4px;
        }
        .info-value {
            font-size: 14px;
            color: #1f2937;
            font-family: 'SF Mono', Monaco, monospace;
            word-break: break-all;
        }
        .timestamp {
            margin-top: 24px;
            font-size: 12px;
            color: #9ca3af;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="success-icon">
            <svg viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
        </div>
        <h1>Demo Deployed!</h1>
        <p class="subtitle">Your demo-deploy module is working correctly.</p>

        <div class="info-grid">
            <div class="info-item">
                <div class="info-label">Hostname</div>
                <div class="info-value">${os.hostname()}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Node Version</div>
                <div class="info-value">${process.version}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Port</div>
                <div class="info-value">${PORT}</div>
            </div>
            <div class="info-item">
                <div class="info-label">Environment</div>
                <div class="info-value">${process.env.NODE_ENV || 'development'}</div>
            </div>
        </div>

        <p class="timestamp">Server started: ${new Date().toISOString()}</p>
    </div>
</body>
</html>
`;

app.get('/', (req, res) => {
    res.send(html);
});

app.get('/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log('Server running on port ' + PORT);
});
